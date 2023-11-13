import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/sakth/Downloads/WhatsApp Image 2023-11-02 at 09.39.30_85640aa8.jpg.csv")
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
start_date = '2020-04-06'
end_date = '2020-04-23'
filtered_data = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
plt.figure(figsize=(12, 6))
plt.scatter(filtered_data['volume'], filtered_data['close'], color='b', label='Volume vs. Stock Prices')
plt.title('Trading Volume vs. Stock Prices of Alphabet Inc. Stock')
plt.xlabel('Volume')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()
