# 知识库总览

> 亚马逊美国站服饰箱包选品与质检合规知识库
> 数据集来源: HuggingFace `ceyda/fashion-products-small` (多模态图片)
> 状态: Active

## 目录结构

```
data/
├── 产品/
│   ├── 冲锋衣-JK902/
│   │   ├── 技术规格.md          DOC-PROD-JK902-TECH     Active
│   │   └── 质检报告.md          SGS-RPT-JK902-2026      Active
│   ├── 瑜伽裤-YG301/
│   │   ├── 技术规格.md          DOC-PROD-YG301-TECH     Active
│   │   └── 质检报告.md          SGS-RPT-YG301-2026      Active
│   ├── 战术背包-BP701/
│   │   ├── 技术规格.md          DOC-PROD-BP701-TECH     Active
│   │   └── 质检报告.md          SGS-RPT-BP701-2026      Active
│   └── 羊毛开衫-CR502/
│       ├── 技术规格.md          DOC-PROD-CR502-TECH     Active
│       └── 质检报告.md          SGS-RPT-CR502-2026      Active
├── 法规政策/
│   ├── FTC纺织标识法.md         DOC-POL-FTC-001         Active
│   ├── 退货政策-2026现行.md     DOC-POL-RET-2026        Active
│   └── 退货政策-2023废止.md     DOC-POL-RET-2023        Deprecated
├── 尺码表/
│   ├── 女款-2026现行.md         DOC-SIZE-W-2026         Active
│   ├── 男款-2026现行.md         DOC-SIZE-M-2026         Active
│   └── 2023废止.md              DOC-SIZE-2023            Deprecated
├── 噪音文档/
│   ├── 洗涤常识.md
│   └── 卖家基础指引.md
├── images/                      HuggingFace ceyda/fashion-products-small 缓存
├── eval-golden-dataset.json     评测黄金数据集
└── case-brief.md                业务背景简介
```

## 设计说明

- **产品文档**: 每个产品含技术规格书 (5页) 和 SGS 质检报告 (3页), 包含面料、辅料、工艺、测试数据
- **法规政策**: 含现行与废止版本, 废止版内容自然体现已过时, 不标注"干扰项"
- **尺码表**: 含完整对照矩阵、国际码转换、身材测量指南、版型说明
- **噪音文档**: 与业务无关的通用常识, 用于测试检索系统能否过滤无关内容
- **图片**: 来自 HuggingFace 数据集, 按类目分目录缓存, 为多模态 RAG 提供视觉素材
