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





print('The average Bitcoin price is', sum(allfile['Bitcoin Open']) / len(allfile['Bitcoin Open']))
print('The average Ethereum price is',sum(allfile['Ethereum Open']) / len(allfile['Ethereum Open']))











allfile['Bithigh']= sorted(allfile['BitcoinPercentDif'], reverse=True)
Bithigh = allfile['Bithigh'][:10]
print(Bithigh)

# Get the top 10 largest values and their indices
top_indices = allfile['BitcoinPercentDif'].nlargest(10).index
top_data = allfile.loc[top_indices,['BitcoinPercentDif', 'Date']]

#########################################################################

allfile['Ethhigh']= sorted(allfile['EthereumPercentDif'], reverse=True)
Ethhigh = allfile['Ethhigh'][:10]
print(Ethhigh)

# Get the top 10 largest values and their indices
top_indices = allfile['EthereumPercentDif'].nlargest(10).index
top_data = allfile.loc[top_indices,['EthereumPercentDif', 'Date']]

#########################################################################

allfile['Monhigh']= sorted(allfile['MoneroPercentDif'], reverse=True)
Monhigh = allfile['Monhigh'][:10]
print(Monhigh)

# Get the top 10 largest values and their indices
top_indices = allfile['MoneroPercentDif'].nlargest(10).index
top_data = allfile.loc[top_indices,['MoneroPercentDif', 'Date']]

#########################################################################

allfile['Dogehigh']= sorted(allfile['DogecoinPercentDif'], reverse=True)
Dogehigh = allfile['Dogehigh'][:10]
print(Dogehigh)

# Get the top 10 largest values and their indices
top_indices = allfile['DogecoinPercentDif'].nlargest(10).index
top_data = allfile.loc[top_indices,['DogecoinPercentDif', 'Date']]

#########################################################################

allfile['Solhigh']= sorted(allfile['SolanaPercentDif'], reverse=True)
Solhigh = allfile['Solhigh'][:10]
print(Solhigh)

# Get the top 10 largest values and their indices
top_indices = allfile['SolanaPercentDif'].nlargest(10).index
top_data = allfile.loc[top_indices,['SolanaPercentDif', 'Date']]

#########################################################################

allfile['Carhigh']= sorted(allfile['CardanoPercentDif'], reverse=True)
Carhigh = allfile['Carhigh'][:10]
print(Carhigh)

# Get the top 10 largest values and their indices
top_indices = allfile['CardanoPercentDif'].nlargest(10).index
top_data = allfile.loc[top_indices,['CardanoPercentDif', 'Date']]

#########################################################################

allfile['Avahigh']= sorted(allfile['AvalanchePercentDif'], reverse=True)
Avahigh = allfile['Avahigh'][:10]
print(Avahigh)

# Get the top 10 largest values and their indices
top_indices = allfile['AvalanchePercentDif'].nlargest(10).index
top_data = allfile.loc[top_indices,['AvalanchePercentDif', 'Date']]

#########################################################################

allfile['Binhigh']= sorted(allfile['BinancePercentDif'], reverse=True)
Binhigh = allfile['Binhigh'][:10]
print(Binhigh)

# Get the top 10 largest values and their indices
top_indices = allfile['BinancePercentDif'].nlargest(10).index
top_data = allfile.loc[top_indices,['BinancePercentDif', 'Date']]

#########################################################################

allfile['Litehigh']= sorted(allfile['LitecoinPercentDif'], reverse=True)
Litehigh = allfile['Litehigh'][:10]
print(Litehigh)

# Get the top 10 largest values and their indices
top_indices = allfile['LitecoinPercentDif'].nlargest(10).index
top_data = allfile.loc[top_indices,['LitecoinPercentDif', 'Date']]

#########################################################################

allfile['Dashigh']= sorted(allfile['DashPercentDif'], reverse=True)
Dashigh = allfile['Dashigh'][:10]
print(Dashigh)

# Get the top 10 largest values and their indices
top_indices = allfile['DashPercentDif'].nlargest(10).index
top_data = allfile.loc[top_indices,['DashPercentDif', 'Date']]

#########################################################################
plt.figure(figsize=(10, 5))
plt.bar(top_data['Date'], top_data['BitcoinPercentDif'], color='black')

# Labels and title
plt.xlabel("Date")
plt.ylabel("Bitcoin Percent Difference")
plt.title("Top Bitcoin Percent Differences by Date")
plt.xticks(rotation=45)  # Rotate x-axis labels for readability

plt.show()
plt.savefig('Bitcoin_Highest_Percentage.png')
print("Top Values and Their Indices:")
print(top_data)



#allfile['Ethhigh']= sorted(allfile['EthereumPercentDif'], reverse=True)
#Ethhigh = allfile['Ethhigh'][:10]
#print(Ethhigh)



