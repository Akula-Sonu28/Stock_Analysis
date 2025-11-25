#!/usr/bin/env python3
"""
Interactive Kite MCP Setup Wizard
Guides you through configuring Kite MCP integration
"""

import os
import sys
from pathlib import Path

class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    """Print a styled header"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 80}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(80)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 80}{Colors.END}\n")

def print_section(text):
    """Print a section header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{text}{Colors.END}")
    print(f"{Colors.BLUE}{'-' * 80}{Colors.END}")

def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_info(text):
    """Print info message"""
    print(f"{Colors.CYAN}ℹ️  {text}{Colors.END}")

def print_warning(text):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def get_input(prompt, default=None, options=None):
    """Get user input with optional default and validation"""
    if default:
        prompt = f"{prompt} [{Colors.GREEN}{default}{Colors.END}]: "
    else:
        prompt = f"{prompt}: "
    
    while True:
        response = input(prompt).strip()
        
        # Use default if empty
        if not response and default:
            return default
        
        # Validate options if provided
        if options:
            if response.lower() in [opt.lower() for opt in options]:
                return response.lower()
            else:
                print_error(f"Please choose from: {', '.join(options)}")
                continue
        
        if response:
            return response
        else:
            print_error("This field is required. Please enter a value.")

def get_yes_no(prompt, default="yes"):
    """Get yes/no input"""
    response = get_input(f"{prompt} (yes/no)", default, ["yes", "no", "y", "n"])
    return response in ["yes", "y"]

def main():
    """Run the interactive setup wizard"""
    
    print_header("KITE MCP INTEGRATION SETUP WIZARD")
    
    print(f"{Colors.BOLD}Welcome to the Kite MCP Integration Setup!{Colors.END}")
    print("\nThis wizard will help you configure your stock analysis system to fetch")
    print("live holdings from Kite instead of manual CSV imports.")
    print()
    
    # Step 1: Explain what we'll configure
    print_section("📋 What We'll Configure")
    print("1. Data source selection (CSV, Kite MCP, or Auto)")
    print("2. Kite MCP enablement")
    print("3. Cache settings")
    print("4. Fallback behavior")
    print("5. Available funds for analysis")
    print()
    
    input(f"{Colors.YELLOW}Press ENTER to continue...{Colors.END}")
    
    # Step 2: Data Source Selection
    print_section("🔌 Data Source Configuration")
    print("\nChoose how you want to load your portfolio holdings:")
    print()
    print(f"{Colors.BOLD}1. CSV{Colors.END} - Use traditional CSV files from Zerodha exports")
    print("   • Manual export required")
    print("   • Works offline")
    print("   • No API dependencies")
    print()
    print(f"{Colors.BOLD}2. Kite MCP{Colors.END} - Fetch live data from your Kite account")
    print("   • Automatic sync")
    print("   • Always current")
    print("   • Requires MCP environment")
    print()
    print(f"{Colors.BOLD}3. Auto{Colors.END} - Try Kite MCP first, fallback to CSV if unavailable")
    print("   • Best of both worlds")
    print("   • Recommended option")
    print("   • Seamless experience")
    print()
    
    data_source = get_input(
        "Select data source (1-3 or csv/kite_mcp/auto)",
        default="auto"
    )
    
    # Map numeric choices
    source_map = {"1": "csv", "2": "kite_mcp", "3": "auto"}
    data_source = source_map.get(data_source, data_source)
    
    # Validate
    if data_source not in ["csv", "kite_mcp", "auto"]:
        print_warning(f"Invalid choice '{data_source}', using 'auto'")
        data_source = "auto"
    
    print_success(f"Data source set to: {data_source}")
    
    # Step 3: Kite MCP Enablement
    print_section("⚙️ Kite MCP Settings")
    
    if data_source == "csv":
        kite_enabled = False
        print_info("Kite MCP will be disabled (CSV mode selected)")
    else:
        print("\nDo you want to enable Kite MCP integration?")
        print("(This allows fetching live data from Kite)")
        kite_enabled = get_yes_no("Enable Kite MCP", default="yes")
    
    # Step 4: Cache Settings
    print_section("💾 Cache Configuration")
    print("\nKite data can be cached to reduce API calls.")
    print("Recommended: 5 minutes (balances freshness with performance)")
    print()
    
    cache_ttl = get_input(
        "Cache TTL in minutes (1-60)",
        default="5"
    )
    
    try:
        cache_ttl = int(cache_ttl)
        if cache_ttl < 1 or cache_ttl > 60:
            print_warning("Invalid TTL, using default of 5 minutes")
            cache_ttl = 5
    except ValueError:
        print_warning("Invalid number, using default of 5 minutes")
        cache_ttl = 5
    
    print_success(f"Cache TTL set to: {cache_ttl} minutes")
    
    # Step 5: Fallback Behavior
    print_section("🔄 Fallback Configuration")
    
    if data_source in ["kite_mcp", "auto"]:
        print("\nIf Kite MCP fails or is unavailable, should the system")
        print("automatically fallback to CSV files?")
        auto_fallback = get_yes_no("Enable automatic CSV fallback", default="yes")
    else:
        auto_fallback = True
        print_info("Fallback enabled by default for CSV mode")
    
    # Step 6: Available Funds
    print_section("💰 Portfolio Configuration")
    print("\nEnter your available funds for new investments.")
    print("This is used for portfolio allocation and recommendations.")
    print()
    
    available_funds = get_input(
        "Available funds (in ₹)",
        default="114129.60"
    )
    
    try:
        available_funds = float(available_funds)
        if available_funds < 0:
            print_warning("Negative funds not allowed, using 0")
            available_funds = 0
    except ValueError:
        print_warning("Invalid amount, using default")
        available_funds = 114129.60
    
    print_success(f"Available funds set to: ₹{available_funds:,.2f}")
    
    # Step 7: Summary
    print_section("📊 Configuration Summary")
    print()
    print(f"Data Source:           {Colors.BOLD}{data_source}{Colors.END}")
    print(f"Kite MCP Enabled:      {Colors.BOLD}{kite_enabled}{Colors.END}")
    print(f"Cache TTL:             {Colors.BOLD}{cache_ttl} minutes{Colors.END}")
    print(f"Auto Fallback to CSV:  {Colors.BOLD}{auto_fallback}{Colors.END}")
    print(f"Available Funds:       {Colors.BOLD}₹{available_funds:,.2f}{Colors.END}")
    print()
    
    confirm = get_yes_no("Apply this configuration", default="yes")
    
    if not confirm:
        print_warning("Configuration cancelled. No changes made.")
        return
    
    # Step 8: Apply Configuration
    print_section("💾 Applying Configuration")
    
    try:
        # Read current portfolio_config.py
        config_path = Path("portfolio_config.py")
        
        if not config_path.exists():
            print_error(f"Configuration file not found: {config_path}")
            return
        
        with open(config_path, 'r') as f:
            config_content = f.read()
        
        # Update configuration values
        import re
        
        # Update DATA_SOURCE
        config_content = re.sub(
            r'DATA_SOURCE\s*=\s*["\'].*?["\']',
            f'DATA_SOURCE = "{data_source}"',
            config_content
        )
        
        # Update KITE_MCP_ENABLED
        config_content = re.sub(
            r'KITE_MCP_ENABLED\s*=\s*(?:True|False)',
            f'KITE_MCP_ENABLED = {kite_enabled}',
            config_content
        )
        
        # Update KITE_CACHE_TTL_MINUTES
        config_content = re.sub(
            r'KITE_CACHE_TTL_MINUTES\s*=\s*\d+',
            f'KITE_CACHE_TTL_MINUTES = {cache_ttl}',
            config_content
        )
        
        # Update AUTO_FALLBACK_TO_CSV
        config_content = re.sub(
            r'AUTO_FALLBACK_TO_CSV\s*=\s*(?:True|False)',
            f'AUTO_FALLBACK_TO_CSV = {auto_fallback}',
            config_content
        )
        
        # Update DEFAULT_AVAILABLE_FUNDS
        config_content = re.sub(
            r'DEFAULT_AVAILABLE_FUNDS\s*=\s*[\d.]+',
            f'DEFAULT_AVAILABLE_FUNDS = {available_funds}',
            config_content
        )
        
        # Write updated configuration
        with open(config_path, 'w') as f:
            f.write(config_content)
        
        print_success("Configuration updated successfully!")
        
        # Create .env file if requested
        print()
        create_env = get_yes_no("Create .env file with these settings", default="no")
        
        if create_env:
            env_content = f"""# Kite MCP Configuration
# Generated by setup wizard on {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

# Data Source Selection
DATA_SOURCE={data_source}

# Enable Kite MCP Integration
KITE_MCP_ENABLED={str(kite_enabled).lower()}

# Kite MCP Cache Settings
KITE_CACHE_TTL_MINUTES={cache_ttl}

# Automatic Fallback
AUTO_FALLBACK_TO_CSV={str(auto_fallback).lower()}

# Portfolio Settings
AVAILABLE_FUNDS={available_funds}

# Logging Level (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL=INFO
"""
            with open('.env', 'w') as f:
                f.write(env_content)
            
            print_success(".env file created!")
        
    except Exception as e:
        print_error(f"Error applying configuration: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Step 9: Next Steps
    print_section("🎯 What's Next?")
    print()
    
    if data_source == "kite_mcp" and kite_enabled:
        print("✨ Kite MCP is now enabled!")
        print()
        print("To use it in an MCP environment (like this chat):")
        print()
        print(f"{Colors.CYAN}from portfolio.analyzer import PortfolioAnalyzer{Colors.END}")
        print(f"{Colors.CYAN}analyzer = PortfolioAnalyzer(){Colors.END}")
        print(f"{Colors.CYAN}analyzer.load_from_kite_mcp_data(kite_holdings){Colors.END}")
        print()
        print("The assistant will fetch your live holdings automatically!")
        
    elif data_source == "auto":
        print("✨ Auto mode is now enabled!")
        print()
        print("Your system will:")
        print("1. Try to fetch live data from Kite MCP first")
        print("2. Automatically fallback to CSV if Kite is unavailable")
        print()
        print("Just use your existing scripts normally - they'll work with both!")
        
    else:
        print("✨ CSV mode is active!")
        print()
        print("Continue using your existing workflow:")
        print("1. Export holdings CSV from Zerodha")
        print("2. Place in Holding/ directory")
        print("3. Run your analysis scripts")
    
    print()
    print("📚 Documentation:")
    print("   • Complete guide: KITE_MCP_INTEGRATION.md")
    print("   • Quick start: python quick_start_kite.py")
    print("   • Demo: python demo_kite_analysis.py")
    print()
    
    print_header("✅ SETUP COMPLETE!")
    print(f"\n{Colors.GREEN}Your Kite MCP integration is configured and ready to use!{Colors.END}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠️  Setup cancelled by user.{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}❌ Unexpected error: {e}{Colors.END}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
