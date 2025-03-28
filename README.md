# CU Quants Club - 03.11 Coding Challenge

## Basic Stock Returns and Risk Analysis

### Overview

This challenge is designed to help you practice key concepts in quantitative finance, specifically risk and return analysis. Participants will work with stock price data to calculate daily returns, evaluate risk, and determine the best stock to invest in using the Sharpe ratio.

### Task Breakdown

1. **Calculate Daily Returns**: Implement a function to compute daily percentage returns from stock prices.

2. **Compute Sharpe Ratio**: Calculate key risk and return metrics, including average daily return, standard deviation (risk), annualized return and risk, and the Sharpe ratio.

3. **Identify the Best Stock**: Find the stock with the highest Sharpe ratio.

4. **Match Expected Output Format**: Ensure that your output format matches the provided format exactly.

5. **Compare with Solutions**: Once completed, compare your results with the provided solutions to check for accuracy and alternative approaches.

### Requirements

- Use only NumPy and Pandas libraries.

- All stock price data is provided in the template (no need for external data sources).

- Follow the instructions in the TODO comments within the code template.

### Evaluation Criteria

Your solution will be assessed based on:

1. **Correctness**: Properly implemented calculations.

2. **Output Format**: Results must match the provided format precisely.

3. **Code Clarity & Organization**: Readable and well-structured code.

### Expected Output Format (Example)

```
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
```

### Submission Instructions

1. Complete the coding challenge by implementing all TODO sections.

2. Ensure that your output matches the expected results exactly.

3. Compare your results with the provided solutions to verify correctness and explore alternative approaches.

Happy coding and good luck!
