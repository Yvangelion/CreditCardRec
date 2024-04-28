import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class Engine:
    def __init__(self, start_date, benchmark=["SPY"], portfolio=[], data_file="", weights=[]):
        self.start_date = start_date
        self.benchmark = benchmark
        self.portfolio = portfolio
        self.data_file = data_file
        self.weights = weights
    
    def load_data(self):
        data = pd.read_csv(self.data_file, parse_dates=['Date'], index_col='Date')
        return data.loc[self.start_date:]
    
    def calculate_returns(self):
        data = self.load_data()
        portfolio_returns = pd.DataFrame(index=data.index)
        for asset, weight in zip(self.portfolio, self.weights):
            asset_returns = data[asset].pct_change().rename(asset)
            portfolio_returns = portfolio_returns.join(asset_returns)
        portfolio_returns['Portfolio'] = (portfolio_returns[self.portfolio] * self.weights).sum(axis=1)
        return portfolio_returns.dropna()
    
    def predict_optimal_allocation(self):
        data = self.load_data()
        X = data[self.portfolio]
        y = data[self.benchmark[0]]  # Predict against benchmark
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        return mse, model.feature_importances_
    
    def returns(engine):
        returns = engine.calculate_returns()
        sharpe_ratio = (returns.mean() / returns.std()) * (252 ** 0.5)
        cumulative_returns = (1 + returns).cumprod() - 1
        total_cumulative_return = cumulative_returns['Portfolio'].iloc[-1]  # Total cumulative return of the portfolio at the last date
        data = {
            'Sharpe Ratio': sharpe_ratio,
            'Total Cumulative Return': total_cumulative_return
        }
        return data 

# Example usage
portfolio = Engine(
    start_date="2018-01-01",
    benchmark=["SPY"],
    portfolio=["AAPL", "BABA", "CASH","GUY"],
    data_file="financial_data.csv",
    weights=[0.25, 0.25, 0.25, 0.25]  # Updated weights to match number of assets
)

print(Engine.returns(portfolio))
print(portfolio.predict_optimal_allocation())



