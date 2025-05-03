import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

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

####################################################################################

def BitcoinPercentdif_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['BitcoinPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse

####################################################################################

def BinancePercentdif_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['BinancePercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def CardanoPercentdif_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['CardanoPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def AvalanchePercentdif_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['AvalanchePercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def LitecoinPercentdif_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['LitecoinPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def EthereumPercentdif_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['EthereumPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def SolanaPercentdif_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['SolanaPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def DogecoinPercentdif_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['DogecoinPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def MoneroPercentdif_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['MoneroPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse
####################################################################################

def DashPercentdif_get_mse(data):
    """Calculates and returns the Mean Squared Error (MSE)."""

    data['Days'] = (data['Date'] - data['Date'].min()).dt.days

    X = data[['Days']]
    y = data['DashPercentDif']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predicted_prices = model.predict(X_test)

    # Calculate the MSE
    mse = mean_squared_error(y_test, predicted_prices)

    return mse


# Assuming 'allfile' is your DataFrame with the crypto data
print("Crypto with Supply Capacity")
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

supplycapacity = Bitcoin_mse_value + Binance_mse_value + Cardano_mse_value + Avalanche_mse_value + Litecoin_mse_value

print(f'The average is:', supplycapacity / 5 )

#####################################
print("######################################################")
print('Crypto without supply capacity')

Monero_mse_value = Monero_get_mse(allfile)
print(f"Mean Squared Error Monero: {Monero_mse_value:.2f}")

Ethereum_mse_value = Ethereum_get_mse(allfile)
print(f"Mean Squared Error Ethereum: {Ethereum_mse_value:.2f}")

Solana_mse_value = Solana_get_mse(allfile)
print(f"Mean Squared Error Solana: {Solana_mse_value:.2f}")

Dogecoin_mse_value = Dogecoin_get_mse(allfile)
print(f"Mean Squared Error Dogecoin: {Dogecoin_mse_value:.2f}")

Dash_mse_value = Dash_get_mse(allfile)
print(f"Mean Squared Error Dash: {Dash_mse_value:.2f}")

NOsupplycapacity = Monero_mse_value + Ethereum_mse_value + Solana_mse_value + Dogecoin_mse_value + Dash_mse_value

print(f'The average is:', NOsupplycapacity / 5 )

print("######################################################")

print('Crypto with supply capacity')

BitcoinPercentdif_mse_value = BitcoinPercentdif_get_mse(allfile)
print(f"Mean Squared Error Bitcoin Percentdif: {BitcoinPercentdif_mse_value:.2f}")

BinancePercentdif_mse_value = BinancePercentdif_get_mse(allfile)
print(f"Mean Squared Error Binance Percentdif: {BinancePercentdif_mse_value:.2f}")

CardanoPercentdif_mse_value = CardanoPercentdif_get_mse(allfile)
print(f"Mean Squared Error Cardano Percentdif: {CardanoPercentdif_mse_value:.2f}")

AvalanchePercentdif_mse_value = AvalanchePercentdif_get_mse(allfile)
print(f"Mean Squared Error Avalanche Percentdif: {AvalanchePercentdif_mse_value:.2f}")

LitecoinPercentdif_mse_value = LitecoinPercentdif_get_mse(allfile)
print(f"Mean Squared Error Litecoin Percentdif: {LitecoinPercentdif_mse_value:.2f}")

supplycapacitypercdif = BitcoinPercentdif_mse_value + BinancePercentdif_mse_value + CardanoPercentdif_mse_value + AvalanchePercentdif_mse_value + LitecoinPercentdif_mse_value

print(f'The average is:', supplycapacitypercdif / 5 )


print("######################################################")

print('Crypto without supply capacity')

EthereumPercentdif_mse_value = EthereumPercentdif_get_mse(allfile)
print(f"Mean Squared Error Ethereum: {EthereumPercentdif_mse_value:.2f}")

SolanaPercentdif_mse_value = SolanaPercentdif_get_mse(allfile)
print(f"Mean Squared Error Solana Percentdif: {SolanaPercentdif_mse_value:.2f}")

DogecoinPercentdif_mse_value = DogecoinPercentdif_get_mse(allfile)
print(f"Mean Squared Error Dogecoin Percentdif: {DogecoinPercentdif_mse_value:.2f}")

MoneroPercentdif_mse_value = MoneroPercentdif_get_mse(allfile)
print(f"Mean Squared Error Monero Percentdif: {MoneroPercentdif_mse_value:.2f}")

DashPercentdif_mse_value = DashPercentdif_get_mse(allfile)
print(f"Mean Squared Error Dash Percentdif: {DashPercentdif_mse_value:.2f}")

NOsupplycapacitypercdif = MoneroPercentdif_mse_value + EthereumPercentdif_mse_value + SolanaPercentdif_mse_value + DogecoinPercentdif_mse_value + DashPercentdif_mse_value

print(f'The average is:', NOsupplycapacitypercdif / 5 )

