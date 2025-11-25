#!/usr/bin/env python3
"""Test Kite MCP Connector Transformation"""

import sys
sys.path.insert(0, '.')

from src.kite_mcp_connector import KiteMCPConnector

# Sample Kite holdings data (first few from actual holdings)
kite_data = [
    {
        'tradingsymbol': 'SBIN',
        'exchange': 'NSE',
        'quantity': 42,
        'average_price': 852.085714,
        'last_price': 982.9,
        'close_price': 970.6,
        'pnl': 5494.200012,
        'day_change_percentage': 1.26725737,
        'isin': 'INE062A01020',
        'product': 'CNC'
    },
    {
        'tradingsymbol': 'CANBK',
        'exchange': 'NSE',
        'quantity': 261,
        'average_price': 118.62008,
        'last_price': 147.14,
        'close_price': 146.67,
        'pnl': 7443.69912,
        'day_change_percentage': 0.32044726,
        'isin': 'INE476A01022',
        'product': 'CNC'
    },
    {
        'tradingsymbol': 'PNB',
        'exchange': 'NSE',
        'quantity': 345,
        'average_price': 107.116231,
        'last_price': 122.44,
        'close_price': 121.75,
        'pnl': 5286.700305,
        'day_change_percentage': 0.56673511,
        'isin': 'INE160A01022',
        'product': 'CNC'
    }
]

# Test transformation
print("=" * 80)
print("KITE MCP CONNECTOR TEST")
print("=" * 80)
print()

connector = KiteMCPConnector()
df = connector.transform_kite_holdings(kite_data)

print(f"✅ Holdings transformed: {len(df)} stocks")
print()
print("DataFrame columns:", df.columns.tolist())
print()
print("Sample data:")
print(df[['Instrument', 'Qty.', 'Avg. cost', 'LTP', 'P&L', 'Return_Pct', 'Weight']].to_string())
print()

summary = connector.get_holdings_summary(df)
print("💰 Portfolio Summary:")
print(f"   Total Invested: Rs {summary['total_invested']:,.2f}")
print(f"   Current Value: Rs {summary['total_current_value']:,.2f}")
print(f"   Total P&L: Rs {summary['total_pnl']:,.2f}")
print(f"   Return: {summary['total_return_pct']:.2f}%")
print(f"   Profitable Stocks: {summary['profitable_stocks']}/{summary['total_stocks']}")
print()
print("=" * 80)
