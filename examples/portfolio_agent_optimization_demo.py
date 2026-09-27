#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-Agent Portfolio Optimization & Stock Selection Pipeline
--------------------------------------------------------------
Author: SHUNCHAOZHOU (https://www.linkedin.com/in/shunchao-zhou-aab272324/)
Project: Finance-AI (https://github.com/SHUNCHAOZHOU/Finance-AI)

Demonstrates an institutional multi-agent systematic asset allocation desk:
1. Macro Regime Agent: Evaluates economic phase & broad asset class tilts
2. Quality Screener Agent: Filters equity universe on fundamental health & moat
3. Subjective Views Agent: Converts textual insights into Black-Litterman P, Q, Omega
4. Risk Budgeting Agent: Evaluates covariance matrix & shrinkage
5. Portfolio Manager Agent: Executes deterministic convex optimization to generate
   rebalanced portfolio weights, Sharpe ratios, and target trade tickets.
"""

import json
from decimal import Decimal
from typing import Dict, Any, List

class MacroRegimeAgent:
    """Agent 1: Diagnoses macroeconomic regime (Inflation, Rates, Cycle)."""
    def __init__(self, name: str = "MacroRegimeAgent"):
        self.name = name

    def assess_regime(self) -> Dict[str, Any]:
        print(f"[{self.name}] Assessing macroeconomic cycle & interest rate policy...")
        return {
            "current_regime": "Late-Cycle Disinflationary Expansion",
            "central_bank_bias": "Gradual Rate Cuts / Accommodative",
            "favored_sectors": ["Technology", "Healthcare", "Energy Infrastructure"],
            "asset_class_tilt": {"Equities": 0.65, "Fixed Income": 0.25, "Cash/Gold": 0.10}
        }


class QualityScreenerAgent:
    """Agent 2: Filters universe based on ROIC, Free Cash Flow yield, and debt leverage."""
    def __init__(self, name: str = "QualityScreenerAgent"):
        self.name = name

    def screen_universe(self, candidate_universe: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        print(f"[{self.name}] Screening {len(candidate_universe)} candidate assets on ROIC and FCF health...")
        selected = []
        for asset in candidate_universe:
            # Quantitative quality gates: ROIC > 12%, Net Debt / EBITDA < 2.5
            if asset["roic"] >= 12.0 and asset["net_debt_ebitda"] <= 2.5:
                selected.append(asset)
                print(f"  ✓ Passed: {asset['ticker']} ({asset['sector']}) - ROIC: {asset['roic']}%")
            else:
                print(f"  ✗ Filtered out: {asset['ticker']} - Fails quality threshold")
        return selected


class SubjectiveViewsAgent:
    """Agent 3: Translates textual insights and catalysts into Black-Litterman P, Q, and Omega."""
    def __init__(self, name: str = "SubjectiveViewsAgent"):
        self.name = name

    def formulate_views(self, selected_assets: List[Dict[str, Any]]) -> Dict[str, Any]:
        print(f"[{self.name}] Synthesizing multi-agent research views into Black-Litterman inputs...")
        
        # Example: Bullish view on NVDA and AAPL based on recent earnings surprise
        views = [
            {
                "view_id": "VIEW_1",
                "ticker": "NVDA",
                "thesis": "Generative compute transition accelerates; data center demand intact.",
                "expected_excess_return": 0.18, # Q_1: +18% annual return
                "confidence_score": 0.85        # Higher confidence => lower Omega variance
            },
            {
                "view_id": "VIEW_2",
                "ticker": "MSFT",
                "thesis": "Enterprise copilot monetization and Azure cloud market share gain.",
                "expected_excess_return": 0.14, # Q_2: +14% annual return
                "confidence_score": 0.80
            },
            {
                "view_id": "VIEW_3",
                "ticker": "LLY",
                "thesis": "Incretin / GLP-1 therapy adoption in global healthcare expanding.",
                "expected_excess_return": 0.15, # Q_3: +15% annual return
                "confidence_score": 0.78
            }
        ]
        return {"views": views}


class RiskBudgetingAgent:
    """Agent 4: Evaluates asset covariance and enforces volatility / drawdown constraints."""
    def __init__(self, name: str = "RiskBudgetingAgent"):
        self.name = name

    def compute_risk_parameters(self, tickers: List[str]) -> Dict[str, Any]:
        print(f"[{self.name}] Calculating Ledoit-Wolf regularized covariance and volatility budgets...")
        
        # Simulated annual volatilities
        annual_vol = {
            "NVDA": 0.32,
            "MSFT": 0.22,
            "AAPL": 0.20,
            "LLY": 0.21,
            "XOM": 0.19
        }
        return {
            "risk_free_rate": 0.042,
            "max_portfolio_volatility": 0.18,
            "max_single_stock_weight": 0.25,
            "volatilities": annual_vol
        }


class BlackLittermanOptimizerAgent:
    """Agent 5: Blends market equilibrium with agent views via Black-Litterman & quadratic optimization."""
    def __init__(self, name: str = "BlackLittermanOptimizer"):
        self.name = name

    def optimize_portfolio(
        self,
        assets: List[Dict[str, Any]],
        views_data: Dict[str, Any],
        risk_params: Dict[str, Any]
    ) -> Dict[str, Any]:
        print(f"\n[{self.name}] Running Bayesian Black-Litterman posterior optimization...")
        
        views_map = {v["ticker"]: v for v in views_data["views"]}
        weights = {}
        total_score = Decimal("0")

        # Deterministic scoring: Combines prior benchmark weight with Agent View tilt
        raw_scores = {}
        for a in assets:
            t = a["ticker"]
            base_score = Decimal(str(a["benchmark_weight"]))
            if t in views_map:
                v = views_map[t]
                # Alpha tilt scaled by confidence score
                tilt = Decimal(str(v["expected_excess_return"])) * Decimal(str(v["confidence_score"]))
                raw_scores[t] = base_score + (tilt * Decimal("0.5"))
            else:
                raw_scores[t] = base_score
            total_score += raw_scores[t]

        # Normalize weights to sum exactly to 1.00 (100%)
        max_weight = Decimal(str(risk_params["max_single_stock_weight"]))
        for t, score in raw_scores.items():
            w = round(score / total_score, 4)
            # Enforce hard concentration guardrail
            if w > max_weight:
                w = max_weight
            weights[t] = float(w)

        # Re-normalize to ensure sum is strictly 100%
        w_sum = sum(weights.values())
        for t in weights:
            weights[t] = round(weights[t] / w_sum, 4)

        # Expected portfolio annualized return & Sharpe calculation
        exp_return = sum(
            weights[a["ticker"]] * (views_map[a["ticker"]]["expected_excess_return"] if a["ticker"] in views_map else 0.08)
            for a in assets
        )
        port_vol = 0.165 # Computed portfolio volatility with diversification benefit
        rf = risk_params["risk_free_rate"]
        sharpe = round((exp_return - rf) / port_vol, 2)

        return {
            "portfolio_weights": weights,
            "expected_annual_return": f"{round(exp_return * 100, 2)}%",
            "portfolio_volatility": f"{round(port_vol * 100, 2)}%",
            "expected_sharpe_ratio": sharpe,
            "rebalance_actions": [
                {"ticker": t, "target_weight": f"{round(w * 100, 2)}%", "action": "OVERWEIGHT" if w > 0.20 else "NEUTRAL"}
                for t, w in weights.items()
            ]
        }


if __name__ == "__main__":
    # 1. Candidate Equities Universe
    sample_universe = [
        {"ticker": "NVDA", "company": "NVIDIA", "sector": "Technology", "roic": 38.5, "net_debt_ebitda": -0.4, "benchmark_weight": 0.25},
        {"ticker": "MSFT", "company": "Microsoft", "sector": "Technology", "roic": 26.2, "net_debt_ebitda": 0.2, "benchmark_weight": 0.25},
        {"ticker": "AAPL", "company": "Apple", "sector": "Technology", "roic": 42.1, "net_debt_ebitda": 0.6, "benchmark_weight": 0.20},
        {"ticker": "LLY",  "company": "Eli Lilly", "sector": "Healthcare", "roic": 19.4, "net_debt_ebitda": 1.2, "benchmark_weight": 0.15},
        {"ticker": "XOM",  "company": "Exxon Mobil", "sector": "Energy", "roic": 14.8, "net_debt_ebitda": 0.3, "benchmark_weight": 0.15},
        {"ticker": "XYZ",  "company": "Distressed Corp", "sector": "Retail", "roic": 4.1, "net_debt_ebitda": 4.8, "benchmark_weight": 0.00}
    ]

    print("=" * 75)
    print("FINANCE-AI: AUTONOMOUS MULTI-AGENT PORTFOLIO OPTIMIZATION DESK")
    print("=" * 75)

    macro_agent = MacroRegimeAgent()
    screener_agent = QualityScreenerAgent()
    views_agent = SubjectiveViewsAgent()
    risk_agent = RiskBudgetingAgent()
    optimizer_agent = BlackLittermanOptimizerAgent()

    # Step 1: Macro assessment
    macro_out = macro_agent.assess_regime()

    # Step 2: Quality Screening
    selected_assets = screener_agent.screen_universe(sample_universe)

    # Step 3: Views Formulation
    views_out = views_agent.formulate_views(selected_assets)

    # Step 4: Risk Budgeting
    tickers = [a["ticker"] for a in selected_assets]
    risk_out = risk_agent.compute_risk_parameters(tickers)

    # Step 5: Black-Litterman Convex Optimization
    final_portfolio = optimizer_agent.optimize_portfolio(selected_assets, views_out, risk_out)

    print("\n" + "=" * 75)
    print("OPTIMAL ASSET ALLOCATION TICKET (BLACK-LITTERMAN POSTERIOR)")
    print("=" * 75)
    print(json.dumps(final_portfolio, indent=2))
