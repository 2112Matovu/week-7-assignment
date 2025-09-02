import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

print("Basic statistics of numerical columns:")
print(df.describe())

numerical_cols = df.select_dtypes(include='number').columns  
grouped = df.groupby('species')[numerical_cols].mean()
print("\nMean of numerical columns for each species:")
print(grouped)

print("\nPatterns / Observations:")
for species in df['species'].unique():
    mean_values = df[df['species'] == species][numerical_cols].mean()
    print(f"\nAverage measurements for {species}:")
    print(mean_values)

print("\nCorrelation matrix:")
print(df[numerical_cols].corr())
