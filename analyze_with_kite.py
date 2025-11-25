#!/usr/bin/env python3
"""
Analyze Top 200 Stocks with Live Kite Holdings
==============================================

This wrapper script fetches live holdings from Kite MCP and then runs
the comprehensive stock analysis with your current portfolio.

Usage:
    python analyze_with_kite.py --portfolio-amount 100000 -n 10

Note: This requires Kite MCP integration to be set up.
      Run setup_kite_mcp.py first to configure.
"""

import sys
import os
import argparse
import pandas as pd
from datetime import datetime

def main():
    """Main wrapper function"""
    
    print("\n" + "=" * 90)
    print("📊 KITE MCP LIVE HOLDINGS ANALYSIS")
    print("=" * 90)
    print("\n🔄 Fetching live holdings from Kite...\n")
    
    # Parse arguments to pass through
    parser = argparse.ArgumentParser(description='Analyze stocks with live Kite holdings')
    parser.add_argument('--portfolio-amount', type=float, default=100000, 
                       help='Available funds for new investments')
    parser.add_argument('-n', '--num', type=int, default=0,
                       help='Number of stocks to analyze')
    parser.add_argument('-w', '--workers', type=int, default=3,
                       help='Number of worker threads')
    parser.add_argument('--risk-profile', type=str, 
                       choices=['conservative', 'moderate', 'aggressive', 'balanced'],
                       default='moderate', help='Risk profile')
    
    args = parser.parse_args()
    
    # Check if Kite MCP is configured
    try:
        import portfolio_config
        if not getattr(portfolio_config, 'KITE_MCP_ENABLED', False):
            print("❌ Kite MCP is not enabled in portfolio_config.py")
            print("\n💡 To enable Kite MCP:")
            print("   1. Run: python setup_kite_mcp.py")
            print("   2. Follow the interactive configuration")
            print("   3. Then run this script again\n")
            return 1
    except ImportError:
        print("❌ portfolio_config.py not found")
        print("\n💡 Run setup_kite_mcp.py to create configuration\n")
        return 1
    
    # Import Kite connector
    try:
        from src.kite_mcp_connector import KiteMCPConnector
        connector = KiteMCPConnector()
    except ImportError:
        print("❌ Kite MCP connector not found")
        print("\n💡 Ensure src/kite_mcp_connector.py exists\n")
        return 1
    
    # ***** IMPORTANT *****
    # This script REQUIRES Copilot/MCP context to fetch holdings
    # It cannot directly call mcp_kite_get_holdings
    # 
    # The proper workflow is:
    # 1. User tells Copilot: "Fetch my Kite holdings and run analysis"
    # 2. Copilot calls: mcp_kite_get_holdings
    # 3. Copilot saves holdings to CSV
    # 4. Copilot runs: python analyze_top200_stocks_enhanced.py
    
    print("=" * 90)
    print("⚠️  MCP CONTEXT REQUIRED")
    print("=" * 90)
    print("\nThis script requires MCP (Model Context Protocol) to fetch live holdings.")
    print("\nInstead of running this script directly, please ask your Copilot assistant:")
    print("\n  💬 'Fetch my Kite holdings and run stock analysis'")
    print("\nThe Copilot will:")
    print("  1. ✅ Fetch your live holdings from Kite")
    print("  2. ✅ Save them to a CSV file")
    print("  3. ✅ Run the comprehensive analysis")
    print("  4. ✅ Generate allocation recommendations")
    print("\n" + "=" * 90)
    print("\nAlternatively, you can:")
    print("  1. Run: python fetch_kite_holdings.py")
    print("  2. Then: python analyze_top200_stocks_enhanced.py")
    print("=" * 90 + "\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
