#!/usr/bin/env python3
"""
Full Integration Test - Load Kite Holdings into Portfolio Analyzer
"""

import sys
sys.path.insert(0, '.')

from portfolio.analyzer import PortfolioAnalyzer

# Your actual Kite holdings data (top 10 stocks)
kite_holdings_data = [
    {"tradingsymbol":"SBIN","exchange":"NSE","quantity":42,"average_price":852.085714,"last_price":982.9,"close_price":970.6,"pnl":5494.200012,"day_change_percentage":1.26725737,"isin":"INE062A01020","product":"CNC"},
    {"tradingsymbol":"CANBK","exchange":"NSE","quantity":261,"average_price":118.62008,"last_price":147.14,"close_price":146.67,"pnl":7443.69912,"day_change_percentage":0.32044726,"isin":"INE476A01022","product":"CNC"},
    {"tradingsymbol":"PNB","exchange":"NSE","quantity":345,"average_price":107.116231,"last_price":122.44,"close_price":121.75,"pnl":5286.700305,"day_change_percentage":0.56673511,"isin":"INE160A01022","product":"CNC"},
    {"tradingsymbol":"BANKBARODA","exchange":"NSE","quantity":64,"average_price":232.4,"last_price":284.05,"close_price":281.9,"pnl":3305.6,"day_change_percentage":0.76268180,"isin":"INE028A01039","product":"CNC"},
    {"tradingsymbol":"UJJIVANSFB","exchange":"BSE","quantity":874,"average_price":48.767643,"last_price":53.4,"close_price":53.84,"pnl":4048.680018,"day_change_percentage":-0.81723626,"isin":"INE551W01018","product":"CNC"},
    {"tradingsymbol":"BANKINDIA","exchange":"BSE","quantity":113,"average_price":111.89,"last_price":146.4,"close_price":145.95,"pnl":3899.63,"day_change_percentage":0.30832477,"isin":"INE084A01016","product":"CNC"},
    {"tradingsymbol":"FEDERALBNK","exchange":"NSE","quantity":115,"average_price":221.100869,"last_price":252.96,"close_price":248.17,"pnl":3663.800065,"day_change_percentage":1.93012854,"isin":"INE171A01029","product":"CNC"},
    {"tradingsymbol":"MAHABANK","exchange":"BSE","quantity":854,"average_price":54.875409,"last_price":59.05,"close_price":58.25,"pnl":3565.100714,"day_change_percentage":1.37339056,"isin":"INE457A01014","product":"CNC"},
    {"tradingsymbol":"INDIANB","exchange":"NSE","quantity":42,"average_price":773.385714,"last_price":862.6,"close_price":854.75,"pnl":3747.000012,"day_change_percentage":0.91839719,"isin":"INE562A01011","product":"CNC"},
    {"tradingsymbol":"AXISBANK","exchange":"NSE","quantity":28,"average_price":1196.428571,"last_price":1271.4,"close_price":1269,"pnl":2099.200012,"day_change_percentage":0.18912530,"isin":"INE238A01034","product":"CNC"}
]

print("=" * 80)
print("FULL INTEGRATION TEST: KITE MCP -> PORTFOLIO ANALYZER")
print("=" * 80)
print()

# Initialize analyzer
print("🔧 Initializing Portfolio Analyzer...")
analyzer = PortfolioAnalyzer(available_funds=114129.60)
print()

# Load Kite holdings
print(f"📡 Loading {len(kite_holdings_data)} holdings from Kite MCP...")
success = analyzer.load_from_kite_mcp_data(kite_holdings_data)
print()

if success:
    print("✅ Holdings loaded successfully!")
    print()
    
    # Show holdings
    print("📊 Holdings DataFrame:")
    print(analyzer.holdings_df[['Instrument', 'Qty.', 'Avg. cost', 'LTP', 'P&L', 'Return_Pct', 'Weight']].to_string())
    print()
    
    # Show detailed summary
    total_invested = analyzer.holdings_df['Invested'].sum()
    total_current = analyzer.holdings_df['Cur. val'].sum()
    total_pnl = analyzer.holdings_df['P&L'].sum()
    total_return_pct = (total_pnl / total_invested * 100) if total_invested > 0 else 0
    
    profitable = len(analyzer.holdings_df[analyzer.holdings_df['P&L'] > 0])
    loss_making = len(analyzer.holdings_df[analyzer.holdings_df['P&L'] < 0])
    
    print("=" * 80)
    print("💰 PORTFOLIO SUMMARY")
    print("=" * 80)
    print(f"Total Holdings: {len(analyzer.holdings_df)} stocks")
    print(f"Total Invested: ₹{total_invested:,.2f}")
    print(f"Current Value: ₹{total_current:,.2f}")
    print(f"Total P&L: ₹{total_pnl:,.2f}")
    print(f"Overall Return: {total_return_pct:.2f}%")
    print(f"Profitable Stocks: {profitable}")
    print(f"Loss-Making Stocks: {loss_making}")
    print()
    
    # Top performers
    print("🏆 Top 3 Performers (by Return %):")
    top_performers = analyzer.holdings_df.nlargest(3, 'Return_Pct')[['Instrument', 'Return_Pct', 'P&L']]
    for idx, row in top_performers.iterrows():
        print(f"   {row['Instrument']}: {row['Return_Pct']:.2f}% (₹{row['P&L']:,.2f})")
    print()
    
    # Largest holdings
    print("💼 Top 3 Largest Holdings (by Weight):")
    largest = analyzer.holdings_df.nlargest(3, 'Weight')[['Instrument', 'Weight', 'Cur. val']]
    for idx, row in largest.iterrows():
        print(f"   {row['Instrument']}: {row['Weight']:.2f}% (₹{row['Cur. val']:,.2f})")
    print()
    
    print("=" * 80)
    print("✅ INTEGRATION TEST PASSED!")
    print("=" * 80)
    print()
    print("Next steps:")
    print("1. Enable Kite MCP in portfolio_config.py:")
    print("   KITE_MCP_ENABLED = True")
    print("   DATA_SOURCE = 'kite_mcp'")
    print()
    print("2. Use analyzer.load_portfolio_data() which will now support both CSV and Kite MCP")
    print()
    
else:
    print("❌ Failed to load holdings from Kite MCP")
