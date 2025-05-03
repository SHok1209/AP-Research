import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



allfile = pd.read_csv('Crypto.csv', parse_dates=['Date'])



print(allfile.info())



allfile.columns = allfile.columns.str.strip()


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
#######################################################################

allfile.plot(x = 'Date', y = [ "EthereumPercentDif", 'DogecoinPercentDif', 'SolanaPercentDif', 'MoneroPercentDif', 'DashPercentDif'])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-12-31', '2024-12-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentWITHOUTsupplyDEC.png')