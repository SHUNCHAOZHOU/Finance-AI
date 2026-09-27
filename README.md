# Finance-AI: 金融与会计领域 AI Agent 研究与实践平台

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Finance--AI-blue.svg" alt="Platform">
  <img src="https://img.shields.io/badge/Domain-Accounting%20%26%20Quant%20%26%20Risk-emerald.svg" alt="Domain">
  <img src="https://img.shields.io/badge/Tech-AI%20Agent%20%7C%20Multi--Agent-purple.svg" alt="Technology">
  <img src="https://img.shields.io/badge/Status-Actively%20Updated-success.svg" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-orange.svg" alt="License">
</p>

> **Finance-AI** 是一个**持续更新**的专注于探讨、设计与实践 **AI Agent（人工智能体）技术在现代金融科技全场景（会计核算、智能审计、量化投研、动态风控、管理会计 FP&A 等）深度落地**的开源知识库与博客平台。

---

## 🌐 在线门户网站 (GitHub Pages)

我们已将整个知识库与博客文章构建为现代化、响应式的在线网站：

👉 **在线访问链接**：[**https://shunchaozhou.github.io/Finance-AI/**](https://shunchaozhou.github.io/Finance-AI/)

### 网站核心特性：
- 🌓 **暗黑/明亮双主题**无缝切换；
- 📑 **文章专栏矩阵**：按 `会计与审计`、`量化投研`、`智能风控`、`FP&A管理会计` 多维度动态分类筛选；
- 📐 **专业学术与工业级排版**：内置 KaTeX 数学公式渲染、Prism.js 代码高亮、目录平滑滚动高亮与阅读进度条；
- ⚡ **在线交互原型演示 (Interactive Demo)**：在网页端直接体验多智能体协同（Auditor $\rightarrow$ Recon $\rightarrow$ Bookkeeper $\rightarrow$ 确定性护栏）的实时推演。

---

## 📚 博客专篇索引 (Blog Articles Matrix)

| 状态 | 领域分类 | 博客专篇名称 | 在线网页 | 纯文本 Markdown | 配套代码 |
| :---: | :---: | :--- | :---: | :---: | :---: |
| 🟢 **已发布** | **会计与审计** | **《从规则驱动到自主协同：AI Agent 在会计行业的落地演进与未来重塑》** | [进入阅读](https://shunchaozhou.github.io/Finance-AI/articles/ai-agent-in-accounting.html) | [`ai_agent_in_accounting.md`](articles/ai_agent_in_accounting.md) | [`multi_agent_accounting_demo.py`](examples/multi_agent_accounting_demo.py) |
| 🟡 *筹备中* | **量化投研** | 《多智能体投研体系：从非结构化研报解读到 Alpha 因子自动生成》 | *即将上线* | *撰写中* | *规划中* |
| 🟡 *筹备中* | **智能风控** | 《面向金税四期与反洗钱：图大模型 Agent 在关联交易与反欺诈中的实践》 | *即将上线* | *撰写中* | *规划中* |
| 🟡 *筹备中* | **管理会计** | 《自主 FP&A 智能体：如何让 AI 掌管企业动态预算与滚动现金流压力测试》 | *即将上线* | *撰写中* | *规划中* |

---

## 📂 仓库项目结构

```text
Finance-AI/
├── index.html                             # 门户主页（包含分类筛选、路线图与文章矩阵）
├── .github/workflows/deploy-pages.yml     # GitHub Pages CI/CD 自动部署脚本
├── articles/
│   ├── ai-agent-in-accounting.html        # 《AI Agent 在会计行业》在线交互式专栏页面
│   └── ai_agent_in_accounting.md          # 对应的高质量 Markdown 格式博文（便于跨平台发布）
├── examples/
│   └── multi_agent_accounting_demo.py     # 财务多智能体（MAS）处理流水线可运行原型
├── LICENSE                                # MIT 开源许可证
└── README.md                              # 仓库整体说明
```

---

## 🛠️ 本地运行与体验

### 1. 运行财务多智能体协同流水线示例
```bash
# 无需外部重量级依赖，纯 Python 原生标准库运行
python3 examples/multi_agent_accounting_demo.py
```

### 2. 本地预览在线网站
```bash
# 在项目根目录下启动轻量级本地 HTTP 服务
python3 -m http.server 8080
# 浏览器访问 http://localhost:8080 即可浏览门户网站与博客
```

---

## 🚀 持续更新与路线图 (Roadmap)

本项目由 [SHUNCHAOZHOU](https://github.com/SHUNCHAOZHOU) 发起并长期维护，旨在为金融科技从业者、会计师事务所、AI 架构师提供深度的技术见解与开源实现。

欢迎提交 **Issue** 讨论观点，或发起 **Pull Request** 贡献新场景探讨！如果你觉得本项目有启发，欢迎给个 ⭐️ **Star** 关注更新！

---

## 📄 许可证

本项目基于 [MIT 许可证](LICENSE) 开源。
