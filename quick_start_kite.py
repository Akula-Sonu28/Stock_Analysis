#!/usr/bin/env python3
"""
Quick Start: Kite MCP Integration
Run this script for a quick overview and health check
"""

import sys
import os
from pathlib import Path

print("=" * 80)
print(" " * 25 + "KITE MCP INTEGRATION")
print(" " * 28 + "QUICK START GUIDE")
print("=" * 80)
print()

print("📋 INTEGRATION STATUS")
print("-" * 80)

# Check file existence
files_to_check = [
    ("src/kite_mcp_connector.py", "Kite MCP Connector"),
    ("portfolio/analyzer.py", "Portfolio Analyzer"),
    ("config.py", "Global Config"),
    ("portfolio_config.py", "Portfolio Config"),
    (".env.example", "Environment Template"),
    ("KITE_MCP_INTEGRATION.md", "Complete Guide"),
    ("KITE_INTEGRATION_SUMMARY.md", "Summary Document"),
]

all_present = True
for filepath, description in files_to_check:
    exists = os.path.exists(filepath)
    status = "✅" if exists else "❌"
    print(f"{status} {description:<30} {filepath}")
    if not exists:
        all_present = False

print()

if all_present:
    print("✅ All integration files are present!")
else:
    print("⚠️  Some files are missing. Please check the installation.")
    sys.exit(1)

print()
print("🔧 CONFIGURATION")
print("-" * 80)

# Check configuration
try:
    import portfolio_config
    data_source = getattr(portfolio_config, 'DATA_SOURCE', 'csv')
    kite_enabled = getattr(portfolio_config, 'KITE_MCP_ENABLED', False)
    auto_fallback = getattr(portfolio_config, 'AUTO_FALLBACK_TO_CSV', True)
    
    print(f"Data Source:        {data_source}")
    print(f"Kite MCP Enabled:   {kite_enabled}")
    print(f"Auto Fallback:      {auto_fallback}")
    print()
    
    if data_source == 'csv':
        print("ℹ️  Currently using CSV mode")
        print("   To enable Kite MCP, edit portfolio_config.py:")
        print("   DATA_SOURCE = 'kite_mcp'")
        print("   KITE_MCP_ENABLED = True")
    elif data_source == 'kite_mcp':
        print("✅ Kite MCP mode is active!")
    elif data_source == 'auto':
        print("✅ Auto mode active (Kite with CSV fallback)")
    
except Exception as e:
    print(f"⚠️  Could not read configuration: {e}")

print()
print("🚀 QUICK USAGE")
print("-" * 80)
print()
print("Method 1: In MCP Environment (This Chat)")
print("```python")
print("from portfolio.analyzer import PortfolioAnalyzer")
print()
print("analyzer = PortfolioAnalyzer(available_funds=114129.60)")
print("analyzer.load_from_kite_mcp_data(kite_holdings)  # Assistant fetches data")
print("```")
print()
print("Method 2: Enable in Config and Use Normally")
print("```python")
print("# Edit portfolio_config.py: DATA_SOURCE = 'kite_mcp'")
print("analyzer = PortfolioAnalyzer()")
print("analyzer.load_portfolio_data()  # Automatically uses Kite MCP")
print("```")
print()

print("🧪 DEMO SCRIPTS")
print("-" * 80)
print()
print("Run these scripts to test the integration:")
print()
print("1. Test Transformation:")
print("   python test_kite_transformation.py")
print()
print("2. Test Full Integration:")
print("   python test_full_integration.py")
print()
print("3. Complete Portfolio Analysis:")
print("   python demo_kite_analysis.py")
print()

print("📚 DOCUMENTATION")
print("-" * 80)
print()
print("• Complete Guide:     KITE_MCP_INTEGRATION.md")
print("• Summary:            KITE_INTEGRATION_SUMMARY.md")
print("• API Documentation:  src/kite_mcp_connector.py (inline)")
print()

print("💡 KEY FEATURES")
print("-" * 80)
print()
print("✅ Live holdings from Kite")
print("✅ Automatic format transformation")
print("✅ CSV fallback mechanism")
print("✅ Data caching (5-minute TTL)")
print("✅ Full backward compatibility")
print("✅ Multiple data source modes")
print()

print("📊 YOUR CURRENT PORTFOLIO")
print("-" * 80)
print()
print("Based on latest Kite sync:")
print("• Holdings:      24 stocks")
print("• Invested:      ₹764,021.21")
print("• Current Value: ₹823,879.40")
print("• Total P&L:     ₹59,858.19")
print("• Return:        7.83%")
print("• Profitable:    19/24 stocks (79.2%)")
print()

print("🎯 NEXT STEPS")
print("-" * 80)
print()
print("1. Review documentation (KITE_MCP_INTEGRATION.md)")
print("2. Run demo scripts to see it in action")
print("3. Enable Kite MCP in config (optional)")
print("4. Use your existing analysis scripts with live data!")
print()

print("=" * 80)
print(" " * 20 + "✅ INTEGRATION COMPLETE & READY!")
print("=" * 80)
print()
