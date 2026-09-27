# Finance-AI: Autonomous AI Agent Platform in Finance & Accounting

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Finance--AI-blue.svg" alt="Platform">
  <img src="https://img.shields.io/badge/Domain-Accounting%20%7C%20Quant%20%7C%20Risk-emerald.svg" alt="Domain">
  <img src="https://img.shields.io/badge/Tech-AI%20Agent%20%7C%20Multi--Agent%20(MAS)-purple.svg" alt="Technology">
  <img src="https://img.shields.io/badge/Language-English%20(Default)%20%7C%20%E4%B8%AD%E6%96%87-blueviolet.svg" alt="Language">
  <a href="https://www.linkedin.com/in/shunchao-zhou-aab272324/"><img src="https://img.shields.io/badge/LinkedIn-SHUNCHAOZHOU-0A66C2?logo=linkedin" alt="LinkedIn"></a>
  <img src="https://img.shields.io/badge/Status-Actively%20Updated-success.svg" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-orange.svg" alt="License">
</p>

> **Finance-AI** is an **evolving, open-source research and engineering platform** maintained by [SHUNCHAOZHOU](https://www.linkedin.com/in/shunchao-zhou-aab272324/), dedicated to exploring, designing, and operationalizing **autonomous AI Agents and Multi-Agent Systems (MAS)** across corporate accounting, intelligent auditing, quantitative research, and dynamic risk management.

🌐 **Live Interactive Website**: [**https://shunchaozhou.github.io/Finance-AI/**](https://shunchaozhou.github.io/Finance-AI/)  
*(Defaults to full English with one-click instant toggle to Chinese; includes dark/light modes, KaTeX math typesetting, code highlighting, and live interactive Multi-Agent pipeline simulations)*

---

## 🌍 Bilingual Support (双语支持)

This platform and its articles provide first-class **Bilingual (English default, Chinese optional)** reading experiences:

| Language | Live Web Article | Markdown Source | Description |
| :---: | :---: | :---: | :--- |
| **English (Default)** | [Read on Web](https://shunchaozhou.github.io/Finance-AI/articles/ai-agent-in-accounting.html) | [`ai_agent_in_accounting_en.md`](articles/ai_agent_in_accounting_en.md) | Academic & industry synthesis for international researchers and practitioners |
| **中文 (Chinese)** | [在线网页阅读](https://shunchaozhou.github.io/Finance-AI/articles/ai-agent-in-accounting.html) | [`ai_agent_in_accounting.md`](articles/ai_agent_in_accounting.md) | 针对中国准则、金税工程与本地化财务共享中心（FSSC）的深度实战解构 |

---

## 📚 Living Research Papers & Articles Matrix

| Status | Domain | Paper / Article Title | Web Version | Markdown | Code Prototype |
| :---: | :---: | :--- | :---: | :---: | :---: |
| 🟢 **Published** | **Accounting & Auditing** | **From Rule-Based Automation to Autonomous Orchestration: AI Agents in Accounting** | [Read Paper](https://shunchaozhou.github.io/Finance-AI/articles/ai-agent-in-accounting.html) | [`EN`](articles/ai_agent_in_accounting_en.md) / [`ZH`](articles/ai_agent_in_accounting.md) | [`multi_agent_accounting_demo.py`](examples/multi_agent_accounting_demo.py) |
| 🟢 **Published** | **Quantitative & Equity Research** | **Autonomous Financial Analysts: How LLM Agents Transform News Intelligence and Equity Research Reports** | [Read Paper](https://shunchaozhou.github.io/Finance-AI/articles/llm-agent-in-equity-research.html) | [`EN`](articles/llm_agent_in_equity_research_en.md) / [`ZH`](articles/llm_agent_in_equity_research.md) | [`news_to_equity_research_agent_demo.py`](examples/news_to_equity_research_agent_demo.py) |
| 🟡 *In Progress* | **Dynamic Risk & RegTech** | *Graph-RAG & LLM Agents in Related-Party Transactions and Anti-Money Laundering* | *Upcoming* | *Drafting* | *Planned* |
| 🟡 *In Progress* | **Autonomous FP&A** | *Self-Driving FP&A: Dynamic Enterprise Budgeting & Monte Carlo Cash Flow Stress Testing* | *Upcoming* | *Drafting* | *Planned* |

---

## 🏛️ System Architecture Preview (Virtual Finance Office)

```
                    +-------------------------------------+
                    |   CFO / Controller Orchestrator     |
                    +-------------------------------------+
                                       │ Task Routing & Supervision
          ┌────────────────────────────┼───────────────────────────┐
          ▼                            ▼                           ▼
+---------------------+      +---------------------+     +---------------------+
| Auditor Agent       |      | Bookkeeper Agent    |     | Recon Agent         |
+---------------------+      +---------------------+     +---------------------+
| · Tax ID Validation |      | · Account Mapping   |     | · 3-Way Matching    |
| · Policy Compliance |      | · Double-Entry Gen  |     | · Bank Rec Matching |
| · Fraud Screening   |      | · ERP API Delivery  |     | · Variance Tracing  |
+---------------------+      +---------------------+     +---------------------+
                                       │ Agent Debate & Cross-Verification
                                       ▼
                    +-------------------------------------+
                    |      Human-in-the-Loop (HITL)       |
                    | (Senior Controller Review Console)  |
                    +-------------------------------------+
```

---

## 📂 Repository Layout

```text
Finance-AI/
├── index.html                                 # Portal homepage with domain filter & roadmap (EN default / ZH toggle)
├── .github/workflows/deploy-pages.yml         # GitHub Pages CI/CD workflow
├── articles/
│   ├── ai-agent-in-accounting.html            # Interactive bilingual accounting paper page
│   ├── ai_agent_in_accounting_en.md           # English Markdown accounting source
│   ├── ai_agent_in_accounting.md              # Chinese Markdown accounting source
│   ├── llm-agent-in-equity-research.html      # Interactive bilingual equity research paper page
│   ├── llm_agent_in_equity_research_en.md     # English Markdown equity research source
│   └── llm_agent_in_equity_research.md        # Chinese Markdown equity research source
├── examples/
│   ├── multi_agent_accounting_demo.py         # Autonomous accounting & reconciliation pipeline
│   └── news_to_equity_research_agent_demo.py  # Autonomous news analysis & equity research pod
├── LICENSE                                    # MIT License
└── README.md                                  # Project overview and matrix index
```

---

## 🚀 Quickstart & Local Reproduction

### 1. Run the Multi-Agent Financial Simulations
The prototypes require only standard Python (3.8+) without heavy external dependencies:

```bash
# 1. Run the Autonomous Accounting & Reconciliation Pipeline
python3 examples/multi_agent_accounting_demo.py

# 2. Run the Autonomous Equity Research Pod (News -> Audit -> Bull/Bear Debate -> Report)
python3 examples/news_to_equity_research_agent_demo.py
```
This demonstrates compliance verification, purchase order three-way matching, double-entry voucher synthesis, and mathematical debit-credit balance guardrail assertions.

### 2. Preview the Web Portal Locally
```bash
# Start a local static HTTP server in the repository root
python3 -m http.server 8080
# Open http://localhost:8080 in your browser
```

---

## 🗺️ Engineering Roadmap

- **Phase 01 (Active)**: Autonomous accounting, continuous closing, deterministic guardrails, and MAS proof-of-concepts.
- **Phase 02 (In Queue)**: Multimodal financial document parsing, earnings call transcript sentiment models, and automated backtesting pipelines.
- **Phase 03 (Frontier)**: Live sandbox connectors to ERPs (SAP S/4HANA, NetSuite) and reinforcement learning game-theoretic trading agents.

---

## 📄 License

Distributed under the [MIT License](LICENSE). Contributions, feedback, and issue discussions are warmly welcome!
