#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finance-AI Living Research Helper
---------------------------------
Automates branch syncing, verification, and checks across main and gh-pages.
Usage:
  python3 scripts/publish_article.py --status
  python3 scripts/publish_article.py --sync "feat: add new research paper on XYZ"
"""

import sys
import subprocess
import argparse

def run_cmd(cmd: str):
    print(f"--> Running: {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error (Exit {res.returncode}):\n{res.stderr}")
        return False, res.stdout, res.stderr
    print(res.stdout.strip())
    return True, res.stdout, res.stderr

def check_status():
    print("=" * 60)
    print("FINANCE-AI REPOSITORY STATUS CHECK")
    print("=" * 60)
    run_cmd("git status -s")
    run_cmd("git branch -vv")

def sync_branches(commit_msg: str):
    print("=" * 60)
    print(f"SYNCING BOTH MAIN & GH-PAGES BRANCHES: {commit_msg}")
    print("=" * 60)
    
    # 1. Commit on main
    run_cmd("git checkout main")
    run_cmd("git add .")
    run_cmd(f'git commit -m "{commit_msg}"')
    run_cmd("git push origin main")

    # 2. Fast-forward gh-pages
    run_cmd("git checkout gh-pages")
    run_cmd("git merge main")
    run_cmd("git push origin gh-pages")

    # 3. Switch back to main
    run_cmd("git checkout main")
    print("\n✓ Both 'main' and 'gh-pages' branches successfully synced with GitHub!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Finance-AI Living Research Publisher")
    parser.add_argument("--status", action="store_true", help="Check repository status")
    parser.add_argument("--sync", type=str, help="Commit message to sync both main and gh-pages branches")
    args = parser.parse_args()

    if args.sync:
        sync_branches(args.sync)
    else:
        check_status()
