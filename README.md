# Artificial Intelligence for Portfolio Asset Allocation 

## Project Description:
This project aims to optimize an investment portfolio based on user-defined risk tolerance and retirement age. It combines financial data from multiple CSV files, calculates returns, determines risk tolerance based on age, and optimizes the portfolio using the Sharpe ratio or other criteria. Additionally, it includes a utility to process CSV files containing stock data and combine them into a single output file.

## Running Environments:
- Python 3.x+
- Required packages: pandas, numpy, scipy
- Step 1: Install requirements: 
    pip install -r requirements.txt
- Step 2: Input Data: 
    Input CSV data from market watch.
- Step 3: Run CSV cleaner:
    Python csvcleaner.py  
- Step 4: Run main application:
    Python app.py

## Major Results:
- Optimized portfolio weights based on user input and risk tolerance.
- Performance metrics including expected return, standard deviation (risk), and Sharpe ratio.
- Combined CSV file containing consolidated stock data.


### Example Run:
- Age: 40, Retirement Age: 65
- The optimized portfolio suggests investing in multiple assets including Apple (AAPL), Google (GOOG), Adobe (ADBE), Vanguard Total International Stock Index Fund (VTIAX),  Vanguard Total Stock Market Index Fund (VTSAX), and Vanguard Total Bond Market Index Fund (BND).
- All assets have equal weights except for AIRXX and FTDJX, which are not included.
- The determined risk tolerance is medium.
- Expected return: 18.91%
- Standard deviation (risk): 43.86%
- Sharpe Ratio: 0.4312
These indicate a positive excess return given the risk taken.
