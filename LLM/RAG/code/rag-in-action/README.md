# ⚡ rag-in-action

> **生产级 RAG 架构演进：从入门到专家课程配套教学代码**  
> —— 7 课 × 40 分钟录播精课 · 亚马逊美国站服饰箱包全流程实战  
> **"Building Deterministic Engineering Harness for Probabilistic LLMs."**

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Managed with uv](https://img.shields.io/badge/managed%20by-uv-purple.svg)](https://github.com/astral-sh/uv)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![Repo: rag-in-action](https://img.shields.io/badge/GitHub-HuangZurong%2Frag--in--action-orange.svg)](https://github.com/HuangZurong/rag-in-action)

---

## 🗺️ 项目结构

```text
LLM/RAG/
├── code/
│   └── rag-in-action/                # ⚙️ Python 工程根目录
│   ├── pyproject.toml
│   ├── .python-version
│   ├── uv.lock
│   ├── src/                          # 核心 RAG 算法与工程模块
│   │   ├── core/                     # 文档加载
│   │   ├── ingestion/                # 多源文档解析与表头注入
│   │   ├── chunking/                 # Parent-Child 父子切片
│   │   ├── retrieval/                # 混合检索 (BM25 + Dense + RRF) 与 Cross-Encoder 重排
│   │   ├── multimodal/               # 多模态 RAG (FashionSigLIP 跨模态以图搜款)
│   │   ├── packing/                  # Context Repacking (Reverse 反向升序装箱)
│   │   └── evaluation/               # RAG Triad 量化评估
│   └── demos/                        # 各课配套一键运行脚本
│       ├── lesson01_naive_rag.py
│       ├── lesson02_hybrid_bm25_rerank.py
│       ├── lesson03_multimodal_search.py
│       ├── lesson04_parent_child_demo.py
│       └── lesson05_rag_triad_ci.py
│
├── courseware/                       # 📚 课件与演示素材
│   ├── docs/                         # 课程大纲与 PPT 审查
│   ├── output/                       # 生成的 PPT 幻灯片
│   └── demo-assets/                  # 演示素材与讲稿
│
├── data/                             # 📦 知识库与评测数据
│   ├── knowledge-base.json
│   ├── knowledge-base.md
│   ├── case-brief.md
│   ├── eval-golden-dataset.json
│   └── images/                       # 多模态图库 (HuggingFace: ceyda/fashion-products-small)
│
└── research/                         # 🔬 行业调研与对标笔记
```

---

## ⚡ 快速启动

```bash
cd LLM/RAG/code/rag-in-action
uv sync

# 运行第 1 课 Demo
uv run demos/lesson01_naive_rag.py

# 运行第 2 课 Demo
uv run demos/lesson02_hybrid_bm25_rerank.py

# 运行第 5 课 Demo
uv run demos/lesson05_rag_triad_ci.py
```

---

## 📜 开源协议与声明
本项目基于 Apache 2.0 开源协议，所有案例数据均为教学脱敏与模拟构造资产。
