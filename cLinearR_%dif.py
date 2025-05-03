import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

allfile = pd.read_csv('Crypto.csv', parse_dates=['Date'])



allfile["BitcoinPercentDif"] = ((allfile['Bitcoin High'] - allfile['Bitcoin Low']) / allfile['Bitcoin Low'] * 100)

allfile["EthereumPercentDif"]= ((allfile['Ethereum High'] - allfile['Ethereum Low']) / allfile['Ethereum Low'] * 100)

allfile["DogecoinPercentDif"] = ((allfile['Dogecoin High'] - allfile['Dogecoin Low']) / allfile['Dogecoin Low'] * 100)

allfile["SolanaPercentDif"]= ((allfile['Solana High'] - allfile['Solana Low']) / allfile['Solana Low'] * 100)

allfile["CardanoPercentDif"] = ((allfile['Cardano High'] - allfile['Cardano Low']) / allfile['Cardano Low'] * 100)

allfile["BinancePercentDif"]= ((allfile['Binance High'] - allfile['Binance Low']) / allfile['Binance Low'] * 100)

allfile["AvalanchePercentDif"]= ((allfile['Avalanche High'] - allfile['Avalanche Low']) / allfile['Avalanche Low'] * 100)

allfile["MoneroPercentDif"]= ((allfile['Monero High'] - allfile['Monero Low']) / allfile['Monero Low'] * 100)

allfile["LitecoinPercentDif"]= ((allfile['Litecoin High'] - allfile['Litecoin Low']) / allfile['Litecoin Low'] * 100)

allfile["DashPercentDif"]= ((allfile['Dash High'] - allfile['Dash Low']) / allfile['Dash Low'] * 100)
print(allfile['Date'])

def aBitcoin_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['BitcoinPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['BitcoinPercentDif'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Bitcoin percent dif Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.savefig('aBitcoinPercentDif_Linear_Regression_Graph.png') 
    plt.show() 

################################################################# Binance


def aBinance_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['BinancePercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['BinancePercentDif'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Binance percent dif Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aBinancePercentDif_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Cardano


def aCardano_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['CardanoPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['CardanoPercentDif'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Cardano percent dif Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aCardanoPercentDif_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Avalanche


def aAvalanche_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['AvalanchePercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['AvalanchePercentDif'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Avalanche percent dif Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aAvalanchePercentDif_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Litecoin


def aLitecoin_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['LitecoinPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['LitecoinPercentDif'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Litecoin percent dif Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aLitecoinPercentDif_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Ethereum


def aEthereum_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['EthereumPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['EthereumPercentDif'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Ethereum percent dif Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aEthereumPercentDif_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Solana


def aSolana_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['SolanaPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['SolanaPercentDif'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Solana percent dif Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aSolanaPercentDif_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Dogecoin


def aDogecoin_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['DogecoinPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['DogecoinPercentDif'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Dogecoin percent dif Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aDogecoinPercentDif_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Monero


def aMonero_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['MoneroPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['MoneroPercentDif'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Monero percent dif Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aMoneroPercentDif_Linear_Regression_Graph.png') #saves the figure
    plt.show() #shows the figure.
################################################################# Dash


def aDash_linear_regression_prediction_graph(data):
    """Predicts and graphs the Bitcoin price using Linear Regression."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['DashPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the entire dataset
    predicted_prices = model.predict(X)

    # Plot the actual and predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['DashPercentDif'], label='Actual Price', color='blue')
    plt.plot(data['Date'], predicted_prices, label='Predicted Price (Linear Regression)', color='red', linestyle='--')
    plt.title('Dash percent dif Prediction with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    #Make sure to save the figure, or show it.
    plt.savefig('aDashPercentDif_Linear_Regression_Graph.png') #saves the figure
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




