import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler

# Load data only ONCE
allfile = pd.read_csv('Crypto.csv', parse_dates=['Date'])
allfile.columns = allfile.columns.str.strip()

# Calculate daily percentage differences
cryptos = ['Bitcoin', 'Ethereum', 'Dogecoin', 'Solana', 'Cardano', 
           'Binance', 'Avalanche', 'Monero', 'Litecoin', 'Dash']

for crypto in cryptos:
    high_col = f'{crypto} High'
    low_col = f'{crypto} Low'
    percent_diff_col = f'{crypto}PercentDif'
    allfile[percent_diff_col] = ((allfile[high_col] - allfile[low_col]) / allfile[low_col] * 100)

# Feature engineering - FIXED: using Close prices instead of High for moving averages
for crypto in cryptos:
    close_col = f'{crypto} Close'  # Using Close prices is more standard
    allfile[f'{crypto}_7day_MA'] = allfile[close_col].rolling(window=7).mean()
    allfile[f'{crypto}_30day_MA'] = allfile[close_col].rolling(window=30).mean()
    allfile[f'{crypto}_volatility'] = allfile[close_col].pct_change().rolling(window=7).std()
    # Lag features
    for lag in [1, 3, 7]:
        allfile[f'{crypto}_lag_{lag}'] = allfile[close_col].shift(lag)

# Drop NA values
allfile = allfile.dropna()

# Convert dates to numerical values
allfile['Days'] = (allfile['Date'] - allfile['Date'].min()).dt.days

# Target and features
target_crypto = 'Bitcoin'
target_col = f'{target_crypto} Close'  # Predicting Close price is more standard
features = [f'{target_crypto}_lag_1', f'{target_crypto}_lag_3', f'{target_crypto}_lag_7',
            f'{target_crypto}_7day_MA', f'{target_crypto}_volatility'] + \
           [f'{crypto}_volatility' for crypto in cryptos]

X = allfile[features]
y = allfile[target_col]

# Train-test split (chronological)
train_size = int(0.8 * len(X))
X_train, X_test = X.iloc[:train_size], X.iloc[train_size:]
y_train, y_test = y.iloc[:train_size], y.iloc[train_size:]

# Scale features - FIXED: proper reshaping
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Scale target separately
y_scaler = MinMaxScaler()
y_train_scaled = y_scaler.fit_transform(y_train.values.reshape(-1, 1)).ravel()
y_test_scaled = y_scaler.transform(y_test.values.reshape(-1, 1)).ravel()

# Models
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42)
}

predictions = {}
for name, model in models.items():
    model.fit(X_train_scaled, y_train_scaled)
    pred_scaled = model.predict(X_test_scaled)
    predictions[name] = y_scaler.inverse_transform(pred_scaled.reshape(-1, 1)).ravel()

# Forecasting function - IMPROVED
def forecast_future(model, last_known_values, steps=30):
    forecasts = []
    current_input = last_known_values.copy()
    for _ in range(steps):
        # Predict next value (scaled)
        pred_scaled = model.predict(current_input.reshape(1, -1))[0]
        pred = y_scaler.inverse_transform([[pred_scaled]])[0][0]
        forecasts.append(pred)
        # Update input for next prediction
        current_input = np.roll(current_input, -1)
        current_input[-1] = pred_scaled  # Use scaled value for consistency
    return forecasts

# Generate forecasts
last_values = X_test_scaled[-1]
future_dates = pd.date_range(start=allfile['Date'].iloc[-1], periods=31)[1:]
gbr_forecast = forecast_future(models["Gradient Boosting"], last_values)

# Plotting - IMPROVED
plt.figure(figsize=(15, 7))
plt.plot(allfile['Date'], allfile[target_col], label='Historical Prices')
plt.plot(allfile['Date'].iloc[train_size:], y_test, label='Actual Test Values', color='green')
plt.plot(allfile['Date'].iloc[train_size:], predictions["Gradient Boosting"], 
         label='GBR Predictions', color='purple', linestyle='--')
plt.plot(future_dates, gbr_forecast, label='GBR 30-Day Forecast', color='red')
plt.fill_between(future_dates, 
                 np.array(gbr_forecast)*0.95,
                 np.array(gbr_forecast)*1.05,
                 color='pink', alpha=0.3)
plt.title(f'{target_crypto} Price Prediction')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.savefig('AI_Model.png')
plt.show()

# Feature importance
plt.figure(figsize=(10, 6))
importances = models["Random Forest"].feature_importances_
pd.Series(importances, index=features).sort_values().plot.barh()
plt.title('Random Forest Feature Importance')
plt.show()

# Metrics
print("=== Model Performance ===")
for name, pred in predictions.items():
    mae = mean_absolute_error(y_test, pred)
    print(f"{name} - MAE: {mae:.2f}")