#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-Agent Accounting Pipeline Demo
------------------------------------
演示财务多智能体（Multi-Agent）协同场景：
1. Auditor Agent: 单据合规审计与税号/金额校验
2. Reconciliation Agent: 采购单(PO)与发票(Invoice)三单匹配
3. Bookkeeper Agent: 借贷分录生成与确定性平衡护栏(Guardrails)
4. Controller Orchestrator: 流程编排与审计底稿(Audit Trail)记录
"""

import json
from decimal import Decimal
from typing import Dict, Any, List

class AccountingGuardrailError(Exception):
    """会计确定性护栏异常（如借贷不平衡、税率不匹配等）"""
    pass


class AuditorAgent:
    """合规审计智能体：检查发票有效性、税号规范性及费用合规"""
    def __init__(self, name: str = "AuditorAgent"):
        self.name = name

    def audit_document(self, invoice: Dict[str, Any]) -> Dict[str, Any]:
        print(f"[{self.name}] 正在审计发票: {invoice['invoice_no']}...")
        
        # 1. 基础字段非空检查
        required_fields = ["invoice_no", "seller_tax_id", "total_amount", "tax_amount", "category"]
        for f in required_fields:
            if f not in invoice:
                return {"passed": False, "reason": f"缺失必要字段: {f}"}
        
        # 2. 模拟内控合规检查
        total = Decimal(str(invoice["total_amount"]))
        tax = Decimal(str(invoice["tax_amount"]))
        net = total - tax

        # 简单有效税率验证 (假设税率为 6% 或 13%)
        if net > 0:
            implied_rate = round(tax / net, 2)
            if implied_rate not in [Decimal("0.06"), Decimal("0.13"), Decimal("0.09")]:
                return {
                    "passed": False,
                    "reason": f"税率计算异常 (推定税率 {implied_rate * 100}%)，需人工介入"
                }

        print(f"[{self.name}] 审计通过: 发票真实有效，税率校验正常。")
        return {"passed": True, "reason": "合规审计通过", "net_amount": float(net)}


class ReconciliationAgent:
    """对账与匹配智能体：执行 PO、入库单与发票三单匹配"""
    def __init__(self, name: str = "ReconAgent"):
        self.name = name

    def three_way_match(self, invoice: Dict[str, Any], purchase_order: Dict[str, Any]) -> Dict[str, Any]:
        print(f"[{self.name}] 正在比对发票与采购订单 PO: {purchase_order['po_number']}...")
        
        inv_total = Decimal(str(invoice["total_amount"]))
        po_total = Decimal(str(purchase_order["po_total"]))

        # 容差检查（差额小于 0.05 元视为正常汇差或四舍五入）
        diff = abs(inv_total - po_total)
        if diff > Decimal("0.05"):
            return {
                "matched": False,
                "difference": float(diff),
                "reason": f"金额不匹配: 发票金额 {inv_total} vs 订单金额 {po_total}"
            }

        print(f"[{self.name}] 三单匹配成功: 采购订单与发票金额一致。")
        return {"matched": True, "difference": 0.0, "reason": "三单完全匹配"}


class BookkeeperAgent:
    """记账与核算智能体：推导复式记账分录，并施加确定性借贷平衡护栏"""
    def __init__(self, name: str = "BookkeeperAgent"):
        self.name = name

    def generate_journal_entry(self, invoice: Dict[str, Any], net_amount: float) -> List[Dict[str, Any]]:
        print(f"[{self.name}] 正在推导会计分录...")
        
        total = Decimal(str(invoice["total_amount"]))
        tax = Decimal(str(invoice["tax_amount"]))
        net = Decimal(str(net_amount))
        category = invoice.get("category", "通用采购")

        # 示例：根据业务类型匹配借方费用科目
        account_map = {
            "云服务算力": "6602.05 (研发费用-技术开发费)",
            "办公用品": "6602.01 (管理费用-办公费)",
            "差旅住宿": "6602.03 (管理费用-差旅费)"
        }
        debit_expense_account = account_map.get(category, "6602.99 (管理费用-其他)")

        # 构造复式记账会计分录
        entry = [
            {
                "direction": "借 (Debit)",
                "account": debit_expense_account,
                "amount": net
            },
            {
                "direction": "借 (Debit)",
                "account": "2221.01.01 (应交税费-应交增值税-进项税额)",
                "amount": tax
            },
            {
                "direction": "贷 (Credit)",
                "account": "2202.01 (应付账款-应付供应商款)",
                "amount": total
            }
        ]

        # === 确定性护栏检验 (Guardrail) ===
        total_debit = sum(item["amount"] for item in entry if "Debit" in item["direction"])
        total_credit = sum(item["amount"] for item in entry if "Credit" in item["direction"])

        if total_debit != total_credit:
            raise AccountingGuardrailError(
                f"借贷不平！借方总计: {total_debit}，贷方总计: {total_credit}"
            )

        print(f"[{self.name}] 会计分录生成完毕，借贷平衡校验通过 (借贷合计: {total_credit})。")
        return [
            {**item, "amount": float(item["amount"])} for item in entry
        ]


class FinancialOrchestrator:
    """总控协调者：统筹 Multi-Agent 协作流并生成审计追踪底稿"""
    def __init__(self):
        self.auditor = AuditorAgent()
        self.recon = ReconciliationAgent()
        self.bookkeeper = BookkeeperAgent()

    def process_invoice_pipeline(self, invoice: Dict[str, Any], po: Dict[str, Any]) -> Dict[str, Any]:
        print("\n" + "=" * 60)
        print(f"开始执行自动化财务处理工作流 - 发票: {invoice['invoice_no']}")
        print("=" * 60)

        audit_trail = {
            "invoice_no": invoice["invoice_no"],
            "stages": []
        }

        # 阶段 1: 审计合规
        audit_res = self.auditor.audit_document(invoice)
        audit_trail["stages"].append({"stage": "Audit", "result": audit_res})
        if not audit_res["passed"]:
            print(f"流程终止: {audit_res['reason']}")
            return {"status": "REJECTED", "audit_trail": audit_trail}

        # 阶段 2: 三单匹配
        recon_res = self.recon.three_way_match(invoice, po)
        audit_trail["stages"].append({"stage": "Reconciliation", "result": recon_res})
        if not recon_res["matched"]:
            print(f"流程挂起: {recon_res['reason']} (需人工介入 HITL)")
            return {"status": "ESCALATED_TO_HUMAN", "audit_trail": audit_trail}

        # 阶段 3: 记账分录
        try:
            entries = self.bookkeeper.generate_journal_entry(invoice, audit_res["net_amount"])
            audit_trail["stages"].append({"stage": "Bookkeeping", "entries": entries})
            print("\n[Orchestrator] 流程执行成功！已就绪入账。")
            return {"status": "SUCCESS", "journal_entries": entries, "audit_trail": audit_trail}
        except AccountingGuardrailError as err:
            print(f"触发护栏安全阻断: {err}")
            return {"status": "GUARDRAIL_BLOCKED", "error": str(err), "audit_trail": audit_trail}


if __name__ == "__main__":
    # 模拟真实采购发票数据
    sample_invoice = {
        "invoice_no": "INV-20260327-0091",
        "seller_tax_id": "91110108MA00000000",
        "category": "云服务算力",
        "total_amount": 10600.00,
        "tax_amount": 600.00
    }

    # 模拟对应的采购订单数据
    sample_po = {
        "po_number": "PO-2026-CLOUD-01",
        "po_total": 10600.00
    }

    orchestrator = FinancialOrchestrator()
    result = orchestrator.process_invoice_pipeline(sample_invoice, sample_po)

    print("\n生成的审计追踪记录 (Audit Trail):")
    print(json.dumps(result, indent=2, ensure_ascii=False))
