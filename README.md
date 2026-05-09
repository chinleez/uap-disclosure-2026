# UAP / UFO 解密资料汇总（2026 年 5 月）

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Records](https://img.shields.io/badge/records-161-blue)](#关键数字)
[![Translated](https://img.shields.io/badge/lang-中文%20%2F%20English-green)](README_en.md)

[🌐 English](README_en.md)

> 本仓库整理了美国政府于 **2026 年 5 月 8 日**公开的 UAP（不明异常现象，原 UFO）解密资料，包含来自**国防部、FBI、NASA、国务院**的 **161 份档案**。仓库提供：
> - 中英文双语索引（按机构、按地点）
> - 中文翻译（标题、简介、地点、字段标签）
> - 重新组织的 markdown 文档（同案卷重复简介合并、英文原文折叠）
> - 一键复现下载脚本（基于 `download_manifest.json`）
>
> ⚠️ **二进制资源（PDF / 视频 / 图片，约 6.7 GB）不入库**，请使用下方脚本按需下载到本地后即可离线浏览。

## 快速开始

```bash
git clone https://github.com/chinleez/uap-disclosure-2026.git
cd uap-disclosure-2026

# 一键复现 6.7 GB 本地资源（断点续传，跳过已存在文件）
python3 scripts/download_resources.py

# 仅按需拉取部分类型
python3 scripts/download_resources.py --kinds thumb,image       # 仅缩略图与图片，约 45 MB
python3 scripts/download_resources.py --kinds pdf --workers 16  # 仅 PDF
python3 scripts/download_resources.py --dry-run                 # 不下载，只看清单
```

下载完成后所有 markdown 中的本地链接（如 `downloads/pdf/...`）即可正常打开。**未下载时也可在 GitHub 网页上浏览所有文档**，仅资源链接不可达。

## 关键数字

| 项 | 值 |
|---|---|
| 记录总数 | **161** |
| PDF 文档 | 119 |
| 视频 | 28 |
| 图片 | 14 |
| DVIDS 视频 ID | 41 |

## 按机构浏览

| 机构 | 数量 | 链接 |
|---|---|---|
| 美国国防部（DOW） | 82 | [📂 by-dow.md](by-dow.md) |
| FBI（美国联邦调查局） | 56 | [📂 by-fbi.md](by-fbi.md) |
| NASA（美国国家航空航天局） | 15 | [📂 by-nasa.md](by-nasa.md) |
| 美国国务院 | 8 | [📂 by-state.md](by-state.md) |

## 跨主题索引

- [🗺️ 按事件地点查阅](by-location.md)（37 个区域，从「美国西部」到「巴布亚新几内亚」）

## 仓库结构

```
.
├── README.md / README_en.md         ← 入口文档
├── by-dow.md / by-dow_en.md         ← 国防部档案（82）
├── by-fbi.md / by-fbi_en.md         ← FBI 档案（56）
├── by-nasa.md / by-nasa_en.md       ← NASA 档案（15）
├── by-state.md / by-state_en.md     ← 国务院档案（8）
├── by-location.md / _en.md          ← 按事件地点交叉索引
├── uap_index.json                   ← 结构化索引（161 条完整记录）
├── translations_zh.json             ← 英→中翻译表
├── scripts/
│   └── download_resources.py        ← 资源复现脚本
├── downloads/                       ← 本地资源（.gitignore，跑脚本生成）
│   ├── download_manifest.json       ← 下载清单
│   ├── pdf/  video/  image/  thumb/
└── LICENSE                          ← CC BY 4.0
```

## 阅读说明

- **共享简介合并**：同一案卷的多个 section 共享一段背景简介，已合并到组顶展示，不再每条重复（FBI 案卷 18 条、DOW MISREP 32 条、阿波罗 12 月面 5 条等）。
- **英文原文折叠**：默认收起，点击 `<details>` 展开核对。
- **本地资源链接**：默认指向 `downloads/...`；跑下载脚本后即可离线浏览。下载失败的 3 条保留原始 URL 作为回退。
- **元数据单行紧凑**：`类型 · 机构 · 发布日 · 事件日 · 地点 · 是否删改`。

## 数据来源

- 原始档案：<https://www.war.gov/medialink/ufo/release_1/>
- 视频与缩略图：<https://www.dvidshub.net/>
- 美国政府公开档案，根据 17 U.S.C. § 105 进入公有领域

## License

- 美国政府原始档案：**Public Domain**（17 U.S.C. § 105）
- 本仓库的中文翻译、文档结构、脚本：[**CC BY 4.0**](LICENSE)
- 引用建议：`Chinese index by https://github.com/chinleez/uap-disclosure-2026 (CC BY 4.0)`

## 免责声明

本仓库为非官方、社区维护的索引。维护者不对任何文档的真实性、完整性或解读做出主张。中文翻译为尽力而为，**英文原文（折叠在 `<details>` 块中）为权威来源**。
