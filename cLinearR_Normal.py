import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

allfile = pd.read_csv('Crypto.csv', parse_dates=['Date'])

################################################################# Bitcoin


def aBitcoin_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Bitcoin Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Bitcoin Open'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Bitcoin Price Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aBitcoin_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.

################################################################# Binance


def aBinance_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Binance Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Binance Open'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Binance Price Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aBinance_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Cardano


def aCardano_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Cardano Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Cardano Open'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Cardano Price Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aCardano_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Avalanche


def aAvalanche_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Avalanche Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Avalanche Open'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Avalanche Price Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aAvalanche_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Litecoin


def aLitecoin_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Litecoin Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Litecoin Open'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Litecoin Price Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aLitecoin_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Ethereum


def aEthereum_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Ethereum Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Ethereum Open'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Ethereum Price Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aEthereum_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Solana


def aSolana_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Solana Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Solana Open'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Solana Price Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aSolana_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Dogecoin


def aDogecoin_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Dogecoin Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Dogecoin Open'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Dogecoin Price Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aDogecoin_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Monero


def aMonero_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Monero Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Monero Open'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Monero Price Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aMonero_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Dash


def aDash_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['Dash Open']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Dash Open'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Dash Price Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aDash_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.


# Assuming 'allfile' is your DataFrame with the crypto data
aBitcoin_linear_regression_prediction_graph(allfile)

aBinance_linear_regression_prediction_graph(allfile)

aAvalanche_linear_regression_prediction_graph(allfile)

aCardano_linear_regression_prediction_graph(allfile)

aLitecoin_linear_regression_prediction_graph(allfile)

aEthereum_linear_regression_prediction_graph(allfile)

aDogecoin_linear_regression_prediction_graph(allfile)

aSolana_linear_regression_prediction_graph(allfile)

aMonero_linear_regression_prediction_graph(allfile)

aDash_linear_regression_prediction_graph(allfile)




