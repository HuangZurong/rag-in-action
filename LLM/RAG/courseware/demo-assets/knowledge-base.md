# 极光出海（Aurora Fashion）—— 亚马逊美国站服饰箱包选品与质检合规知识库

> **知识库定位**：生产级 RAG 试讲与算法实战评测基准知识库（Amazon.com US Marketplace）  
> **类目覆盖**：女装瑜伽/运动服饰、男女户外冲锋衣、工装裤、美利奴羊毛针织、战术/轻奢箱包  
> **数据设计目标**：  
> 1. **工业级高保真性**：涵盖美国 FTC 纺织品法规、SGS 实验室质检数据（克重/静水压/耐磨）、多维跨页美码对照表、Tech Pack 规格单；  
> 2. **精准问题触发器**：内置精确字符（`Cordura 500D`、`YKK 8#`、`SKU-JK902`）、时效状态（2023 废止 vs 2026 现行）、男女版型冲突、口语时尚黑话鸿沟，专门用于制造检索翻车与验证工业修复。

---

## 目录索引

1. [DOC-US-FTC-001：美国 FTC 纺织品标识法与亚马逊防水宣传合规禁令 (2026 生效)](#doc-us-ftc-001)
2. [DOC-US-RET-001：亚马逊美国站服饰箱包退换货政策与 Q4 假日延长规则 (2026 生效)](#doc-us-ret-001)
3. [DOC-US-RET-2023-OLD：亚马逊美国站历史退换货条例 (2023 已废止·干扰项)](#doc-us-ret-2023-old)
4. [DOC-US-YG-301：极光出海裸感无痕瑜伽裤 (SKU-YG301) 选品面料与工艺规格](#doc-us-yg-301)
5. [DOC-US-JK-902：轻量防暴雨冲锋衣 (SKU-JK902) Tech Pack 与 SGS 实验室质检单](#doc-us-jk-902)
6. [DOC-US-BP-701：高耐磨战术双肩包 (SKU-BP701) Cordura 面料与五金配件标准](#doc-us-bp-701)
7. [DOC-US-SIZE-2026-WOMEN：2026 现行美码女款冲锋衣与工装裤多维剪裁标准 (含 Inseam)](#doc-us-size-2026-women)
8. [DOC-US-SIZE-2026-MEN：2026 现行美码男款冲锋衣与工装裤剪裁标准](#doc-us-size-2026-men)
9. [DOC-US-SIZE-2023-OLD：2023 历史美码冲锋衣尺码表 (已废止·偏小版型干扰项)](#doc-us-size-2023-old)
10. [DOC-US-KNIT-502：秋冬老钱风复古开衫 (SKU-CR502) 美利奴羊毛 16 针工艺技术规范](#doc-us-knit-502)
11. [DOC-NOISE-GENERIC-01：通用服饰箱包日常打理与洗涤常识 (通用干扰项)](#doc-noise-generic-01)
12. [DOC-NOISE-GENERIC-02：亚马逊全球开店通用基础指引 (无答案通用项)](#doc-noise-generic-02)

---

<span id="doc-us-ftc-001"></span>
## DOC-US-FTC-001：美国 FTC 纺织品标识法与亚马逊防水宣传合规禁令 (2026 生效)
- **文档编号**：`DOC-US-FTC-001`
- **站点/地区**：Amazon.com (美国站)
- **管理范畴**：合规法务 / 选品 Listing 审核
- **有效状态**：`Active` (生效中·2026年最新修订版)
- **关联标签**：`FTC`、`Waterproof`、`DWR`、`GORE-TEX`、`合规红线`

### 核心条款：
1. **Waterproof（全防水）标称法定条件**：
   - 根据美国联邦贸易委员会（FTC 16 CFR Part 303）及 ASTM D3393 / AATCC 127 标准，只有**整件成衣接缝处均经过全压胶密封（Fully Taped Seams）**，且面料静水压（Hydrostatic Head）测试**达到或超过 10,000 mm H2O** 时，Listing 标题与详情页方可宣称“Waterproof（防水）”。
2. **Water-Resistant / Water-Repellent（防泼水）标识限制**：
   - 若仅在织物表面喷涂 DWR（Durable Water Repellent，持久防泼水涂层）而未做全压胶处理，**严禁在 Listing 中使用“100% Waterproof”、“Stormproof”等词汇**，必须明确标注为“Water-Resistant（抗水）”或“Water-Repellent（防泼水）”，违者将触发亚马逊侵权与虚假宣传机器人封店。
3. **商标与专有面料授权**：
   - 严禁在非授权商品中直接引用“GORE-TEX”商标（该商标归 W. L. Gore & Associates 所有）；使用“Cordura”面料时，Listing 必须在后台备案英威达（Invista）的授权挂牌编号（Hangtag Serial Number）。

---

<span id="doc-us-ret-001"></span>
## DOC-US-RET-001：亚马逊美国站服饰箱包退换货政策与 Q4 假日延长规则 (2026 生效)
- **文档编号**：`DOC-US-RET-001`
- **站点/地区**：Amazon.com (美国站)
- **适用类目**：Clothing, Shoes, Bags & Accessories (服饰箱包)
- **有效状态**：`Active` (生效中·2026年最新修订版)
- **关联标签**：`Return Policy`、`Q4 Holiday`、`Free Returns`、`已拆封`

### 核心条款：
1. **常规 30 天免费退货（Free Returns）政策**：
   - 亚马逊美国站上销售的服装、鞋靴、箱包类商品，买家自签收之日起 **30 天内享有无条件免费退换货权益（Free Returns）**，无论是否由质量问题引起，退货运费均由卖家全额承担（FBA 订单自动由亚马逊平台扣除卖家物流处理费）。
2. **Q4 假日延长退货特例（Holiday Extended Return Policy）**：
   - 每年 **11 月 1 日至 12 月 31 日期间**购买的服饰箱包商品，退货窗口自动延长至**次年 1 月 31 日**。买家在此期间内发起退货，卖家不得以超过 30 天为由拒退。
3. **拆封与吊牌磨损要求**：
   - 服装吊牌已被剪下或原透明包装袋拆封，**不影响买家行使无理由全额退款权利**；卖家严禁私自向买家收取任何“Restocking Fee（包装折旧费/重新上架费）”；若商品存在明显洗涤痕迹、严重异味或人为撕裂，卖家可通过后台安全索赔（SAFE-T Claim）向亚马逊申请最高 50% 的货值补偿。

---

<span id="doc-us-ret-2023-old"></span>
## DOC-US-RET-2023-OLD：亚马逊美国站历史退换货条例 (2023 已废止·干扰项)
- **文档编号**：`DOC-US-RET-2023-OLD`
- **站点/地区**：Amazon.com (美国站)
- **适用类目**：Clothing & Luggage (服饰与箱包)
- **有效状态**：`Deprecated` (已于 2023 年 12 月 31 日全面废止)
- **关联标签**：`已废止`、`Restocking Fee`、`14天退货`、`历史版本`

### 核心条款（已失效，仅供历史归档）：
1. 买家签收商品超过 14 天后发起退换货，需自行承担寄回运费并提供 USPS Tracking 运单号。
2. 凡商品外包装已拆封或服装吊牌被摘除者，卖家有权在退款中**硬性扣除 15% 的 Restocking Fee（重新包装折旧费）**。
3. 冬季厚重服饰与大容量背包不参与平台跨年延长退货活动，严格按 14 天窗口执行。

---

<span id="doc-us-yg-301"></span>
## DOC-US-YG-301：极光出海裸感无痕瑜伽裤 (SKU-YG301) 选品面料与工艺规格
- **文档编号**：`DOC-US-YG-301`
- **站点/地区**：Amazon.com (美国站)
- **商品代号**：`SKU-YG301` (Naked-Feel High-Waist Yoga Leggings)
- **适用类目**：Women's Activewear (女士运动瑜伽服)
- **有效状态**：`Active` (2026 春夏主力选品款)

### 选品与面料核心参数：
1. **面料黄金配比**：
   - 采用 **75% Nylon 66（锦纶/超细聚酰胺纤维） + 25% Lycra Spandex（莱卡四面弹氨纶）**；
   - 纱线规格：40D/48F 双面精密经编织造，克重严格控制在 **230 GSM（±5g）**。
2. **关键功能测试指标**：
   - **防透光测试（Squat-Proof）**：深蹲极限拉伸状态下透光率 $\le 2\%$，通过 SGS 防透光等级 5 级测试；
   - **裸感双面微磨毛（Double-sided Brushed）**：表面经轻微碳素磨毛处理，提供 Butter-soft（黄油般丝滑）触感；
   - **洗涤养护标准**：支持 30℃ 正常冷水机洗（Machine Wash Cold），禁止高温烘干与氯漂，抗起球等级达 ASTM D3512 4.5 级。

---

<span id="doc-us-jk-902"></span>
## DOC-US-JK-902：轻量防暴雨冲锋衣 (SKU-JK902) Tech Pack 与 SGS 实验室质检单
- **文档编号**：`DOC-US-JK-902`
- **站点/地区**：Amazon.com (美国站)
- **商品代号**：`SKU-JK902` (Ultralight 3L Waterproof Hardshell Jacket)
- **适用类目**：Outdoor Outerwear (户外硬壳冲锋衣)
- **有效状态**：`Active` (2026 秋冬主推选品款)

### 质检与物料工程标准：
1. **面料结构与防水透湿指标**：
   - 采用 3 层复合（3-Layer Laminate）微孔膜硬壳面料；
   - **静水压测试（AATCC 127 / ISO 811）**：**$\ge 15,000 	ext{ mm H}_2	ext{O}$**（暴雨级全防水）；
   - **透湿率测试（JIS L1099 B1）**：**$\ge 18,000 	ext{ g/m}^2/24	ext{h}$**（高透气排汗）；
   - 接缝工艺：全衣采用 13mm 超窄环保 PU 热熔全压胶条（Fully Taped Seams）。
2. **专有辅料与耐磨加强部位**：
   - **肩部与肘部耐磨加强**：高频摩擦区域拼接 **Cordura 500D Ballistic Nylon（考杜拉 500D 弹道尼龙）**，马丁代尔耐磨测试（ISO 12947-2）耐磨转数 $> 50,000$ 转；
   - **拉链系统**：主门襟与腋下透气孔全量采用 **YKK 8# Vislon Aquaguard 防水拉链**。

---

<span id="doc-us-bp-701"></span>
## DOC-US-BP-701：高耐磨战术双肩包 (SKU-BP701) Cordura 面料与五金配件标准
- **文档编号**：`DOC-US-BP-701`
- **站点/地区**：Amazon.com (美国站)
- **商品代号**：`SKU-BP701` (40L Modular Tactical EDC Backpack)
- **适用类目**：Luggage & Tactical Backpacks (箱包与战术背包)
- **有效状态**：`Active` (2026 全年常青款)

### 物料与工艺标准：
1. **主料材质**：
   - 100% 原始 **Cordura 500D 涂层尼龙面料**，表面经 DuPont Teflon（特氟龙）防污三防处理；
   - 织物断裂强力（ASTM D5034）：经向 $\ge 1800	ext{ N}$，纬向 $\ge 1500	ext{ N}$。
2. **扣具与拉链五金**：
   - 全包扣具采用 **Duraflex（多耐福）UTX 军规塑钢扣具**，耐低温极限达 $-40^\circ	ext{C}$；
   - 全部口袋拉链配置 **YKK 10# 重型双向拉链**，拉链咬合强力 $\ge 120	ext{ N}$。

---

<span id="doc-us-size-2026-women"></span>
## DOC-US-SIZE-2026-WOMEN：2026 现行美码女款冲锋衣与工装裤多维剪裁标准 (含 Inseam)
- **文档编号**：`DOC-US-SIZE-2026-WOMEN`
- **站点/地区**：Amazon.com (美国站)
- **适用对象**：Women's Outerwear & Pants (女款外套与裤装)
- **有效状态**：`Active` (2026 年现行标准)

### 美码女款核心尺码对照矩阵（单位：Inches 英寸）：

| 尺码 (US Size) | 对应胸围 (Bust) | 对应腰围 (Waist) | 对应臀围 (Hip) | 袖长 (Sleeve) | 裤内长-矮版 (Petite Inseam) | 裤内长-标准 (Regular Inseam) | 裤内长-高个 (Tall Inseam) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **US XS (0-2)** | 33.0" - 34.0" | 25.5" - 26.5" | 35.5" - 36.5" | 30.5" | 27.5" | 30.0" | 32.5" |
| **US S (4-6)**  | 34.5" - 35.5" | 27.0" - 28.0" | 37.0" - 38.0" | 31.0" | 28.0" | 30.5" | 33.0" |
| **US M (8-10)** | **36.5" - 37.5"** | **29.0" - 30.5"** | **39.0" - 40.5"** | **31.5"** | **28.0"** | **31.0"** | **33.5"** |
| **US L (12-14)**| 39.0" - 40.5" | 32.0" - 33.5" | 42.0" - 43.5" | 32.0" | 28.5" | 31.5" | 34.0" |
| **US XL (16-18)**| 42.0" - 44.0" | 35.0" - 37.0" | 45.0" - 47.0" | 32.5" | 28.5" | 31.5" | 34.0" |

> **女款剪裁特征说明**：  
> 1. 女款冲锋衣在腰部设有 **$1.5	ext{ 英寸}$ 弧形立体收腰（Hourglass Fit）**，下摆设有马蹄防风弧度；  
> 2. 身高 $\le 5'4"	ext{ (162cm)}$ 的买家请推荐 **Petite Inseam（28英寸）**，避免裤腿堆叠过长。

---

<span id="doc-us-size-2026-men"></span>
## DOC-US-SIZE-2026-MEN：2026 现行美码男款冲锋衣与工装裤剪裁标准
- **文档编号**：`DOC-US-SIZE-2026-MEN`
- **站点/地区**：Amazon.com (美国站)
- **适用对象**：Men's Outerwear & Tactical Pants (男款外套与裤装)
- **有效状态**：`Active` (2026 年现行标准)

### 美码男款核心尺码对照矩阵（单位：Inches 英寸）：

| 尺码 (US Size) | 对应胸围 (Chest) | 对应腰围 (Waist) | 肩宽 (Shoulder) | 袖长 (Sleeve) | 裤内长 (Inseam-Regular) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **US S (34-36)** | 35.0" - 37.0" | 29.0" - 31.0" | 17.5" | 33.5" | 31.0" |
| **US M (38-40)** | **38.0" - 40.0"** | **32.0" - 34.0"** | **18.5"** | **34.5"** | **32.0"** |
| **US L (42-44)** | 41.0" - 43.0" | 35.0" - 37.0" | 19.5" | 35.5" | 32.5" |
| **US XL (46-48)**| 44.0" - 47.0" | 38.0" - 41.0" | 20.5" | 36.5" | 33.0" |

> **男款剪裁特征说明**：  
> 男款冲锋衣采用 **直筒宽松工装版型（Relaxed Regular Fit）**，肩部保留 $2	ext{ 英寸}$ 运动放量，便于内搭保暖抓绒衣。

---

<span id="doc-us-size-2023-old"></span>
## DOC-US-SIZE-2023-OLD：2023 历史美码冲锋衣尺码表 (已废止·偏小版型干扰项)
- **文档编号**：`DOC-US-SIZE-2023-OLD`
- **站点/地区**：Amazon.com (美国站)
- **适用对象**：Unisex (男女通用历史版型)
- **有效状态**：`Deprecated` (已于 2023 年全面废弃)

### 历史尺码（亚规改美规历史失败数据）：
- **US M 码**：胸围仅标注为 **$35.0	ext{ 英寸}$**（严重偏小，实为亚洲版型混装美码）；
- **剪裁特点**：修身窄肩，未做男女性别分版，导致退货率高达 $38\%$，已在 2024 年全量召回销毁。

---

<span id="doc-us-knit-502"></span>
## DOC-US-KNIT-502：秋冬老钱风复古开衫 (SKU-CR502) 美利奴羊毛 16 针工艺技术规范
- **文档编号**：`DOC-US-KNIT-502`
- **站点/地区**：Amazon.com (美国站)
- **商品代号**：`SKU-CR502` (Classic Heritage Relaxed Knit Cardigan)
- **适用类目**：Premium Sweaters & Knitwear (高端羊毛针织衫)
- **有效状态**：`Active` (2026 秋冬爆款选品)

### 工艺与材质细节：
1. **纱线成分与支数**：
   - 选用 **100% 澳大利亚进口超细美利奴羊毛（Extra-fine Australian Merino Wool）**，纤维细度 $\le 19.5	ext{ 微米}$；
   - 编织工艺：**德国 Stoll 电脑横机 16 针（16-Gauge）高密精纺**，质感细腻如丝，无扎肤感。
2. **版型与风格设计**：
   - 设计风格：经典复古宽松落肩版型（Relaxed Drop-shoulder Silhouette），俗称欧美“Old Money / 老钱风”核心经典穿搭款；
   - 纽扣配置：天然牛角扣（Horn Buttons），加厚 2x2 罗纹加固门襟与下摆。

---

<span id="doc-noise-generic-01"></span>
## DOC-NOISE-GENERIC-01：通用服饰箱包日常打理与洗涤常识 (通用干扰项)
- **文档编号**：`DOC-NOISE-GENERIC-01`
- **站点/地区**：Global
- **适用范围**：日常纯棉 T 恤、帆布袋等常规杂货
- **有效状态**：`Active`

1. 普通纯棉衣物建议冷水手洗，深浅色衣物分开洗涤，避免日晒褪色。
2. 帆布托特包若有局部污渍，可用软毛牙刷蘸取少量中性洗洁精局部刷洗并阴干。

---

<span id="doc-noise-generic-02"></span>
## DOC-NOISE-GENERIC-02：亚马逊全球开店通用基础指引 (无答案通用项)
- **文档编号**：`DOC-NOISE-GENERIC-02`
- **站点/地区**：Global
- **适用范围**：新卖家入驻须知

1. 卖家须确保双币信用卡状态正常，并定期更新税务信息。
2. 严禁操控评论（Review Manipulation）与刷单违规行为。
