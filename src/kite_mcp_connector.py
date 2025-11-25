"""
Kite MCP Connector - Fetches live holdings from Kite using MCP tools
"""
import pandas as pd
import logging
from typing import Dict, List, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class KiteMCPConnector:
    """
    Connector to fetch live holdings and positions from Kite via MCP tools.
    Uses the available MCP tools instead of direct API calls.
    """
    
    def __init__(self):
        """Initialize the Kite MCP connector"""
        self.logger = logging.getLogger(__name__)
        self.last_fetch_time = None
        self._holdings_cache = None
        self._positions_cache = None
    
    def fetch_holdings(self, use_cache: bool = False, cache_ttl_minutes: int = 5) -> pd.DataFrame:
        """
        Fetch current holdings from Kite via MCP and transform to internal format.
        
        Args:
            use_cache: Whether to use cached data if available
            cache_ttl_minutes: Cache time-to-live in minutes
            
        Returns:
            DataFrame with holdings in internal format matching CSV structure
        """
        try:
            # Check cache if enabled
            if use_cache and self._is_cache_valid(cache_ttl_minutes):
                self.logger.info("Using cached holdings data")
                return self._holdings_cache.copy()
            
            self.logger.info("Fetching live holdings from Kite MCP...")
            
            # Note: Actual MCP call happens in the portfolio analyzer
            # This method is called by the analyzer which has access to MCP tools
            # This is a placeholder for the transformation logic
            
            raise NotImplementedError(
                "This method should be called from portfolio analyzer with MCP tool results"
            )
            
        except Exception as e:
            self.logger.error(f"Error fetching holdings from Kite MCP: {e}")
            raise
    
    def transform_kite_holdings(self, kite_holdings: List[Dict]) -> pd.DataFrame:
        """
        Transform Kite MCP holdings format to internal DataFrame format.
        
        Args:
            kite_holdings: List of holdings from mcp_kite_get_holdings
            
        Returns:
            DataFrame matching the internal format (Instrument, Qty., Avg. cost, etc.)
        """
        try:
            if not kite_holdings:
                self.logger.warning("No holdings returned from Kite")
                return pd.DataFrame()
            
            transformed_data = []
            
            for holding in kite_holdings:
                # Only process holdings with actual quantity
                if holding.get('quantity', 0) <= 0:
                    continue
                
                # Calculate values
                quantity = holding['quantity']
                avg_price = holding['average_price']
                last_price = holding['last_price']
                invested = quantity * avg_price
                current_value = quantity * last_price
                pnl = holding.get('pnl', current_value - invested)
                net_change_pct = ((last_price - avg_price) / avg_price * 100) if avg_price > 0 else 0
                day_change_pct = holding.get('day_change_percentage', 0)
                
                # Transform to internal format matching CSV structure
                transformed_data.append({
                    'Instrument': holding['tradingsymbol'],
                    'Qty.': quantity,
                    'Avg. cost': avg_price,
                    'LTP': last_price,
                    'Invested': invested,
                    'Cur. val': current_value,
                    'P&L': pnl,
                    'Net chg.': net_change_pct,
                    'Day chg.': day_change_pct,
                    # Additional metadata
                    'Exchange': holding.get('exchange', 'NSE'),
                    'ISIN': holding.get('isin', ''),
                    'Product': holding.get('product', 'CNC'),
                    'Close Price': holding.get('close_price', last_price)
                })
            
            df = pd.DataFrame(transformed_data)
            
            # Calculate portfolio weights
            if not df.empty and 'Cur. val' in df.columns:
                total_value = df['Cur. val'].sum()
                if total_value > 0:
                    df['Weight'] = (df['Cur. val'] / total_value * 100).round(2)
                else:
                    df['Weight'] = 0
            
            # Calculate return percentage
            if not df.empty:
                df['Return_Pct'] = df['Net chg.'].round(2)
            
            self.logger.info(f"Transformed {len(df)} holdings from Kite MCP format")
            
            # Update cache
            self._holdings_cache = df.copy()
            self.last_fetch_time = datetime.now()
            
            return df
            
        except Exception as e:
            self.logger.error(f"Error transforming Kite holdings: {e}")
            raise
    
    def fetch_positions(self) -> pd.DataFrame:
        """
        Fetch current positions from Kite via MCP.
        
        Returns:
            DataFrame with positions data
        """
        try:
            self.logger.info("Fetching live positions from Kite MCP...")
            
            # Note: Actual MCP call happens in the calling context
            # This is a placeholder for the transformation logic
            
            raise NotImplementedError(
                "This method should be called with MCP tool results"
            )
            
        except Exception as e:
            self.logger.error(f"Error fetching positions from Kite MCP: {e}")
            raise
    
    def transform_kite_positions(self, kite_positions: Dict) -> pd.DataFrame:
        """
        Transform Kite MCP positions format to internal DataFrame format.
        
        Args:
            kite_positions: Positions data from mcp_kite_get_positions
            
        Returns:
            DataFrame with positions data
        """
        try:
            # Positions have 'net' and 'day' sub-arrays
            net_positions = kite_positions.get('net', [])
            day_positions = kite_positions.get('day', [])
            
            # Focus on net positions for portfolio analysis
            if not net_positions:
                self.logger.warning("No net positions found")
                return pd.DataFrame()
            
            transformed_data = []
            
            for position in net_positions:
                if position.get('quantity', 0) == 0:
                    continue
                
                transformed_data.append({
                    'Instrument': position['tradingsymbol'],
                    'Product': position.get('product', ''),
                    'Quantity': position['quantity'],
                    'Avg. Price': position.get('average_price', 0),
                    'LTP': position.get('last_price', 0),
                    'P&L': position.get('pnl', 0),
                    'Day P&L': position.get('day_pnl', 0),
                    'Exchange': position.get('exchange', ''),
                    'Instrument Token': position.get('instrument_token', 0)
                })
            
            df = pd.DataFrame(transformed_data)
            
            self.logger.info(f"Transformed {len(df)} positions from Kite MCP format")
            
            # Update cache
            self._positions_cache = df.copy()
            
            return df
            
        except Exception as e:
            self.logger.error(f"Error transforming Kite positions: {e}")
            raise
    
    def get_holdings_summary(self, holdings_df: pd.DataFrame) -> Dict:
        """
        Generate summary statistics from holdings DataFrame.
        
        Args:
            holdings_df: Holdings DataFrame
            
        Returns:
            Dictionary with summary statistics
        """
        if holdings_df.empty:
            return {
                'total_stocks': 0,
                'total_invested': 0,
                'total_current_value': 0,
                'total_pnl': 0,
                'total_return_pct': 0,
                'profitable_stocks': 0,
                'loss_making_stocks': 0
            }
        
        return {
            'total_stocks': len(holdings_df),
            'total_invested': holdings_df['Invested'].sum(),
            'total_current_value': holdings_df['Cur. val'].sum(),
            'total_pnl': holdings_df['P&L'].sum(),
            'total_return_pct': (holdings_df['P&L'].sum() / holdings_df['Invested'].sum() * 100) 
                               if holdings_df['Invested'].sum() > 0 else 0,
            'profitable_stocks': len(holdings_df[holdings_df['P&L'] > 0]),
            'loss_making_stocks': len(holdings_df[holdings_df['P&L'] < 0]),
            'max_gain': holdings_df['P&L'].max() if not holdings_df.empty else 0,
            'max_loss': holdings_df['P&L'].min() if not holdings_df.empty else 0,
            'avg_return_pct': holdings_df['Return_Pct'].mean() if not holdings_df.empty else 0
        }
    
    def _is_cache_valid(self, ttl_minutes: int) -> bool:
        """
        Check if cached data is still valid.
        
        Args:
            ttl_minutes: Time-to-live in minutes
            
        Returns:
            True if cache is valid, False otherwise
        """
        if self._holdings_cache is None or self.last_fetch_time is None:
            return False
        
        elapsed = (datetime.now() - self.last_fetch_time).total_seconds() / 60
        return elapsed < ttl_minutes
    
    def clear_cache(self):
        """Clear cached holdings and positions data"""
        self._holdings_cache = None
        self._positions_cache = None
        self.last_fetch_time = None
        self.logger.info("Cache cleared")


# Convenience function for quick access
def get_live_holdings_from_kite(kite_holdings_response: List[Dict]) -> pd.DataFrame:
    """
    Convenience function to quickly transform Kite holdings.
    
    Args:
        kite_holdings_response: Raw holdings from mcp_kite_get_holdings
        
    Returns:
        Transformed DataFrame
    """
    connector = KiteMCPConnector()
    return connector.transform_kite_holdings(kite_holdings_response)
