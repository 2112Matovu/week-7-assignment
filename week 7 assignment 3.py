import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

sns.set(style="whitegrid")

plt.figure(figsize=(8,5))
plt.plot(df.index, df['sepal_length'], label='Sepal Length')
plt.plot(df.index, df['sepal_width'], label='Sepal Width')
plt.title('Line Chart: Sepal Length and Width over Samples')
plt.xlabel('Sample Index')
plt.ylabel('Length / Width (cm)')
plt.legend()
plt.show()

plt.figure(figsize=(6,4))
species_avg = df.groupby('species')['petal_length'].mean()
sns.barplot(x=species_avg.index, y=species_avg.values, palette='viridis')
plt.title('Bar Chart: Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

plt.figure(figsize=(6,4))
plt.hist(df['petal_width'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram: Distribution of Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='sepal_length', y='petal_length', hue='species', palette='deep')
plt.title('Scatter Plot: Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
