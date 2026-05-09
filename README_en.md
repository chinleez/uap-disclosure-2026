# UAP / UFO Declassified Archives (May 2026)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Records](https://img.shields.io/badge/records-161-blue)](#headline-numbers)
[![Translated](https://img.shields.io/badge/lang-中文%20%2F%20English-green)](README.md)

[🌐 中文](README.md)

> Curated index of the UAP (formerly UFO) materials released by the U.S. government on **May 8, 2026**: **161 records** from the **Department of War, FBI, NASA, and Department of State**. The repository provides:
> - Bilingual indexes (by agency, by location)
> - Chinese translations of titles, summaries, locations, and metadata labels
> - Restructured markdown (shared case-file summaries hoisted to section heads, English originals collapsed)
> - A one-shot reproduction script driven by `download_manifest.json`
>
> All resource links point directly at the original public URLs (war.gov / cloudfront) — click and view in the browser, no clone needed. For an offline archive, `scripts/download_resources.py` mirrors the full 6.7 GB tree.

## Quick start

```bash
git clone https://github.com/chinleez/uap-disclosure-2026.git
cd uap-disclosure-2026

# Mirror the full 6.7 GB asset tree (idempotent, skips existing files)
python3 scripts/download_resources.py

# Or pull selectively
python3 scripts/download_resources.py --kinds thumb,image       # ~45 MB
python3 scripts/download_resources.py --kinds pdf --workers 16  # PDFs only
python3 scripts/download_resources.py --dry-run                 # plan, do not fetch
```

The script mirrors every asset into `downloads/` per `download_manifest.json`. If you only want to read the index, **no clone is required** — open any `.md` on GitHub and every resource link already points at its original public URL.

## Headline numbers

| Metric | Value |
|---|---|
| Total records | **161** |
| PDF documents | 119 |
| Videos | 28 |
| Images | 14 |
| DVIDS video IDs | 41 |

## Browse by agency

| Agency | Count | Link |
|---|---|---|
| Department of War | 82 | [📂 by-dow_en.md](by-dow_en.md) |
| FBI | 56 | [📂 by-fbi_en.md](by-fbi_en.md) |
| NASA | 15 | [📂 by-nasa_en.md](by-nasa_en.md) |
| Department of State | 8 | [📂 by-state_en.md](by-state_en.md) |

## Cross-cutting indexes

- [🗺️ Browse by incident location](by-location_en.md) — 37 regions, from "Western United States" to "Papua New Guinea"

## Repository layout

```
.
├── README.md / README_en.md         # entry points
├── by-{dow,fbi,nasa,state}.md / _en.md
├── by-location.md / _en.md          # cross-cutting index by location
├── uap_index.json                   # structured index (161 records)
├── translations_zh.json             # English → Chinese translation table
├── scripts/
│   └── download_resources.py        # asset mirroring script
├── downloads/                       # local assets (.gitignored, populated by the script)
│   ├── download_manifest.json
│   ├── pdf/  video/  image/  thumb/
└── LICENSE                          # CC BY 4.0
```

## Reading notes

- **Shared summaries hoisted**: records that share a case-file summary appear once at the section header, not per record (e.g. 18 FBI 62-HQ-83894 sections, 32 DOW MISREP reports, 5 Apollo 12 lunar photos).
- **English originals**: collapsed inside `<details>` blocks in the Chinese files; rendered as body text in the English files.
- **Resource links** point at the original public URLs and open directly in the browser; the download script is only needed for offline archives.
- **Compact metadata**: a single line per record — `Type · Agency · Released · Incident · Location · Redacted`.

## License

- Original government documents: **Public Domain** (17 U.S.C. § 105)
- This repository's translations, structure, and scripts: [**CC BY 4.0**](LICENSE)
- Suggested credit: `Chinese index by https://github.com/chinleez/uap-disclosure-2026 (CC BY 4.0)`

## Disclaimer

This is an unofficial, community-maintained index. The maintainers make no claims about the authenticity, completeness, or interpretation of any document. Translations are best-effort; **the English originals are authoritative**.
