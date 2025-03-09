'''
CU Quants Club - Weekly Coding Challenge
----------------------------------------

Project: Basic Stock Returns and Risk Analysis
Time: ~20 minutes

Background:
Understanding risk and return is fundamental to quantitative finance. This challenge
focuses on calculating basic statistics on stock price data that are commonly used
in investment analysis.

Task:
1. Complete the function to calculate daily returns from stock prices
2. Implement the Sharpe ratio calculation
3. Find the best stock to invest in based on the highest Sharpe ratio
4. Generate the exact expected output shown at the bottom of this file

Requirements:
- Use only NumPy and Pandas libraries
- All data is provided in the template (no external data fetching required)
- Follow the instructions in each TODO comment

Evaluation Criteria:
- Correctness of calculations
- Matching the expected output exactly
- Code clarity and organization
'''

import numpy as np
import pandas as pd

# Sample stock price data (preset to avoid requiring external libraries)
# This represents closing prices for 5 stocks over 20 trading days
sample_data = {
    'AAPL': [150.25, 152.30, 151.15, 153.70, 155.25, 154.90, 152.80, 153.50, 155.75, 156.80,
             157.30, 156.25, 158.40, 157.90, 159.20, 161.40, 160.75, 159.30, 162.50, 163.75],
    'MSFT': [290.10, 293.50, 295.20, 292.80, 290.40, 294.60, 297.30, 296.50, 298.70, 301.20,
             299.80, 302.40, 304.60, 303.90, 306.20, 308.40, 307.90, 310.20, 312.50, 315.80],
    'GOOG': [2680.30, 2695.40, 2710.20, 2705.80, 2720.50, 2715.30, 2730.80, 2725.40, 2740.60, 2755.30,
             2750.90, 2770.40, 2765.80, 2780.20, 2795.40, 2790.80, 2805.30, 2820.60, 2815.90, 2830.40],
    'AMZN': [3380.20, 3395.60, 3410.80, 3405.30, 3420.70, 3415.40, 3430.90, 3425.50, 3440.80, 3455.40,
             3450.90, 3470.30, 3465.80, 3480.20, 3495.40, 3490.80, 3505.30, 3520.60, 3515.90, 3530.40],
    'TSLA': [710.20, 725.60, 715.30, 730.80, 720.40, 735.90, 725.50, 740.30, 730.90, 745.60,
             735.20, 750.80, 740.40, 755.90, 745.50, 760.30, 750.90, 765.60, 755.20, 770.80]
}

# Risk-free rate for Sharpe ratio calculation (annual)
risk_free_rate = 0.02  # 2%

def calculate_daily_returns(prices_dict):
    """
    Calculate daily percentage returns for each stock.
    
    Parameters:
    prices_dict (dict): Dictionary with stock symbols as keys and lists of prices as values
    
    Returns:
    pandas.DataFrame: DataFrame containing daily returns for each stock
    """
    # TODO: Convert the dictionary of price lists to a DataFrame
    prices_df = None  # Replace with your code
    
    # TODO: Calculate daily percentage returns for each stock
    # Hint: Use pct_change() and drop the first row which will contain NaN values
    returns_df = None  # Replace with your code
    
    return returns_df

def calculate_statistics(returns_df):
    """
    Calculate key statistics for each stock.
    
    Parameters:
    returns_df (pandas.DataFrame): DataFrame containing daily returns
    
    Returns:
    pandas.DataFrame: DataFrame containing statistics for each stock
    """
    # TODO: Calculate the following statistics for each stock:
    # 1. Average daily return
    # 2. Standard deviation of daily returns (risk)
    # 3. Annualized return (assuming 252 trading days in a year)
    # 4. Annualized risk
    # 5. Sharpe ratio: (Annualized return - risk_free_rate) / Annualized risk
    
    # Your code here
    stats = pd.DataFrame(index=returns_df.columns)
    
    # Calculate average daily return for each stock
    stats['Avg Daily Return'] = None  # Replace with your code
    
    # Calculate daily risk (standard deviation) for each stock
    stats['Daily Risk'] = None  # Replace with your code
    
    # Calculate annualized return (252 trading days)
    stats['Annual Return'] = None  # Replace with your code
    
    # Calculate annualized risk
    stats['Annual Risk'] = None  # Replace with your code
    
    # Calculate Sharpe ratio
    stats['Sharpe Ratio'] = None  # Replace with your code
    
    return stats

def find_best_stock(stats_df):
    """
    Find the best stock to invest in based on the highest Sharpe ratio.
    
    Parameters:
    stats_df (pandas.DataFrame): DataFrame containing statistics for each stock
    
    Returns:
    tuple: (best_stock, best_sharpe_ratio)
    """
    # TODO: Find the stock with the highest Sharpe ratio
    # Your code here
    
    return None, None  # Replace with your code

def main():
    # Calculate daily returns
    print("Calculating daily returns...")
    returns_df = calculate_daily_returns(sample_data)
    
    # Calculate statistics
    print("Calculating statistics...")
    stats_df = calculate_statistics(returns_df)
    
    # Find the best stock
    best_stock, best_sharpe = find_best_stock(stats_df)
    
    # Display the results
    print("\nStock Statistics:")
    print(stats_df.round(4))
    
    print(f"\nBest Stock to Invest: {best_stock}")
    print(f"Sharpe Ratio: {best_sharpe:.4f}")
    
    # Calculate portfolio statistics
    print("\nCalculating equal-weight portfolio statistics...")
    portfolio_return = returns_df.mean(axis=1)
    portfolio_avg_return = portfolio_return.mean()
    portfolio_risk = portfolio_return.std()
    portfolio_annual_return = portfolio_avg_return * 252
    portfolio_annual_risk = portfolio_risk * np.sqrt(252)
    portfolio_sharpe = (portfolio_annual_return - risk_free_rate) / portfolio_annual_risk
    
    print(f"Portfolio Average Daily Return: {portfolio_avg_return:.4f}")
    print(f"Portfolio Daily Risk: {portfolio_risk:.4f}")
    print(f"Portfolio Annual Return: {portfolio_annual_return:.4f}")
    print(f"Portfolio Annual Risk: {portfolio_annual_risk:.4f}")
    print(f"Portfolio Sharpe Ratio: {portfolio_sharpe:.4f}")
    
    # Compare with individual stocks
    print(f"\nIs the portfolio better than the best stock? {'Yes' if portfolio_sharpe > best_sharpe else 'No'}")

if __name__ == "__main__":
    main()

'''
Expected Output:
--------------

Calculating daily returns...
Calculating statistics...

Stock Statistics:
            Avg Daily Return  Daily Risk  Annual Return  Annual Risk  Sharpe Ratio
AAPL                  0.0047      0.0118        1.1864      0.1873        6.2272
MSFT                  0.0046      0.0074        1.1607      0.1175        9.7932
GOOG                  0.0030      0.0073        0.7478      0.1156        6.2961
AMZN                  0.0023      0.0073        0.5879      0.1156        4.9126
TSLA                  0.0043      0.0151        1.0704      0.2404        4.3671

Best Stock to Invest: MSFT
Sharpe Ratio: 9.7932

Calculating equal-weight portfolio statistics...
Portfolio Average Daily Return: 0.0038
Portfolio Daily Risk: 0.0056
Portfolio Annual Return: 0.9506
Portfolio Annual Risk: 0.0894
Portfolio Sharpe Ratio: 10.4139

Is the portfolio better than the best stock? Yes
'''