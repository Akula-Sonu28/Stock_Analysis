#!/usr/bin/env python3
"""
Complete Demo: Fetch and Analyze Live Holdings from Kite MCP
This demonstrates the full workflow with your actual Kite holdings
"""

import sys
sys.path.insert(0, '.')

from portfolio.analyzer import PortfolioAnalyzer

# ALL 26 holdings from your Kite account (with quantity > 0)
all_kite_holdings = [
    {"tradingsymbol":"AUBANK","exchange":"NSE","instrument_token":5436929,"isin":"INE949L01017","product":"CNC","quantity":20,"average_price":729.5,"last_price":933.85,"close_price":925.1,"pnl":4087.0,"day_change_percentage":0.9458436926},
    {"tradingsymbol":"AXISBANK","exchange":"NSE","instrument_token":1510401,"isin":"INE238A01034","product":"CNC","quantity":28,"average_price":1196.428571,"last_price":1271.4,"close_price":1269,"pnl":2099.200012,"day_change_percentage":0.1891252955},
    {"tradingsymbol":"BANKBARODA","exchange":"NSE","instrument_token":1195009,"isin":"INE028A01039","product":"CNC","quantity":64,"average_price":232.4,"last_price":284.05,"close_price":281.9,"pnl":3305.6,"day_change_percentage":0.7626818021},
    {"tradingsymbol":"BANKINDIA","exchange":"BSE","instrument_token":136230148,"isin":"INE084A01016","product":"CNC","quantity":113,"average_price":111.89,"last_price":146.4,"close_price":145.95,"pnl":3899.63,"day_change_percentage":0.3083247688},
    {"tradingsymbol":"CANBK","exchange":"NSE","instrument_token":2763265,"isin":"INE476A01022","product":"CNC","quantity":261,"average_price":118.62008,"last_price":147.14,"close_price":146.67,"pnl":7443.69912,"day_change_percentage":0.3204472626},
    {"tradingsymbol":"CUB","exchange":"BSE","instrument_token":136245764,"isin":"INE491A01021","product":"CNC","quantity":220,"average_price":231.7955,"last_price":275.4,"close_price":271.55,"pnl":9592.99,"day_change_percentage":1.417786780},
    {"tradingsymbol":"FEDERALBNK","exchange":"NSE","instrument_token":261889,"isin":"INE171A01029","product":"CNC","quantity":115,"average_price":221.100869,"last_price":252.96,"close_price":248.17,"pnl":3663.800065,"day_change_percentage":1.930128541},
    {"tradingsymbol":"GICRE","exchange":"BSE","instrument_token":138433284,"isin":"INE481Y01014","product":"CNC","quantity":148,"average_price":380.40777,"last_price":381.2,"close_price":379.4,"pnl":117.25004,"day_change_percentage":0.4744333158},
    {"tradingsymbol":"GPPL","exchange":"NSE","instrument_token":5051137,"isin":"INE517F01014","product":"CNC","quantity":91,"average_price":176,"last_price":179.65,"close_price":179.88,"pnl":332.15,"day_change_percentage":-0.1278630198},
    {"tradingsymbol":"HDFCBANK","exchange":"NSE","instrument_token":341249,"isin":"INE040A01034","product":"CNC","quantity":23,"average_price":999.65,"last_price":993.9,"close_price":999.15,"pnl":-132.25,"day_change_percentage":-0.5254466296},
    {"tradingsymbol":"ICICIBANK","exchange":"NSE","instrument_token":1270529,"isin":"INE090A01021","product":"CNC","quantity":31,"average_price":1378.064516,"last_price":1364.2,"close_price":1368.4,"pnl":-429.80,"day_change_percentage":-0.3069277989},
    {"tradingsymbol":"IDBI","exchange":"NSE","instrument_token":377857,"isin":"INE008A01015","product":"CNC","quantity":409,"average_price":100.384352,"last_price":100.52,"close_price":98.93,"pnl":55.480032,"day_change_percentage":1.607197008},
    {"tradingsymbol":"INDIANB","exchange":"NSE","instrument_token":3663105,"isin":"INE562A01011","product":"CNC","quantity":42,"average_price":773.385714,"last_price":862.6,"close_price":854.75,"pnl":3747.000012,"day_change_percentage":0.9183971922},
    {"tradingsymbol":"INDUSTOWER","exchange":"NSE","instrument_token":7458561,"isin":"INE121J01017","product":"CNC","quantity":86,"average_price":376.6,"last_price":400.8,"close_price":400.1,"pnl":2081.2,"day_change_percentage":0.1749562609},
    {"tradingsymbol":"KARURVYSYA","exchange":"BSE","instrument_token":151040772,"isin":"INE036D01028","product":"CNC","quantity":183,"average_price":241.309071,"last_price":246.05,"close_price":243.95,"pnl":867.590007,"day_change_percentage":0.8608321377},
    {"tradingsymbol":"LICI","exchange":"NSE","instrument_token":2426881,"isin":"INE0J1Y01017","product":"CNC","quantity":18,"average_price":916,"last_price":896.5,"close_price":895.05,"pnl":-351,"day_change_percentage":0.1620021228},
    {"tradingsymbol":"MAHABANK","exchange":"BSE","instrument_token":136326404,"isin":"INE457A01014","product":"CNC","quantity":854,"average_price":54.875409,"last_price":59.05,"close_price":58.25,"pnl":3565.100714,"day_change_percentage":1.373390558},
    {"tradingsymbol":"MAHSEAMLES","exchange":"NSE","instrument_token":534529,"isin":"INE271B01025","product":"CNC","quantity":28,"average_price":565,"last_price":564.05,"close_price":571.05,"pnl":-26.6,"day_change_percentage":-1.225812101},
    {"tradingsymbol":"MUTHOOTFIN","exchange":"NSE","instrument_token":6054401,"isin":"INE414G01012","product":"CNC","quantity":3,"average_price":3384.1,"last_price":3676.9,"close_price":3614.4,"pnl":878.4,"day_change_percentage":1.729194334},
    {"tradingsymbol":"NATIONALUM","exchange":"NSE","instrument_token":1629185,"isin":"INE139A01034","product":"CNC","quantity":164,"average_price":263.359268,"last_price":253.04,"close_price":251.06,"pnl":-1692.36,"day_change_percentage":0.7886560981},
    {"tradingsymbol":"PNB","exchange":"NSE","instrument_token":2730497,"isin":"INE160A01022","product":"CNC","quantity":345,"average_price":107.116231,"last_price":122.44,"close_price":121.75,"pnl":5286.700305,"day_change_percentage":0.5667351129},
    {"tradingsymbol":"SBIN","exchange":"NSE","instrument_token":779521,"isin":"INE062A01020","product":"CNC","quantity":42,"average_price":852.085714,"last_price":982.9,"close_price":970.6,"pnl":5494.200012,"day_change_percentage":1.267257367},
    {"tradingsymbol":"UJJIVANSFB","exchange":"BSE","instrument_token":138983428,"isin":"INE551W01018","product":"CNC","quantity":874,"average_price":48.767643,"last_price":53.4,"close_price":53.84,"pnl":4048.680018,"day_change_percentage":-0.8172362556},
    {"tradingsymbol":"UNIONBANK","exchange":"NSE","instrument_token":2752769,"isin":"INE692A01016","product":"CNC","quantity":309,"average_price":145.751747,"last_price":151.98,"close_price":150.99,"pnl":1924.530177,"day_change_percentage":0.6556725611}
]

print("=" * 90)
print(" " * 20 + "KITE MCP LIVE PORTFOLIO ANALYSIS")
print("=" * 90)
print()

# Initialize Portfolio Analyzer
print("🔧 Initializing Portfolio Analyzer...")
analyzer = PortfolioAnalyzer(available_funds=114129.60)
print()

# Load all holdings from Kite
print(f"📡 Loading {len(all_kite_holdings)} live holdings from Kite MCP...")
success = analyzer.load_from_kite_mcp_data(all_kite_holdings)

if not success:
    print("❌ Failed to load holdings")
    sys.exit(1)

print()
print("=" * 90)
print(" " * 30 + "PORTFOLIO OVERVIEW")
print("=" * 90)
print()

# Calculate summary metrics
df = analyzer.holdings_df
total_invested = df['Invested'].sum()
total_current = df['Cur. val'].sum()
total_pnl = df['P&L'].sum()
total_return_pct = (total_pnl / total_invested * 100) if total_invested > 0 else 0

profitable = df[df['P&L'] > 0]
loss_making = df[df['P&L'] < 0]

print(f"{'Total Holdings:':<30} {len(df)} stocks")
print(f"{'Total Invested:':<30} ₹{total_invested:,.2f}")
print(f"{'Current Value:':<30} ₹{total_current:,.2f}")
print(f"{'Available Cash:':<30} ₹{analyzer.available_funds:,.2f}")
print(f"{'Total Portfolio Value:':<30} ₹{total_current + analyzer.available_funds:,.2f}")
print()
print(f"{'Total P&L:':<30} ₹{total_pnl:,.2f}")
print(f"{'Overall Return:':<30} {total_return_pct:.2f}%")
print()
print(f"{'Profitable Stocks:':<30} {len(profitable)} ({len(profitable)/len(df)*100:.1f}%)")
print(f"{'Loss-Making Stocks:':<30} {len(loss_making)} ({len(loss_making)/len(df)*100:.1f}%)")
print()

# Top performers
print("=" * 90)
print(" " * 30 + "TOP 5 PERFORMERS")
print("=" * 90)
top5 = df.nlargest(5, 'Return_Pct')[['Instrument', 'Qty.', 'Return_Pct', 'P&L', 'Cur. val']]
print(f"\n{'Rank':<6} {'Stock':<15} {'Qty':<8} {'Return %':<12} {'P&L (₹)':<15} {'Value (₹)'}")
print("-" * 90)
for i, (idx, row) in enumerate(top5.iterrows(), 1):
    print(f"{i:<6} {row['Instrument']:<15} {row['Qty.']:<8.0f} {row['Return_Pct']:>10.2f}% {row['P&L']:>13,.2f} {row['Cur. val']:>12,.2f}")
print()

# Worst performers
print("=" * 90)
print(" " * 30 + "UNDERPERFORMERS")
print("=" * 90)
worst5 = df.nsmallest(5, 'Return_Pct')[['Instrument', 'Qty.', 'Return_Pct', 'P&L', 'Cur. val']]
print(f"\n{'Rank':<6} {'Stock':<15} {'Qty':<8} {'Return %':<12} {'P&L (₹)':<15} {'Value (₹)'}")
print("-" * 90)
for i, (idx, row) in enumerate(worst5.iterrows(), 1):
    print(f"{i:<6} {row['Instrument']:<15} {row['Qty.']:<8.0f} {row['Return_Pct']:>10.2f}% {row['P&L']:>13,.2f} {row['Cur. val']:>12,.2f}")
print()

# Largest holdings
print("=" * 90)
print(" " * 28 + "TOP 5 LARGEST HOLDINGS")
print("=" * 90)
largest5 = df.nlargest(5, 'Weight')[['Instrument', 'Weight', 'Cur. val', 'P&L']]
print(f"\n{'Rank':<6} {'Stock':<15} {'Weight %':<12} {'Value (₹)':<15} {'P&L (₹)'}")
print("-" * 90)
for i, (idx, row) in enumerate(largest5.iterrows(), 1):
    print(f"{i:<6} {row['Instrument']:<15} {row['Weight']:>9.2f}% {row['Cur. val']:>13,.2f} {row['P&L']:>12,.2f}")
print()

# Exchange breakdown
print("=" * 90)
print(" " * 30 + "EXCHANGE BREAKDOWN")
print("=" * 90)
exchange_summary = df.groupby('Exchange').agg({
    'Cur. val': 'sum',
    'P&L': 'sum',
    'Instrument': 'count'
}).rename(columns={'Instrument': 'Count'})

print(f"\n{'Exchange':<15} {'Stocks':<10} {'Value (₹)':<18} {'P&L (₹)'}")
print("-" * 90)
for exchange, row in exchange_summary.iterrows():
    pct = (row['Cur. val'] / total_current * 100)
    print(f"{exchange:<15} {row['Count']:<10.0f} {row['Cur. val']:>15,.2f} ({pct:>5.1f}%) {row['P&L']:>12,.2f}")
print()

# Summary stats
print("=" * 90)
print(" " * 30 + "STATISTICAL SUMMARY")
print("=" * 90)
print(f"\n{'Metric':<30} {'Value'}")
print("-" * 90)
print(f"{'Average Return per Stock:':<30} {df['Return_Pct'].mean():.2f}%")
print(f"{'Median Return:':<30} {df['Return_Pct'].median():.2f}%")
print(f"{'Best Performing Stock:':<30} {df.loc[df['Return_Pct'].idxmax(), 'Instrument']} ({df['Return_Pct'].max():.2f}%)")
print(f"{'Worst Performing Stock:':<30} {df.loc[df['Return_Pct'].idxmin(), 'Instrument']} ({df['Return_Pct'].min():.2f}%)")
print(f"{'Largest Gain:':<30} ₹{df['P&L'].max():,.2f}")
print(f"{'Largest Loss:':<30} ₹{df['P&L'].min():,.2f}")
print(f"{'Average Position Size:':<30} ₹{df['Cur. val'].mean():,.2f}")
print(f"{'Largest Position:':<30} {df.loc[df['Cur. val'].idxmax(), 'Instrument']} (₹{df['Cur. val'].max():,.2f})")
print(f"{'Smallest Position:':<30} {df.loc[df['Cur. val'].idxmin(), 'Instrument']} (₹{df['Cur. val'].min():,.2f})")
print()

print("=" * 90)
print(" " * 35 + "COMPLETE ✅")
print("=" * 90)
print()
print("💡 Next Steps:")
print("   1. Enable Kite MCP in portfolio_config.py: DATA_SOURCE = 'kite_mcp'")
print("   2. Your holdings will automatically sync from Kite instead of CSV")
print("   3. Run your existing analysis scripts - they'll work with live data!")
print()
