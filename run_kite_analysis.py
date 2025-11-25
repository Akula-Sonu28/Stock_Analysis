#!/usr/bin/env python3
"""
Quick Kite MCP Analysis Runner
===============================

This script provides instructions for running Kite MCP analysis.

Usage:
    Just ask your Copilot assistant:
    "Fetch my Kite holdings and analyze"

Or manually:
    1. Ask Copilot to fetch holdings
    2. Run: python run_kite_analysis.py
"""

import os
import sys
import glob
from datetime import datetime

def main():
    print("\n" + "=" * 80)
    print("🚀 KITE MCP ANALYSIS QUICK START")
    print("=" * 80 + "\n")
    
    # Check for recent holdings file
    holdings_pattern = "Holding/holdings_kite_*.csv"
    holdings_files = glob.glob(holdings_pattern)
    
    if not holdings_files:
        print("❌ No Kite holdings file found!")
        print("\n💡 To fetch your latest holdings, ask your Copilot assistant:\n")
        print("   💬 'Fetch my Kite holdings and analyze'\n")
        print("The Copilot will:")
        print("  1. ✅ Fetch your live holdings from Kite")
        print("  2. ✅ Save them to CSV")
        print("  3. ✅ Run the analysis automatically")
        print("  4. ✅ Generate recommendations\n")
        print("=" * 80 + "\n")
        return 1
    
    # Find most recent holdings file
    latest_holdings = max(holdings_files, key=os.path.getmtime)
    file_date = datetime.fromtimestamp(os.path.getmtime(latest_holdings))
    
    print(f"✅ Found Kite holdings file:")
    print(f"   📁 {latest_holdings}")
    print(f"   📅 Last updated: {file_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Check if file is recent (within last 24 hours)
    hours_old = (datetime.now() - file_date).total_seconds() / 3600
    
    if hours_old > 24:
        print(f"⚠️  Warning: Holdings file is {hours_old:.1f} hours old\n")
        print("💡 For fresh data, ask your Copilot assistant:")
        print("   💬 'Fetch my latest Kite holdings'\n")
    
    # Prompt for available funds
    print("=" * 80)
    print("📊 ANALYSIS CONFIGURATION")
    print("=" * 80 + "\n")
    
    try:
        funds = input("💰 Enter available funds for investment (default: ₹94,080): ").strip()
        funds = float(funds) if funds else 94080
    except ValueError:
        funds = 94080
        print("   Using default: ₹94,080")
    
    try:
        num_stocks = input("📈 Number of stocks to analyze (0=all, default: 10): ").strip()
        num_stocks = int(num_stocks) if num_stocks else 10
    except ValueError:
        num_stocks = 10
        print("   Using default: 10")
    
    print("\n" + "=" * 80)
    print("🚀 RUNNING ANALYSIS...")
    print("=" * 80 + "\n")
    
    # Build command
    cmd = f"python analyze_top200_stocks_enhanced.py --data-source csv --portfolio-amount {funds}"
    if num_stocks > 0:
        cmd += f" -n {num_stocks}"
    
    print(f"📝 Command: {cmd}\n")
    
    # Run the analysis
    exit_code = os.system(cmd)
    
    if exit_code == 0:
        print("\n" + "=" * 80)
        print("✅ ANALYSIS COMPLETE!")
        print("=" * 80 + "\n")
        print("📊 Check the generated reports:")
        print("   • reports/Enhanced_Stock_Report_*.xlsx")
        print("   • Portfolio_Allocation_Dashboard.html\n")
    else:
        print("\n❌ Analysis failed with exit code:", exit_code)
        return exit_code
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
