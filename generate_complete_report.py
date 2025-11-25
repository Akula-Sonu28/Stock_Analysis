import pandas as pd
from datetime import datetime

# Complete holdings data from Kite
holdings_data = [
    {'symbol':'AUBANK','exchange':'NSE','qty':20,'opening_qty':28,'used_qty':8,'avg_cost':729.5,'ltp':935.85,'unrealized_pnl':4127,'day_change':10.75},
    {'symbol':'AUROPHARMA','exchange':'BSE','qty':0,'opening_qty':34,'used_qty':34,'avg_cost':1142.5,'ltp':1213.2,'unrealized_pnl':0,'day_change':18.9},
    {'symbol':'AXISBANK','exchange':'NSE','qty':28,'opening_qty':28,'used_qty':0,'avg_cost':1196.43,'ltp':1270.4,'unrealized_pnl':2071.20,'day_change':1.4},
    {'symbol':'BANKBARODA','exchange':'NSE','qty':64,'opening_qty':90,'used_qty':26,'avg_cost':232.4,'ltp':284.65,'unrealized_pnl':3344,'day_change':2.75},
    {'symbol':'BANKINDIA','exchange':'BSE','qty':113,'opening_qty':113,'used_qty':0,'avg_cost':111.89,'ltp':146.5,'unrealized_pnl':3910.93,'day_change':0.55},
    {'symbol':'CANBK','exchange':'NSE','qty':261,'opening_qty':372,'used_qty':111,'avg_cost':118.62,'ltp':147.81,'unrealized_pnl':7618.57,'day_change':1.14},
    {'symbol':'CUB','exchange':'BSE','qty':220,'opening_qty':220,'used_qty':0,'avg_cost':231.80,'ltp':277.2,'unrealized_pnl':9988.99,'day_change':5.65},
    {'symbol':'FEDERALBNK','exchange':'NSE','qty':115,'opening_qty':115,'used_qty':0,'avg_cost':221.1,'ltp':254.01,'unrealized_pnl':3784.55,'day_change':5.84},
    {'symbol':'GICRE','exchange':'BSE','qty':148,'opening_qty':148,'used_qty':0,'avg_cost':380.41,'ltp':381.2,'unrealized_pnl':117.25,'day_change':1.8},
    {'symbol':'GPPL','exchange':'NSE','qty':91,'opening_qty':91,'used_qty':0,'avg_cost':176,'ltp':180.34,'unrealized_pnl':394.94,'day_change':0.46},
    {'symbol':'HDFCBANK','exchange':'NSE','qty':23,'opening_qty':23,'used_qty':0,'avg_cost':999.65,'ltp':995.05,'unrealized_pnl':-105.8,'day_change':-4.1},
    {'symbol':'ICICIBANK','exchange':'NSE','qty':31,'opening_qty':31,'used_qty':0,'avg_cost':1378.06,'ltp':1366.5,'unrealized_pnl':-358.5,'day_change':-1.9},
    {'symbol':'IDBI','exchange':'NSE','qty':409,'opening_qty':409,'used_qty':0,'avg_cost':100.38,'ltp':101.35,'unrealized_pnl':394.95,'day_change':2.42},
    {'symbol':'INDIANB','exchange':'NSE','qty':42,'opening_qty':42,'used_qty':0,'avg_cost':773.39,'ltp':866.9,'unrealized_pnl':3927.6,'day_change':12.15},
    {'symbol':'INDUSINDBK','exchange':'NSE','qty':0,'opening_qty':32,'used_qty':32,'avg_cost':826.2,'ltp':831.35,'unrealized_pnl':0,'day_change':-4.7},
    {'symbol':'INDUSTOWER','exchange':'NSE','qty':86,'opening_qty':86,'used_qty':0,'avg_cost':376.6,'ltp':401,'unrealized_pnl':2098.4,'day_change':0.9},
    {'symbol':'KARURVYSYA','exchange':'BSE','qty':183,'opening_qty':183,'used_qty':0,'avg_cost':241.31,'ltp':248.2,'unrealized_pnl':1261.04,'day_change':4.25},
    {'symbol':'LICI','exchange':'NSE','qty':18,'opening_qty':18,'used_qty':0,'avg_cost':916,'ltp':897.25,'unrealized_pnl':-337.5,'day_change':2.2},
    {'symbol':'MAHABANK','exchange':'BSE','qty':854,'opening_qty':854,'used_qty':0,'avg_cost':54.88,'ltp':59.05,'unrealized_pnl':3565.1,'day_change':0.8},
    {'symbol':'MAHSEAMLES','exchange':'NSE','qty':28,'opening_qty':28,'used_qty':0,'avg_cost':565,'ltp':565,'unrealized_pnl':0,'day_change':-6.05},
    {'symbol':'MUTHOOTFIN','exchange':'NSE','qty':3,'opening_qty':3,'used_qty':0,'avg_cost':3384.1,'ltp':3679.4,'unrealized_pnl':885.9,'day_change':65},
    {'symbol':'NATIONALUM','exchange':'NSE','qty':164,'opening_qty':164,'used_qty':0,'avg_cost':263.36,'ltp':253.98,'unrealized_pnl':-1538.2,'day_change':2.92},
    {'symbol':'PNB','exchange':'NSE','qty':345,'opening_qty':345,'used_qty':0,'avg_cost':107.12,'ltp':122.62,'unrealized_pnl':5348.8,'day_change':0.87},
    {'symbol':'SBIN','exchange':'NSE','qty':42,'opening_qty':42,'used_qty':0,'avg_cost':852.09,'ltp':985.5,'unrealized_pnl':5603.4,'day_change':14.9},
    {'symbol':'UJJIVANSFB','exchange':'BSE','qty':874,'opening_qty':874,'used_qty':0,'avg_cost':48.77,'ltp':53.46,'unrealized_pnl':4101.12,'day_change':-0.38},
    {'symbol':'UNIONBANK','exchange':'NSE','qty':309,'opening_qty':309,'used_qty':0,'avg_cost':145.75,'ltp':151.86,'unrealized_pnl':1887.45,'day_change':0.87},
    # New buys today
    {'symbol':'ACC','exchange':'NSE','qty':10,'opening_qty':0,'used_qty':0,'avg_cost':1864,'ltp':1864.9,'unrealized_pnl':9,'day_change':0.9}
]

# Today's realized trades
trades_realized = [
    {'symbol':'INDUSINDBK','type':'SELL','qty':32,'sell_price':833.35,'buy_price':826.2,'realized_pnl':228.8},
    {'symbol':'CANBK','type':'SELL','qty':111,'sell_price':147.04,'buy_price':118.62,'realized_pnl':3154.62},
    {'symbol':'AUROPHARMA','type':'SELL','qty':34,'sell_price':1209,'buy_price':1142.5,'realized_pnl':2261},
    {'symbol':'AUBANK','type':'SELL','qty':8,'sell_price':935.9,'buy_price':729.5,'realized_pnl':1651.2},
    {'symbol':'BANKBARODA','type':'SELL','qty':26,'sell_price':284.4,'buy_price':232.4,'realized_pnl':1352}
]

# Create dataframes
df_holdings = pd.DataFrame(holdings_data)
df_trades = pd.DataFrame(trades_realized)

# Calculate current value
df_holdings['cur_val'] = df_holdings['qty'] * df_holdings['ltp']

# Prepare output CSV
output_df = pd.DataFrame({
    'Symbol': df_holdings['symbol'],
    'Instrument': df_holdings['symbol'] + ' (' + df_holdings['exchange'] + ')',
    'Qty': df_holdings['qty'],
    'Avg cost': df_holdings['avg_cost'].round(2),
    'LTP': df_holdings['ltp'].round(2),
    'Cur val': df_holdings['cur_val'].round(2),
    'P&L': df_holdings['unrealized_pnl'].round(2),
    'Day change': df_holdings['day_change'].round(2),
    'Sector': 'Banking'
})

# Save files
timestamp = datetime.now().strftime('%Y%m%d')
holdings_file = f'Holding/holdings_kite_{timestamp}.csv'
trades_file = f'Holding/trades_realized_{timestamp}.csv'

output_df.to_csv(holdings_file, index=False)
df_trades.to_csv(trades_file, index=False)

# Calculate stats
total_value = output_df['Cur val'].sum()
total_unrealized_pnl = output_df['P&L'].sum()
total_realized_pnl = df_trades['realized_pnl'].sum()
stocks_holding = len(output_df[output_df['Qty'] > 0])

total_sells = df_trades['qty'].sum() * df_trades['sell_price'].mean()
total_buys = 17794 + 24938.1 + 10984 + 18640  # From today's buys

print('=' * 80)
print(f'📊 COMPLETE KITE PORTFOLIO DATA - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
print('=' * 80)
print()
print('💼 PORTFOLIO SUMMARY:')
print(f'   Current Portfolio Value: ₹{total_value:,.2f}')
print(f'   Active Holdings: {stocks_holding} stocks')
print(f'   Unrealized P&L: ₹{total_unrealized_pnl:,.2f}')
print(f'   Realized P&L (Today): ₹{total_realized_pnl:,.2f}')
print(f'   Total P&L: ₹{(total_unrealized_pnl + total_realized_pnl):,.2f}')
print()
print('📈 TODAY\'S TRADING ACTIVITY:')
print(f'   Total Sells Value: ₹1,13,571.16')
print(f'   Total Buys Value: ₹72,356.10')
print(f'   Net Cash Inflow: ₹41,215.06')
print()
print('💰 ACCOUNT STATUS:')
print(f'   Cash Available: ₹94,080')
print(f'   Live Balance: ₹1,20,700.14')
print()
print('🏆 TOP 5 WINNERS (Unrealized):')
top_winners = output_df[output_df['Qty'] > 0].nlargest(5, 'P&L')[['Symbol', 'Qty', 'P&L']]
for idx, row in top_winners.iterrows():
    print(f'   {row["Symbol"]:12} - {int(row["Qty"]):3} shares @ ₹{row["P&L"]:8.2f}')
print()
print('⚠️  TOP 5 LOSERS (Unrealized):')
top_losers = output_df[output_df['Qty'] > 0].nsmallest(5, 'P&L')[['Symbol', 'Qty', 'P&L']]
for idx, row in top_losers.iterrows():
    print(f'   {row["Symbol"]:12} - {int(row["Qty"]):3} shares @ ₹{row["P&L"]:8.2f}')
print()
print('💵 TODAY\'S REALIZED GAINS:')
for idx, row in df_trades.iterrows():
    print(f'   {row["symbol"]:12} - Sold {int(row["qty"]):3} @ ₹{row["sell_price"]:7.2f} = +₹{row["realized_pnl"]:8.2f}')
print()
print('=' * 80)
print(f'✅ Holdings saved to: {holdings_file}')
print(f'✅ Trades saved to: {trades_file}')
print('=' * 80)
