import json
import pandas as pd
from datetime import datetime

# Load booking history
with open('data/booking_history.json', 'r') as f:
    booking_history = json.load(f)

# Today's realized trades
todays_trades = [
    {'symbol':'INDUSINDBK','qty':32,'sell_price':833.35,'buy_price':826.2},
    {'symbol':'CANBK','qty':111,'sell_price':147.04,'buy_price':118.62},
    {'symbol':'AUROPHARMA','qty':34,'sell_price':1209,'buy_price':1142.5},
    {'symbol':'AUBANK','qty':8,'sell_price':935.9,'buy_price':729.5},
    {'symbol':'BANKBARODA','qty':26,'sell_price':284.4,'buy_price':232.4}
]

print('=' * 90)
print('💰 COMPLETE REALIZED PROFIT HISTORY')
print('=' * 90)
print()

# Calculate past realized profits from booking history
total_past_realized = 0
past_trades = []

for symbol, data in booking_history.items():
    if data['total_booked_qty'] > 0:
        qty_booked = data['total_booked_qty']
        buy_price = data['original_price']
        
        # Estimate based on 25% profit booking (conservative estimate)
        estimated_profit_pct = 0.25
        estimated_sell_price = buy_price * (1 + estimated_profit_pct)
        
        realized_pnl = (estimated_sell_price - buy_price) * qty_booked
        total_past_realized += realized_pnl
        
        past_trades.append({
            'Symbol': symbol,
            'Qty Sold': qty_booked,
            'Buy Price': f'Rs.{buy_price:.2f}',
            'Est. Sell': f'Rs.{estimated_sell_price:.2f}',
            'Est. Profit': f'Rs.{realized_pnl:,.2f}'
        })

print('📊 PAST REALIZED PROFITS (From Booking History):')
print()
if past_trades:
    df_past = pd.DataFrame(past_trades)
    print(df_past.to_string(index=False))
    print()
    print(f'   Estimated Total Past Realized: Rs.{total_past_realized:,.2f}')
else:
    print('   No past booking history found')
print()
print('-' * 90)
print()

# Today's realized profits
total_today_realized = 0
today_details = []

print("💵 TODAY'S REALIZED PROFITS (Confirmed):")
print()
for trade in todays_trades:
    pnl = (trade['sell_price'] - trade['buy_price']) * trade['qty']
    total_today_realized += pnl
    today_details.append({
        'Symbol': trade['symbol'],
        'Qty': trade['qty'],
        'Buy Price': f"Rs.{trade['buy_price']:.2f}",
        'Sell Price': f"Rs.{trade['sell_price']:.2f}",
        'Profit': f'Rs.{pnl:,.2f}'
    })

df_today = pd.DataFrame(today_details)
print(df_today.to_string(index=False))
print()
print(f"   Total Realized Today: Rs.{total_today_realized:,.2f}")
print()
print('=' * 90)
print()

# Grand total
grand_total_realized = total_past_realized + total_today_realized

print('📈 SUMMARY:')
print()
print(f'   Past Realized Profits (Estimated):  Rs.{total_past_realized:,.2f}')
print(f"   Today's Realized Profits:           Rs.{total_today_realized:,.2f}")
print(f'   ─────────────────────────────────────────────────')
print(f'   TOTAL REALIZED PROFIT:              Rs.{grand_total_realized:,.2f}')
print()
print('=' * 90)
print()
print('📝 Notes:')
print('   • Past profits are estimated (25% avg profit booking assumption)')
print("   • Today's profits are actual realized gains from confirmed trades")
print('   • For exact past profits, download complete trade history from Kite')
print()

# Save detailed report
report_data = {
    'past_trades': past_trades,
    'today_trades': today_details,
    'summary': {
        'past_realized_estimated': total_past_realized,
        'today_realized': total_today_realized,
        'total_realized': grand_total_realized,
        'generated_on': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
}

with open('reports/realized_profit_history.json', 'w') as f:
    json.dump(report_data, f, indent=2)

print(f'✅ Detailed report saved to: reports/realized_profit_history.json')
