import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



allfile = pd.read_csv('AllCrypto.csv', parse_dates=['Date'])



print(allfile.info())

#(New Value - Old Value) / Old Value * 100 = percentage change


plt.show()

allfile.plot(x = "Date", y = ['Ethereum High', 'Ethereum Low'])
plt.show()
plt.savefig('ethereum_graph.png')


allfile.columns = allfile.columns.str.strip()


allfile["BitcoinPercentDif"] = ((allfile['Bitcoin High'] - allfile['Bitcoin Low']) / allfile['Bitcoin Low'] * 100)

allfile["EthereumPercentDif"]= ((allfile['Ethereum High'] - allfile['Ethereum Low']) / allfile['Ethereum Low'] * 100)

print(allfile['Date'])



allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif"])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-12-31', '2024-10-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentDECOCT.png')


allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif"])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-09-30', '2024-07-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentSEPJUL.png')

allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif"])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-06-30', '2024-04-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentMAYAPR.png')

allfile.plot(x = 'Date', y = ["BitcoinPercentDif", "EthereumPercentDif"])
plt.title('crypto change ')
plt.xlabel('Date')
plt.xlim('2024-03-30', '2024-01-01')  
plt.ylabel('Percent Difference')
plt.show()
plt.savefig('percentMARJAN.png')

print('The average Bitcoin price is', sum(allfile['Bitcoin Open']) / len(allfile['Bitcoin Open']))
print('The average Ethereum price is',sum(allfile['Ethereum Open']) / len(allfile['Ethereum Open']))



allfile['Bithigh']= sorted(allfile['BitcoinPercentDif'], reverse=True)
Bithigh = allfile['Bithigh'][:10]
print(Bithigh)

# Get the top 10 largest values and their indices
top_indices = allfile['BitcoinPercentDif'].nlargest(10).index
top_data = allfile.loc[top_indices,['BitcoinPercentDif', 'Date']]

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



