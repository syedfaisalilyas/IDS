import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

np.random.seed(42)
start_date = datetime.now() - timedelta(days=730)
date_range = [start_date + timedelta(days=random.randint(0, 730)) for _ in range(1000)]
companies_list = ['CorpA', 'CorpB', 'CorpC', 'CorpD', 'CorpZE']
market_data = {
    'Trade Date': date_range,
    'Corporation': np.random.choice(companies_list, 1000),
    'Opening Price': np.random.uniform(60, 450, 1000),
    'Closing Price': np.random.uniform(60, 450, 1000),
    'Trade Volume': np.random.randint(2000, 1500000, 1000)
}
df_stocks = pd.DataFrame(market_data)

closing_prices = df_stocks['Closing Price'].to_numpy()
percent_change = np.diff(closing_prices) / closing_prices[:-1] * 100
df_stocks['Percent Change Daily'] = np.insert(percent_change, 0, 0)

high_change_df = df_stocks[df_stocks['Percent Change Daily'] > 2]
total_traded_volume = df_stocks.groupby('Corporation')['Trade Volume'].sum()

selected_company = 'CorpA'
company_prices = df_stocks[df_stocks['Corporation'] == selected_company].sort_values('Trade Date')

plt.figure(figsize=(10, 6))
plt.plot(company_prices['Trade Date'], company_prices['Closing Price'], marker='x', color='g', alpha=0.7)
plt.title(f'Closing Price Trend for {selected_company}')
plt.xlabel('Trade Date')
plt.ylabel('Closing Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# avg_daily_change = df_stocks.groupby('Corporation')['Percent Change Daily'].mean()

# plt.figure(figsize=(8, 5))
# avg_daily_change.plot(kind='bar', color='purple', alpha=0.85)
# plt.title('Average Daily Percent Change per Corporation')
# plt.xlabel('Corporation')
# plt.ylabel('Average Daily Change (%)')
# plt.tight_layout()
# plt.show()

# print("\nStock price increase by more than 2% on the following days:")
# print(high_change_df.head())
# print("\nTotal Volume Traded per Corporation:")
# print(total_traded_volume)
