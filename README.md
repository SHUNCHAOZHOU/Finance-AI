# Finance-AI: Autonomous AI Agent Platform in Finance & Accounting

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Finance--AI-blue.svg" alt="Platform">
  <img src="https://img.shields.io/badge/Domain-Accounting%20%7C%20Quant%20%7C%20Risk%20%7C%20FP%26A-emerald.svg" alt="Domain">
  <img src="https://img.shields.io/badge/Tech-AI%20Agent%20%7C%20Multi--Agent%20(MAS)-purple.svg" alt="Technology">
  <img src="https://img.shields.io/badge/Language-English%20(Default)%20%7C%20%E4%B8%AD%E6%96%87-blueviolet.svg" alt="Language">
  <a href="https://www.linkedin.com/in/shunchao-zhou-aab272324/"><img src="https://img.shields.io/badge/LinkedIn-SHUNCHAOZHOU-0A66C2?logo=linkedin" alt="LinkedIn"></a>
  <img src="https://img.shields.io/badge/Status-Actively%20Evolving%20%26%20Updated-success.svg" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-orange.svg" alt="License">
</p>

> **Finance-AI** is an **evolving, personal living research platform** founded and maintained by [**Shunchao Zhou (SHUNCHAOZHOU)**](https://www.linkedin.com/in/shunchao-zhou-aab272324/). 
> 
> The core objective of this project is to **systematically explore, document, and engineer the frontier convergence of Autonomous AI Agents, Large Financial Models (FinLLMs), and Capital Market / Corporate Accounting infrastructure**.

🌐 **Live Interactive Research Portal**: [**https://shunchaozhou.github.io/Finance-AI/**](https://shunchaozhou.github.io/Finance-AI/)  
*(Defaults to English with instant one-click toggle to Chinese; includes dark/light modes, KaTeX math typesetting, interactive Multi-Agent pipeline simulations, and citation-grounded research notes)*

---

## 🎯 Motivation & Research Mission (为什么建立该平台？)

In modern corporate finance and institutional asset management, practitioners and researchers face a glaring paradox:

1. **The Brittle Legacy Ceiling**: Traditional financial enterprise software (RPA scripts, basic regex parsers, single-sentence FinBERT sentiment models) fails when confronted with messy, unstructured corporate documents and complex financial rhetoric.
2. **The Stochasticity vs. Determinism Dilemma**: Large Language Models (LLMs) are probabilistic engines, whereas accounting, auditing, and valuation demand **zero-tolerance mathematical precision and auditability**.

### Our Philosophical Thesis:
> **"We do not treat AI Agents as mere conversational toys, but as rigorous, auditable, goal-driven cognitive engines."**

By combining **Multi-Agent Systems (MAS)**, dialectic adversarial debate (e.g., Bull vs. Bear, Auditor vs. Bookkeeper), and deterministic code guardrails (where no calculation is left to probabilistic token prediction), this platform aims to establish the next-generation foundation for **Autonomous Continuous Accounting** and **Agentic Investment Intelligence**.

---

## 🗺️ Research Taxonomy & Living Matrix (研究六大核心矩阵)

This repository is continuously updated with in-depth academic/industrial synthesis papers and reproducible Python prototypes across six dedicated pillars:

| Pillar | Domain | Core Focus | Status |
| :---: | :--- | :--- | :---: |
| **01** | **Autonomous Accounting & Continuous Close** | Multi-source 3-way matching, bank rec fuzzy clustering, self-healing month-end close | 🟢 **Published** |
| **02** | **Institutional Equity Research & News Alpha** | Causal event graphs, 10-Q fundamental cross-auditing, Bull-vs-Bear adversarial debate | 🟢 **Published** |
| **03** | **Systematic Stock Picking & Dynamic Asset Allocation** | Bayesian Black-Litterman model integration, multi-agent view matrices (P, Q, Ω), convex solvers | 🟢 **Published** |
| **04** | **Dynamic Risk & Graph RegTech** | Graph-RAG agents for related-party transaction discovery, anti-money laundering (AML) | 🟡 *In Progress* |
| **05** | **Autonomous FP&A & Corporate Treasury** | Voucher-level variance attribution, rolling 90-day Monte Carlo liquidity stress testing | 🟡 *In Progress* |
| **06** | **Game-Theoretic Market Simulation** | Multi-agent algorithmic trading sandboxes with reinforcement learning and ZKP privacy | 🟡 *Frontier* |

---

## 📚 Published Research Papers (已发布旗舰论文)

### 1. Corporate Accounting & Record-to-Report (R2R)
- **Title**: *From Rule-Based Automation to Autonomous Orchestration: The Evolution and Re-architecture of AI Agents in Accounting*
- **Interactive Web Page**: [Read Online](https://shunchaozhou.github.io/Finance-AI/articles/ai-agent-in-accounting.html)
- **Source Files**: English ([`ai_agent_in_accounting_en.md`](articles/ai_agent_in_accounting_en.md)) / 中文 ([`ai_agent_in_accounting.md`](articles/ai_agent_in_accounting.md))
- **Executable Prototype**: [`examples/multi_agent_accounting_demo.py`](examples/multi_agent_accounting_demo.py)
- **Key Concepts**: Four-pillar Agent engine, Financial Chain-of-Thought (F-CoT), deterministic double-entry balance guardrails ($\sum \text{Debit} - \sum \text{Credit} \equiv 0.00$).

### 2. Quantitative Intelligence & Equity Research
- **Title**: *Autonomous Financial Analysts: How LLM Agents Transform Financial News Intelligence and Equity Research Reports*
- **Interactive Web Page**: [Read Online](https://shunchaozhou.github.io/Finance-AI/articles/llm-agent-in-equity-research.html)
- **Source Files**: English ([`llm_agent_in_equity_research_en.md`](articles/llm_agent_in_equity_research_en.md)) / 中文 ([`llm_agent_in_equity_research.md`](articles/llm_agent_in_equity_research.md))
- **Executable Prototype**: [`examples/news_to_equity_research_agent_demo.py`](examples/news_to_equity_research_agent_demo.py)
- **Key Concepts**: Causal transmission vectors, cross-modal 10-Q fundamental triangulation, adversarial Bull-vs-Bear debate, and grounded research notes.

### 3. Systematic Stock Picking & Dynamic Asset Allocation
- **Title**: *Autonomous Portfolio Management: How LLM Multi-Agent Systems Revolutionize Systematic Stock Picking & Dynamic Asset Allocation*
- **Interactive Web Page**: [Read Online](https://shunchaozhou.github.io/Finance-AI/articles/llm-agent-in-portfolio-selection.html)
- **Source Files**: English ([`llm_agent_in_portfolio_selection_en.md`](articles/llm_agent_in_portfolio_selection_en.md)) / 中文 ([`llm_agent_in_portfolio_selection.md`](articles/llm_agent_in_portfolio_selection.md))
- **Executable Prototype**: [`examples/portfolio_agent_optimization_demo.py`](examples/portfolio_agent_optimization_demo.py)
- **Key Concepts**: Bayesian Black-Litterman model, Agent subjective view matrices ($P, Q, \Omega$), Ledoit-Wolf covariance shrinkage, and quadratic programming with turnover friction.

---

## 🏛️ System Architecture Preview (Multi-Agent Equity Research Pod)

```
                                  [Real-Time Financial News / SEC Filings]
                                                     │
                                                     ▼
                                      +------------------------------+
                                      | 1. News Ingestion & Filter   |
                                      |    (Event Extraction Agent)  |
                                      +------------------------------+
                                                     │ Cleaned Events & Claims
                                                     ▼
                                      +------------------------------+
                                      | 2. Financial Verification    |
                                      |    (Fundamental Auditor)     | <──> [FactSet/EDGAR API]
                                      +------------------------------+
                                                     │ Triangulated Evidence
                                                     ▼
                               +─────────────────────────────────────────────+
                               │ 3. Adversarial Multi-Agent Debate Pod       │
                               │                                             │
                               │   +------------------+   +----------------+ │
                               │   | Bull Analyst     |   | Bear Analyst   | │
                               │   | (Growth, Moat,   |<─>| (Risks, Margin | │
                               │   |  Catalysts)      |   |  Compression)  | │
                               │   +------------------+   +----------------+ │
                               +─────────────────────────────────────────────+
                                                     │ Debate Transcript & Weights
                                                     ▼
                                      +------------------------------+
                                      | 4. Chief Investment Officer  |
                                      |    (CIO Synthesis Agent)     |
                                      +------------------------------+
                                                     │
                                                     ▼
                          [Institution-Grade Research Report + Target Price + Rating]
```

---

## 📂 Repository Layout

```text
Finance-AI/
├── index.html                                 # Web portal with domain filtering & research mission (EN default / ZH toggle)
├── .github/workflows/deploy-pages.yml         # GitHub Pages automated CI/CD pipeline
├── articles/
│   ├── ai-agent-in-accounting.html            # Interactive bilingual accounting paper
│   ├── ai_agent_in_accounting_en.md           # English Markdown accounting source
│   ├── ai_agent_in_accounting.md              # Chinese Markdown accounting source
│   ├── llm-agent-in-equity-research.html      # Interactive bilingual equity research paper
│   ├── llm_agent_in_equity_research_en.md     # English Markdown equity research source
│   └── llm_agent_in_equity_research.md        # Chinese Markdown equity research source
├── examples/
│   ├── multi_agent_accounting_demo.py         # Autonomous accounting & reconciliation MAS prototype
│   ├── news_to_equity_research_agent_demo.py  # Autonomous news analysis & equity research pod prototype
│   └── portfolio_agent_optimization_demo.py   # Multi-agent stock picking & Black-Litterman allocation
├── scripts/
│   └── publish_article.py                     # Automation script for branch syncing & verification
├── LICENSE                                    # MIT License
└── README.md                                  # Repository overview and research manifesto
```

---

## 🚀 Quickstart & Local Reproduction

### 1. Run the Multi-Agent Financial Simulations
The prototypes are built with pure Python (3.8+) standard libraries with zero external bloat:

```bash
# 1. Run the Autonomous Accounting & Reconciliation Pipeline
python3 examples/multi_agent_accounting_demo.py

# 2. Run the Autonomous Equity Research Pod (News -> Audit -> Bull/Bear Debate -> Report)
python3 examples/news_to_equity_research_agent_demo.py

# 3. Run the Autonomous Portfolio Optimization & Black-Litterman Allocation Desk
python3 examples/portfolio_agent_optimization_demo.py
```

### 2. Preview the Web Portal Locally
```bash
# Start a local static HTTP server in the repository root
python3 -m http.server 8080
# Open http://localhost:8080 in your browser
```

---

## ✍️ How New Research is Added (文章持续更新流程)

Whenever new papers or prototypes are developed:
1. Write the research paper in Markdown (`articles/your_topic_en.md` and `articles/your_topic.md`).
2. Generate or adapt the interactive HTML companion (`articles/your_topic.html`).
3. Add a runnable simulation script in `examples/`.
4. Run the automated publishing helper to sync both `main` and `gh-pages` branches:
   ```bash
   python3 scripts/publish_article.py --sync "feat: add research paper on XYZ"
   ```

---

## 👨‍💻 About the Author (关于作者)

**Shunchao Zhou (周顺超)**  
- **LinkedIn**: [https://www.linkedin.com/in/shunchao-zhou-aab272324/](https://www.linkedin.com/in/shunchao-zhou-aab272324/)  
- **GitHub**: [SHUNCHAOZHOU](https://github.com/SHUNCHAOZHOU)  
- **Research Interests**: Autonomous AI Agents, Large Financial Models, Multi-Agent Game Theory, Continuous Corporate Accounting, and Quantitative NLP.

If you are an academic researcher, fintech practitioner, or institutional investor interested in collaborating or discussing the future of AI Agents in finance, feel free to connect via LinkedIn or open an issue/PR!

---

## 📄 License

Distributed under the [MIT License](LICENSE).
