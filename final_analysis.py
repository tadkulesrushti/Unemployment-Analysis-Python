import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Unemployment in India.csv")

# Data Cleaning
df = df.dropna()
df.columns = df.columns.str.strip()
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

print("="*50)
print("DATASET INFORMATION")
print("="*50)
print(df.info())

# 1. Unemployment Distribution

plt.figure(figsize=(8,5))
plt.hist(df['Estimated Unemployment Rate (%)'])
plt.title("Distribution of Unemployment Rate")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Frequency")
plt.show()

# 2. Unemployment Trend Over Time

monthly_unemployment = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(10,5))
plt.plot(monthly_unemployment.index,
         monthly_unemployment.values)

plt.title("Average Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Covid Impact Analysis

before_covid = df[df['Date'] < '2020-04-01']
after_covid = df[df['Date'] >= '2020-04-01']

print("\nAverage Unemployment Before Covid:",
      round(before_covid['Estimated Unemployment Rate (%)'].mean(),2))

print("Average Unemployment During Covid:",
      round(after_covid['Estimated Unemployment Rate (%)'].mean(),2))

# 4. Monthly Trend Analysis

df['Month'] = df['Date'].dt.month_name()

monthly_avg = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()

print("\nMonthly Average Unemployment")
print(monthly_avg)

plt.figure(figsize=(10,5))
monthly_avg.plot(kind='bar')
plt.title("Average Unemployment Rate by Month")
plt.xlabel("Month")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# 5. Top 10 States

state_unemployment = (
    df.groupby('Region')['Estimated Unemployment Rate (%)']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 States by Unemployment Rate")
print(state_unemployment)

plt.figure(figsize=(10,5))
state_unemployment.plot(kind='bar')
plt.title("Top 10 States with Highest Unemployment Rate")
plt.xlabel("State")
plt.ylabel("Average Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# 6. Rural vs Urban Analysis

area_unemployment = (
    df.groupby('Area')['Estimated Unemployment Rate (%)']
    .mean()
)

print("\nRural vs Urban Unemployment")
print(area_unemployment)

plt.figure(figsize=(6,4))
area_unemployment.plot(kind='bar')
plt.title("Rural vs Urban Unemployment Rate")
plt.xlabel("Area")
plt.ylabel("Average Unemployment Rate (%)")
plt.tight_layout()
plt.show()