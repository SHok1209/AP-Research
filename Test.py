import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv



bitfile = pd.read_csv('bitcoin.csv', parse_dates=['Date'])
ethfile = pd.read_csv('ethereum.csv', parse_dates=['Date'])



print(bitfile.info(), ethfile.info())

#(New Value - Old Value) / Old Value * 100 = percentage change





plt.show()
plt.savefig('ethpercent.png')

ethfile.plot(x = "Date", y = ['High', 'Low'])
plt.show()
plt.savefig('ethgraph.png')


bitfile.columns = bitfile.columns.str.strip()

print(bitfile.info())

bitfile["BitcoinPercentDif"] = ((bitfile['Bitcoin High'] - bitfile['Bitcoin Low']) / bitfile['Bitcoin Low'] * 100)

bitfile["EthereumPercentDif"]= ((bitfile['Ethereum High'] - bitfile['Ethereum Low']) / bitfile['Ethereum Low'] * 100)

print(bitfile['Date'])



bitfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif"])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-12-31', '2024-10-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentDECOCT.png')


bitfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif"])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-09-30', '2024-07-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentSEPJUL.png')

bitfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif"])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-06-30', '2024-04-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentMAYAPR.png')

bitfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif"])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-03-30', '2024-01-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentMARJAN.png')

print('The average Bitcoin price is', sum(bitfile['Bitcoin Open']) / len(bitfile['Bitcoin Open']))
print('The average Ethereum price is',sum(bitfile['Ethereum Open']) / len(bitfile['Ethereum Open']))

bitfile['Bithigh']= sorted(bitfile['BitcoinPercentDif'], reverse=True)
Bithigh = bitfile['Bithigh'][:10]
print(Bithigh)

bitfile['Ethhigh']= sorted(bitfile['EthereumPercentDif'], reverse=True)
Ethhigh = bitfile['Ethhigh'][:10]
print(Ethhigh)



