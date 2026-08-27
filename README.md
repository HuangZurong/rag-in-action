# ⚡ rag-in-action

> **RAG从小白到专家课程配套教学代码**  
> —— 5 课 × 40 分钟录播高清精课 · 亚马逊美国站服饰箱包全流程实战  
> **"Building Deterministic Engineering Harness for Probabilistic LLMs."**

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Managed with uv](https://img.shields.io/badge/managed%20by-uv-purple.svg)](https://github.com/astral-sh/uv)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![Quality Gate: 100% Faithfulness](https://img.shields.io/badge/Quality%20Gate-100%25%20Faithfulness-red.svg)](demos/lesson05_rag_triad_ci.py)
[![Repo: rag-in-action](https://img.shields.io/badge/GitHub-HuangZurong%2Frag--in--action-orange.svg)](https://github.com/HuangZurong/rag-in-action)

---

## 🗺️ 课程与代码工程架构

本项目基于现代化的 **`uv` + `pyproject.toml` (Python 3.12)** 构建，为《生产级 RAG 架构演进：从入门到专家》5 门深度录播课的官方配套代码库：

```text
rag-in-action/
├── pyproject.toml                     # 现代 Python 3.12 项目依赖与打包配置 (PEP 621)
├── .python-version                    # Python 3.12 版本约束
├── uv.lock                            # 确定性依赖锁定文件
│
├── docs/                              # 📚 5 门录播大课讲义与课件规划
│   ├── 00-course-syllabus.md          # 5 课 × 40 分钟全景大纲
│   ├── lesson-01-naive-rag.md         # 第 1 课：大模型两大硬伤与 Naive RAG 极简闭环
│   ├── lesson-02-hybrid-rerank.md     # 第 2 课：稀疏货号匹配、深度重排与 Reverse 装箱
│   ├── lesson-03-multimodal-rag.md    # 第 3 课：顶会最佳实践与多模态以图搜款
│   ├── lesson-04-ingestion-parent.md  # 第 4 课：脏数据 Ingestion 治理与 Parent-Child 父子索引
│   └── lesson-05-eval-ci-cd.md        # 第 5 课：垂直领域微调与 100% 事实忠实度发布门禁
│
├── data/                              # 📦 真实企业实战数据与知识库资产
│   ├── knowledge-base.md              # 亚马逊美国站服饰箱包知识库（FTC法规/质检单/美码大表）
│   ├── case-brief.md                  # 极光出海品牌背景与选品业务场景介绍
│   ├── eval-golden-dataset.json       # 10 道标准评测与拒答 Golden Dataset
│   └── images/                        # 多模态图库 (对接 D:\data\zby\fashion-products-small)
│
├── src/                               # ⚙️ 生产级核心 RAG 算法与工程模块库
│   ├── ingestion/                     # Ingestion 脏数据治理 (MinerU解析/表头注入/评论蒸馏)
│   ├── chunking/                      # 层次化分块 (Parent-Child 父子切片/句子窗口)
│   ├── retrieval/                     # 混合检索 (Dense + BM25 RRF) 与 Cross-Encoder 重排
│   ├── multimodal/                    # 多模态 RAG (FashionSigLIP 跨模态以图搜款)
│   ├── packing/                       # Context Repacking (Reverse 反向升序装箱)
│   └── evaluation/                    # RAG Triad 量化评估与 100% 事实忠实度发布门禁
│
└── demos/                             # 🚀 5 门课配套一键运行的实战脚本
    ├── lesson01_naive_rag.py          # 第 1 课 Demo：跑通基线与裸答翻车重现
    ├── lesson02_hybrid_bm25_rerank.py # 第 2 课 Demo：货号搜不出 ➔ BM25(RRF) + 重排修复
    ├── lesson03_multimodal_search.py  # 第 3 课 Demo：本地真实图库以图搜款
    ├── lesson04_parent_child_demo.py  # 第 4 课 Demo：跨页大表注入与父子切片实战
    └── lesson05_rag_triad_ci.py       # 第 5 课 Demo：100% 事实忠实度回归与门禁判定
```

---

## ⚡ 快速启动 (Quick Start with uv)

本项目推荐使用现代极速包管理器 [**`uv`**](https://github.com/astral-sh/uv)：

### 1. 安装项目环境与依赖 (Python 3.12)
```bash
# 克隆仓库
git clone git@github.com:HuangZurong/rag-in-action.git
cd rag-in-action

# 使用 uv 一键安装并同步虚拟环境
uv sync
```

### 2. 运行各课演示 Demo
```bash
# 运行第 1 课：基线跑通与裸答翻车复现
uv run demos/lesson01_naive_rag.py

# 运行第 2 课：混合检索与 Cross-Encoder 重排
uv run demos/lesson02_hybrid_bm25_rerank.py

# 运行第 5 课：RAG Triad 自动化回归与 100% 门禁
uv run demos/lesson05_rag_triad_ci.py
```

---

## 📜 开源协议与声明
本项目基于 Apache 2.0 开源协议，所有案例数据均为教学脱敏与模拟构造资产。
