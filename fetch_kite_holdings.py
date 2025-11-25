#!/usr/bin/env python3
"""
Kite MCP Holdings Fetcher
Demonstrates how to fetch live holdings from Kite using MCP integration
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from portfolio.analyzer import PortfolioAnalyzer
from src.kite_mcp_connector import KiteMCPConnector
import portfolio_config


def fetch_live_holdings_demo():
    """
    Demonstration of fetching live holdings from Kite MCP
    
    NOTE: This script requires MCP tools to be available in the environment.
    The actual MCP call (mcp_kite_get_holdings) must be done in an MCP-enabled context.
    """
    
    print("=" * 70)
    print("KITE MCP LIVE HOLDINGS FETCHER")
    print("=" * 70)
    print()
    
    # Check configuration
    data_source = getattr(portfolio_config, 'DATA_SOURCE', 'csv')
    kite_enabled = getattr(portfolio_config, 'KITE_MCP_ENABLED', False)
    
    print(f"📋 Current Configuration:")
    print(f"   Data Source: {data_source}")
    print(f"   Kite MCP Enabled: {kite_enabled}")
    print(f"   Auto Fallback to CSV: {getattr(portfolio_config, 'AUTO_FALLBACK_TO_CSV', True)}")
    print()
    
    # Initialize portfolio analyzer
    print("🔧 Initializing Portfolio Analyzer...")
    available_funds = getattr(portfolio_config, 'DEFAULT_AVAILABLE_FUNDS', 100000)
    analyzer = PortfolioAnalyzer(available_funds=available_funds)
    print()
    
    # Instructions for MCP usage
    print("📖 USAGE INSTRUCTIONS:")
    print()
    print("To use Kite MCP integration, you need to:")
    print()
    print("1. Enable Kite MCP in portfolio_config.py:")
    print("   KITE_MCP_ENABLED = True")
    print("   DATA_SOURCE = 'kite_mcp'  # or 'auto' for fallback")
    print()
    print("2. In an MCP-enabled environment (like this chat), use:")
    print()
    print("   from portfolio.analyzer import PortfolioAnalyzer")
    print("   analyzer = PortfolioAnalyzer()")
    print()
    print("   # Fetch from MCP (requires mcp_kite_get_holdings tool)")
    print("   # kite_data = mcp_kite_get_holdings()  # This is called by assistant")
    print()
    print("   # Load into analyzer")
    print("   analyzer.load_from_kite_mcp_data(kite_data)")
    print()
    print("3. The analyzer will transform Kite data to internal format automatically")
    print()
    print("4. Continue with normal portfolio analysis:")
    print("   analyzer.analyze_performance()")
    print("   analyzer.generate_recommendations()")
    print()
    
    # Try to load portfolio data with current config
    print("=" * 70)
    print("LOADING PORTFOLIO DATA...")
    print("=" * 70)
    print()
    
    try:
        success = analyzer.load_portfolio_data()
        
        if success and analyzer.holdings_df is not None:
            print(f"✅ Successfully loaded {len(analyzer.holdings_df)} holdings")
            print()
            print("📊 Holdings Preview:")
            print(analyzer.holdings_df[['Instrument', 'Qty.', 'Avg. cost', 'LTP', 'P&L']].head(10))
            print()
            
            # Display summary
            total_invested = analyzer.holdings_df['Invested'].sum()
            total_current = analyzer.holdings_df['Cur. val'].sum()
            total_pnl = analyzer.holdings_df['P&L'].sum()
            
            print("💰 Portfolio Summary:")
            print(f"   Total Invested: ₹{total_invested:,.2f}")
            print(f"   Current Value: ₹{total_current:,.2f}")
            print(f"   Total P&L: ₹{total_pnl:,.2f}")
            print(f"   Return: {(total_pnl/total_invested*100):.2f}%")
        else:
            print("❌ Failed to load portfolio data")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    print()
    print("=" * 70)


def show_kite_mcp_example():
    """Show example code for using Kite MCP in an MCP-enabled context"""
    
    example_code = '''
# Example: Using Kite MCP Integration in MCP-Enabled Context
# (This would be run where MCP tools are available, like in this chat)

from portfolio.analyzer import PortfolioAnalyzer

# Initialize analyzer
analyzer = PortfolioAnalyzer(available_funds=114129.60)

# Fetch live holdings using MCP tool (done by assistant)
# kite_holdings = mcp_kite_get_holdings()

# Example Kite holdings data structure:
kite_holdings = [
    {
        "tradingsymbol": "SBIN",
        "exchange": "NSE",
        "quantity": 42,
        "average_price": 852.09,
        "last_price": 982.90,
        "pnl": 5494.20,
        "day_change_percentage": 1.27,
        # ... more fields
    },
    # ... more holdings
]

# Load Kite data into analyzer
success = analyzer.load_from_kite_mcp_data(kite_holdings)

if success:
    # Holdings are now loaded and transformed
    # Continue with analysis
    print(f"Loaded {len(analyzer.holdings_df)} holdings from Kite")
    
    # Perform analysis
    analyzer.analyze_performance()
    analyzer.analyze_sector_allocation()
    
    # Generate recommendations
    recommendations = analyzer.generate_recommendations()
    
    # Export results
    analyzer.export_to_excel("portfolio_analysis_kite.xlsx")
'''
    
    print("=" * 70)
    print("KITE MCP INTEGRATION EXAMPLE CODE")
    print("=" * 70)
    print()
    print(example_code)
    print()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Kite MCP Holdings Fetcher")
    parser.add_argument('--example', action='store_true', help='Show example code')
    
    args = parser.parse_args()
    
    if args.example:
        show_kite_mcp_example()
    else:
        fetch_live_holdings_demo()
