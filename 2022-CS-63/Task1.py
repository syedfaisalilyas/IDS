import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

days_in_year = pd.date_range(start='2024-01-01', periods=365)
temps = np.random.randint(5, 38, size=365)
humidity_levels = np.random.randint(25, 85, size=365)
wind_speeds = np.random.randint(1, 25, size=365)
conditions = np.random.choice(['Clear', 'Stormy', 'Overcast'], size=365)

climate_data = pd.DataFrame({
    'Day': days_in_year,
    'Temp (°C)': temps,
    'Humidity (%)': humidity_levels,
    'Wind (km/h)': wind_speeds,
    'Condition': conditions
})

print(climate_data)

temp_array = climate_data['Temp (°C)'].to_numpy()
avg_temp = np.mean(temp_array)
median_temperature = np.median(temp_array)
temperature_std_dev = np.std(temp_array)

print(f'Average Temp: {avg_temp:.2f}°C')
print(f'Median Temp: {median_temperature:.2f}°C')
print(f'Standard Deviation of Temp: {temperature_std_dev:.2f}°C')

hot_clear_days = climate_data[(climate_data['Temp (°C)'] > 32) & (climate_data['Condition'] == 'Clear')]
hot_clear_day_count = hot_clear_days.shape[0]

print(hot_clear_days)
print(f"Number of clear days with temperature above 32°C: {hot_clear_day_count}")

avg_humidity_by_condition = climate_data.groupby('Condition')['Humidity (%)'].mean().reset_index()
avg_humidity_by_condition.columns = ['Condition', 'Avg Humidity']

print(avg_humidity_by_condition)

plt.figure(figsize=(10, 6))
plt.plot(climate_data['Day'], climate_data['Temp (°C)'], color='orange')
plt.title('Yearly Temperature Fluctuations')
plt.xlabel('Day of the Year')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

condition_counts = climate_data['Condition'].value_counts()

plt.figure(figsize=(8, 5))
condition_counts.plot(kind='bar', color='skyblue')
plt.title('Weather Condition Frequency Throughout the Year')
plt.xlabel('Condition')
plt.ylabel('Days Count')
plt.tight_layout()
plt.show()
