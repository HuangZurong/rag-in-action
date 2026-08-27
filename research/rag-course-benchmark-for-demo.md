# RAG 精品试讲参考课程横评

> 研究日期：2026-08-25  
> 目标：为 30–45 分钟 RAG 试讲选择可借鉴的课程结构、演示和评测方法，而不是按播放量推荐。

## 结论

没有一门公开课同时把基础直觉、可运行演示、检索失败、量化评测和生产约束讲好。最佳方案是组合借鉴：

- **最小闭环：** Abhishek Veeramalla 的 40 分钟实践课。
- **评测骨架：** DeepLearning.AI 的 Building and Evaluating Advanced RAG。
- **失败诊断：** Arize AI 的 Optimizing RAG With LLMs。
- **增强演示：** Google Cloud 的 metadata filtering 与 Vectorize 的 rerank。
- **生产延伸：** Phoenix tracing、Full Stack Deep Learning、Microsoft GraphRAG。

精品试讲不应只是“把 RAG 跑通”，而应现场完成一次：**基线失败 → 定位检索问题 → 加一种改进 → 指标证明改善。**

## 第一梯队：必看

| 资源 | 定位 | 最值得借鉴 | 不足 |
|---|---|---|---|
| [RAG Zero to Hero in 40 minutes](https://www.youtube.com/watch?v=uRwSQdMMyGY)（Abhishek Veeramalla，2026，40:53） | 最小 RAG 实践 | 裸模型失败 → 手工上下文 → 自动检索 → 完整 pipeline；有[配套代码](https://github.com/iam-veeramalla/RAG-crash-course) | 没有 hybrid、rerank、evaluation、ACL、安全与可观测性 |
| [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/courses/building-evaluating-advanced-rag)（DeepLearning.AI，2h05m） | 高级检索与评测 | Sentence Window、Auto-merging；把 Context Relevance、Groundedness、Answer Relevance 分开评估 | 不适合直接当零基础开场，生产内容不完整 |
| [Optimizing RAG With LLMs](https://www.youtube.com/watch?v=QpRTdZDR4tE)（Arize AI） | 检索失败诊断 | `40:00–41:40` 的价格查询案例清楚证明 similarity 不等于 relevance；后续用可视化和指标调 chunk | 偏工具与技术分享，主线不如课程紧凑 |
| [Advanced RAG techniques for developers](https://www.youtube.com/watch?v=sGvXO7CVwc0)（Google Cloud Tech） | 检索增强技巧 | `01:03–02:18` 用 topic/category/product metadata 先过滤再检索，适合现场 A/B | 内容短，无法独立构成完整课程 |
| [Rerank for better RAG](https://www.youtube.com/watch?v=K1F8BIgcoNk)（Vectorize） | 重排直觉 | `00:38–00:55`、`03:38–03:55`：先多召回，再从 10 个候选重排取 top 5 | 供应商视角，需改成中立概念和固定评测集 |

## 第二梯队：按需参考

| 资源 | 适用部分 | 评价 |
|---|---|---|
| [RAG Fundamentals and Advanced Techniques](https://www.youtube.com/watch?v=ea2W8IogX80)（freeCodeCamp，2024，1:36:49） | 完整入门路径、naive RAG 陷阱 | 系统性好，适合备课；试讲不宜照搬长项目流程 |
| [Complete RAG Crash Course With LangChain](https://www.youtube.com/watch?v=o126p1QN_RI)（Krish Naik，2025，2:08:08） | 工程实现与 live coding | [代码仓库](https://github.com/krishnaik06/RAG-Tutorials)便于复现；评测和生产约束偏弱 |
| [Vector Databases simply explained](https://www.youtube.com/watch?v=dN0lsF2cvm4)（AssemblyAI） | embedding 可视化 | `01:29–02:19` 的二维向量空间适合零基础；需补“距离近不等于包含答案” |
| [Chunking Strategies in RAG](https://www.youtube.com/watch?v=pIGRwMjhMaQ)（Mervin Praison） | chunking 对照 | `03:01–06:01` 与 `08:26–09:45` 可比较 fixed/recursive/semantic；不应在试讲里铺满全部算法 |
| [Phoenix tutorials](https://github.com/Arize-ai/phoenix/tree/main/tutorials)（Arize） | tracing 与 evaluation | 适合展示 query → chunks → rerank → answer 的链路和回归评测，不是完整课程 |
| [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/) | 部署、成本、反馈闭环 | 生产思维强，但不是专门的 retrieval 课程 |
| [Microsoft GraphRAG](https://microsoft.github.io/graphrag/) | Graph RAG 延伸 | 适合解释跨文档全局问题与 local/global search；不应塞进基础试讲主线 |

## 推荐的 40 分钟试讲

| 时间 | 内容 | 借鉴来源 |
|---|---|---|
| 0–4 分钟 | 展示失败：用户问产品价格，top-k 都是“语义接近”的技术文档，但没有价格答案 | Arize |
| 4–10 分钟 | 解释 RAG 信息流和“知识存储与推理解耦” | Abhishek |
| 10–16 分钟 | 用二维点图解释 embedding；强调 similarity 只负责候选排序 | AssemblyAI |
| 16–23 分钟 | 同一语料跑最小 RAG，展开 query、top-k chunk、prompt、answer | Abhishek |
| 23–30 分钟 | 制造并解释 chunk 边界、错误版本或错误产品导致的误召回 | Google Cloud / chunking 课程 |
| 30–35 分钟 | 加 metadata filter 或 rerank，只选一个增强点做前后对比 | Google Cloud / Vectorize |
| 35–40 分钟 | 用固定问题集比较 Recall@k、答案忠实度、延迟和成本，回扣开场失败 | DeepLearning.AI / Phoenix |

## 精品标准

试讲必须具备四个可观察证据：

1. **展示检索内容：** 不能只显示最终答案，要让听众看到 top-k chunk 和分数。
2. **保留失败样本：** 至少一个高相似但无答案、版本错误或权限错误的案例。
3. **做前后对比：** baseline 与改进方案使用同一语料、同一问题、同一指标。
4. **明确边界：** 跑通 demo 不等于生产可用；结尾指出索引更新、ACL、安全、评测和监控。

建议准备 8–12 条固定问题：正常命中、换说法、跨 chunk、无答案、旧版本、同名实体、无权限文档各至少一条。试讲只现场展示 3 条，其余用于课前回归，避免临场结果不可控。

## 不应照搬

- 不要现场安装环境或长时间 live coding；提前准备可复现 notebook，只修改一个参数或打开一个增强步骤。
- 不要一节课同时讲 hybrid、rerank、agentic、graph 和 production；选一个增强点讲透。
- 不要把 cosine 阈值、chunk size、overlap 或 top-k 讲成通用答案；它们必须由评测集校准。
- 不要用“答案看起来不错”作为评价；至少拆开检索命中与生成忠实度。
- 不要让框架名成为主线；先让听众看清数据如何流动、错误在哪一步发生。

## 推荐观看顺序

1. Abhishek：确认最小闭环和讲课节奏。
2. Arize `40:00–42:40`：设计核心失败案例。
3. DeepLearning.AI：建立评测骨架。
4. Google Cloud + Vectorize：选择 metadata filter 或 rerank 作为唯一增强实验。
5. Phoenix/FSDL：补最后 2–3 分钟的生产边界。
