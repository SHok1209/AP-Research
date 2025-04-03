import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



allfile = pd.read_csv('Crypto.csv', parse_dates=['Date'])



print(allfile.info())

#(New Value - Old Value) / Old Value * 100 = percentage change


plt.show()

allfile.plot(x = "Date", y = ['Ethereum High', 'Ethereum Low'])
plt.show()
plt.savefig('ethereum_graph.png')


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

allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif", 'DogecoinPercentDif', 'SolanaPercentDif', 'BinancePercentDif', 'CardanoPercentDif', 'AvalanchePercentDif', 'LitecoinPercentDif', 'MoneroPercentDif', 'DashPercentDif'])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-12-31', '2024-12-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentDEC.png')


allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif", 'DogecoinPercentDif', 'SolanaPercentDif', 'BinancePercentDif', 'CardanoPercentDif', 'AvalanchePercentDif', 'LitecoinPercentDif', 'MoneroPercentDif', 'DashPercentDif'])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-11-30', '2024-11-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentNOV.png')


allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif", 'DogecoinPercentDif', 'SolanaPercentDif', 'BinancePercentDif', 'CardanoPercentDif', 'AvalanchePercentDif', 'LitecoinPercentDif', 'MoneroPercentDif', 'DashPercentDif'])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-10-31', '2024-10-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentOCT.png')


allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif", 'DogecoinPercentDif', 'SolanaPercentDif', 'BinancePercentDif', 'CardanoPercentDif', 'AvalanchePercentDif', 'LitecoinPercentDif', 'MoneroPercentDif', 'DashPercentDif'])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-09-30', '2024-09-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentSEP.png')

allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif", 'DogecoinPercentDif', 'SolanaPercentDif', 'BinancePercentDif', 'CardanoPercentDif', 'AvalanchePercentDif', 'LitecoinPercentDif', 'MoneroPercentDif', 'DashPercentDif'])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-08-31', '2024-08-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentAUG.png')

allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif", 'DogecoinPercentDif', 'SolanaPercentDif', 'BinancePercentDif', 'CardanoPercentDif', 'AvalanchePercentDif', 'LitecoinPercentDif', 'MoneroPercentDif', 'DashPercentDif'])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-07-31', '2024-07-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentJUL.png')

allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif", 'DogecoinPercentDif', 'SolanaPercentDif', 'BinancePercentDif', 'CardanoPercentDif', 'AvalanchePercentDif', 'LitecoinPercentDif', 'MoneroPercentDif', 'DashPercentDif'])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-06-30', '2024-06-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentJUN.png')


allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif", 'DogecoinPercentDif', 'SolanaPercentDif', 'BinancePercentDif', 'CardanoPercentDif', 'AvalanchePercentDif', 'LitecoinPercentDif', 'MoneroPercentDif', 'DashPercentDif'])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-05-31', '2024-05-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentMAY.png')

allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif", 'DogecoinPercentDif', 'SolanaPercentDif', 'BinancePercentDif', 'CardanoPercentDif', 'AvalanchePercentDif', 'LitecoinPercentDif', 'MoneroPercentDif', 'DashPercentDif'])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-04-30', '2024-04-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentAPR.png')

allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif", 'DogecoinPercentDif', 'SolanaPercentDif', 'BinancePercentDif', 'CardanoPercentDif', 'AvalanchePercentDif', 'LitecoinPercentDif', 'MoneroPercentDif', 'DashPercentDif'])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-03-31', '2024-03-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentMAR.png')

allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif", 'DogecoinPercentDif', 'SolanaPercentDif', 'BinancePercentDif', 'CardanoPercentDif', 'AvalanchePercentDif', 'LitecoinPercentDif', 'MoneroPercentDif', 'DashPercentDif'])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-02-29', '2024-02-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentFEB.png')

allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif", 'DogecoinPercentDif', 'SolanaPercentDif', 'BinancePercentDif', 'CardanoPercentDif', 'AvalanchePercentDif', 'LitecoinPercentDif', 'MoneroPercentDif', 'DashPercentDif'])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-01-31', '2024-01-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentJAN.png')









allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif"])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-12-31', '2024-10-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('bitethpercentDECOCT.png')


allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif"])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-09-30', '2024-07-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('bitethpercentSEPJUL.png')

allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif"])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-06-30', '2024-04-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('bitethpercentMAYAPR.png')

allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif"])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-03-30', '2024-01-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('bitethpercentMARJAN.png')
