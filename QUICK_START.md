# 🚀 Quick Start Guide - Kite MCP Stock Analysis

## ✨ **Easiest Method (Recommended)**

Just tell your **Copilot assistant**:

```
"Fetch my Kite holdings and analyze"
```

That's it! Copilot will:
1. ✅ Fetch your live holdings from Kite
2. ✅ Save them to CSV
3. ✅ Run comprehensive analysis
4. ✅ Generate recommendations & reports

---

## 💻 **Manual Methods**

### **Option 1: Interactive Script**

```powershell
python run_kite_analysis.py
```

This script will:
- Check for existing holdings
- Prompt for investment amount
- Run the analysis automatically

---

### **Option 2: Direct Command**

```powershell
# If you already have holdings CSV
python analyze_top200_stocks_enhanced.py --data-source csv --portfolio-amount 94080 -n 10
```

**Parameters:**
- `--data-source csv` - Use CSV holdings file
- `--portfolio-amount 94080` - Available funds (change as needed)
- `-n 10` - Number of stocks to analyze (0 = all)

---

### **Option 3: Fetch Fresh Holdings First**

**Step 1:** Ask Copilot:
```
"Fetch my Kite holdings"
```

**Step 2:** Run analysis:
```powershell
python analyze_top200_stocks_enhanced.py --data-source csv --portfolio-amount 94080 -n 10
```

---

## 📊 **What Gets Generated**

After each run, you'll get:

1. **📈 Excel Report** - `reports/Enhanced_Stock_Report_YYYYMMDD_HHMMSS.xlsx`
   - Complete stock analysis
   - Recommendations
   - Risk metrics
   - Technical indicators

2. **🌐 Dashboard** - `Portfolio_Allocation_Dashboard.html`
   - Interactive charts
   - Buy/Sell actions
   - Portfolio allocation

3. **📋 Comparison Report** - `Stock_Comparison_Report_YYYYMMDD_HHMMSS.xlsx`
   - Changes from previous run
   - Performance tracking

4. **💾 Holdings CSV** - `Holding/holdings_kite_YYYYMMDD.csv`
   - Your current portfolio snapshot

---

## ⚙️ **Advanced Options**

### Risk Profile
```powershell
# Conservative (more defensive stocks)
python analyze_top200_stocks_enhanced.py --risk-profile conservative

# Aggressive (higher risk/reward)
python analyze_top200_stocks_enhanced.py --risk-profile aggressive
```

### Focus on Growth
```powershell
python analyze_top200_stocks_enhanced.py --focus-growth
```

### Focus on Momentum
```powershell
python analyze_top200_stocks_enhanced.py --focus-momentum
```

### Skip Risk Analysis (Faster)
```powershell
python analyze_top200_stocks_enhanced.py --skip-risk
```

### Only Undervalued Stocks
```powershell
python analyze_top200_stocks_enhanced.py --undervalued-only
```

---

## 🔄 **Daily Workflow**

### **Morning Routine:**
1. Open VS Code
2. Tell Copilot: **"Fetch my Kite holdings and analyze"**
3. Review the generated reports
4. Execute trades based on recommendations

### **Alternative:**
```powershell
python run_kite_analysis.py
```

---

## 📝 **Configuration**

Your settings are stored in:
- `portfolio_config.py` - Portfolio settings
- `config.py` - General settings

To modify settings:
```powershell
python setup_kite_mcp.py
```

---

## 💡 **Tips**

1. **Fresh Data**: Fetch holdings before market hours for best results
2. **Regular Updates**: Run analysis daily or weekly
3. **Compare Reports**: Use comparison reports to track changes
4. **Dashboard**: Keep the HTML dashboard open for quick reference

---

## 🆘 **Troubleshooting**

### "No holdings file found"
```powershell
# Ask Copilot:
"Fetch my Kite holdings"
```

### "Kite MCP not enabled"
```powershell
python setup_kite_mcp.py
```

### Need help?
Just ask your Copilot assistant for assistance!

---

## 📚 **Learn More**

- `KITE_MCP_INTEGRATION.md` - Full integration guide
- `README.md` - Project overview
- `KITE_INTEGRATION_SUMMARY.md` - Integration summary

---

**Happy Investing! 📈💰**
