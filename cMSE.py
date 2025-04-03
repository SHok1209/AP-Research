import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

allfile = pd.read_csv('Crypto.csv', parse_dates=['Date'])

####################################################################################

def Bitcoin_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Bitcoin Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse

####################################################################################

def Binance_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Binance Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def Cardano_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Cardano Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def Avalanche_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Avalanche Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def Litecoin_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Litecoin Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def Ethereum_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Ethereum Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def Solana_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Solana Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def Dogecoin_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Dogecoin Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def Monero_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Monero Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def Dash_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Dash Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse


# Assuming 'allfile' is your DataFrame with the crypto data
Bitcoin_mse_value = Bitcoin_get_mse(allfile)
print(f"Mean Squared Error Bitcoin: {Bitcoin_mse_value:.2f}")

Binance_mse_value = Binance_get_mse(allfile)
print(f"Mean Squared Error Binance: {Binance_mse_value:.2f}")

Cardano_mse_value = Cardano_get_mse(allfile)
print(f"Mean Squared Error Cardano: {Cardano_mse_value:.2f}")

Avalanche_mse_value = Avalanche_get_mse(allfile)
print(f"Mean Squared Error Avalanche: {Avalanche_mse_value:.2f}")

Litecoin_mse_value = Litecoin_get_mse(allfile)
print(f"Mean Squared Error Litecoin: {Litecoin_mse_value:.2f}")

Solana_mse_value = Solana_get_mse(allfile)
print(f"Mean Squared Error Solana: {Solana_mse_value:.2f}")

Dogecoin_mse_value = Dogecoin_get_mse(allfile)
print(f"Mean Squared Error Dogecoin: {Dogecoin_mse_value:.2f}")

Monero_mse_value = Monero_get_mse(allfile)
print(f"Mean Squared Error Monero: {Monero_mse_value:.2f}")

Dash_mse_value = Dash_get_mse(allfile)
print(f"Mean Squared Error Dash: {Dash_mse_value:.2f}")

