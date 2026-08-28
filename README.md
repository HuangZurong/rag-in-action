# rag-in-action

亚马逊美国站服饰箱包知识库的 RAG 入门课程代码。

代码按“先拆步骤，再串流程”的顺序组织为普通 Jupyter Notebook，最后才加入混合检索：

```text
notebooks/
├── 01-什么是RAG.ipynb
├── 02-调用大模型.ipynb
├── 03-文本向量.ipynb
├── 04-文档分块.ipynb
├── 05-向量检索.ipynb
├── 06-构建最小RAG.ipynb
├── 07-用LangChain实现RAG.ipynb
└── 08-混合检索.ipynb
```

## 运行

```bash
cd LLM/RAG/code/rag-in-action
uv sync
uv run jupyter lab
```

按顺序打开 `notebooks/` 下的 Notebook。前 6 个 Notebook 用普通 Python 展示 RAG 的基本步骤，第 7 个展示 LangChain 如何串起同一条链路，第 8 个加入 BM25 和 RRF 混合检索。

如果要调用大模型，在项目根目录创建 `.env`：

```env
LLM_API_KEY=your-api-key
LLM_BASE_URL=https://your-openai-compatible-endpoint/v1
LLM_MODEL=your-model-name
EMBEDDING_MODEL=text-embedding-3-small
```

没有 API Key 时，文档加载、分块、BM25 和 Prompt 组装仍可运行；需要 Embedding 或生成答案的单元会提示配置 API。

## 数据

`data/` 下的 Markdown 文件是教学知识库，包含产品规格、法规政策、尺码表和噪音文档。过期文档保留在数据中，用于观察检索结果中的版本问题；Notebook 默认不把文件名包含“废止”的文档放入基础检索集合。

案例数据为教学模拟资产。

