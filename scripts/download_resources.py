#!/usr/bin/env python3
"""
Download / mirror the UAP resources referenced by the markdown index.

Reads `downloads/download_manifest.json` (or the path passed via
`--manifest`) and recreates the local `downloads/` directory tree by
fetching every asset whose status is "downloaded" in the manifest.

Resources are skipped if the local file already exists with matching
size, so the script is idempotent and safe to re-run.

Usage:
    python3 scripts/download_resources.py
    python3 scripts/download_resources.py --workers 16 --kinds pdf,thumb
    python3 scripts/download_resources.py --dry-run

Requirements: Python 3.8+ (stdlib only).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = REPO_ROOT / "downloads" / "download_manifest.json"
USER_AGENT = "uap-disclosure-2026/1.0 (+https://github.com/chinleez/uap-disclosure-2026)"


def normalize_local_path(raw: str) -> Path:
    """Manifest paths are absolute-ish (`output/downloads/...`).

    The repo root corresponds to the original `output/` directory, so we
    strip the leading `output/` prefix when present.
    """
    raw = raw.replace("\\", "/")
    if raw.startswith("output/"):
        raw = raw[len("output/"):]
    return REPO_ROOT / raw


def should_skip(local_path: Path) -> bool:
    """Skip when the local file already exists and is non-empty."""
    return local_path.exists() and local_path.stat().st_size > 0


def fetch(url: str, dest: Path, timeout: int = 60, retries: int = 3) -> tuple[bool, str]:
    """Download `url` to `dest` with simple retry. Returns (ok, message)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    last_err: str = ""
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp, open(tmp, "wb") as fh:
                while True:
                    chunk = resp.read(64 * 1024)
                    if not chunk:
                        break
                    fh.write(chunk)
            tmp.replace(dest)
            return True, f"ok ({dest.stat().st_size:,} B)"
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
            last_err = f"{type(exc).__name__}: {exc}"
            if tmp.exists():
                try:
                    tmp.unlink()
                except OSError:
                    pass
            if attempt < retries:
                time.sleep(2 * attempt)
    return False, last_err


def iter_targets(manifest: list[dict], kinds: set[str] | None) -> Iterable[dict]:
    for entry in manifest:
        if entry.get("status") != "downloaded":
            continue
        if kinds and entry.get("asset_kind") not in kinds:
            continue
        if not entry.get("url") or not entry.get("path"):
            continue
        yield entry


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST),
                        help="Path to download_manifest.json (default: downloads/download_manifest.json)")
    parser.add_argument("--workers", type=int, default=8,
                        help="Concurrent download workers (default: 8)")
    parser.add_argument("--kinds", default="",
                        help="Comma-separated asset kinds to fetch: image,pdf,thumb,video. "
                             "Empty = all.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would be downloaded, do not fetch.")
    args = parser.parse_args(argv)

    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = REPO_ROOT / manifest_path
    if not manifest_path.exists():
        print(f"manifest not found: {manifest_path}", file=sys.stderr)
        return 2

    with manifest_path.open() as fh:
        manifest = json.load(fh)

    kinds = {k.strip() for k in args.kinds.split(",") if k.strip()} or None
    targets = list(iter_targets(manifest, kinds))
    if not targets:
        print("nothing to do (manifest is empty or all entries filtered out)")
        return 0

    print(f"Repo root: {REPO_ROOT}")
    print(f"Targets:   {len(targets)} entries"
          + (f" (kinds: {sorted(kinds)})" if kinds else ""))

    todo: list[tuple[str, Path]] = []
    skipped = 0
    for entry in targets:
        local = normalize_local_path(entry["path"])
        if should_skip(local):
            skipped += 1
            continue
        todo.append((entry["url"], local))

    print(f"Already present: {skipped}")
    print(f"To fetch:        {len(todo)}")

    if args.dry_run or not todo:
        for url, local in todo[:10]:
            print(f"  would fetch: {url} -> {local.relative_to(REPO_ROOT)}")
        if len(todo) > 10:
            print(f"  ...and {len(todo) - 10} more")
        return 0

    successes = failures = 0
    started = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(fetch, url, local): (url, local) for url, local in todo}
        for i, fut in enumerate(as_completed(futures), 1):
            url, local = futures[fut]
            ok, msg = fut.result()
            tag = "OK " if ok else "FAIL"
            print(f"[{i:>3d}/{len(todo)}] {tag} {local.relative_to(REPO_ROOT)} — {msg}")
            successes += int(ok)
            failures += int(not ok)

    elapsed = time.time() - started
    print(f"\nDone in {elapsed:.1f}s — success {successes}, fail {failures}, skipped {skipped}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
