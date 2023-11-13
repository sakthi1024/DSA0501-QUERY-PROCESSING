import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/sakth/Downloads/WhatsApp Image 2023-11-02 at 09.39.30_85640aa8.jpg.csv")
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
start_date = '2020-04-06'
end_date = '2020-04-23'
filtered_data = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
plt.figure(figsize=(12, 6))
plt.plot(filtered_data['date'], filtered_data['close'], marker='o', linestyle='-', color='b', label='Alphabet Inc. Stock Price')
plt.title('Historical Stock Prices of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()
