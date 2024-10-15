import numpy as np
import pandas as pd

def c():
    print("----------------------------------------------------------------")

# Creating series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s
print(s)
c()
#Creating DataFrames
dates = pd.date_range("20240303", periods=6)
print(dates)
c()

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
c()
print(df[0:3])
c()

#pandas.DataFrame.loc
df = pd.DataFrame(
    [[1, 2], [4, 5], [7, 8]],
    index=['cobra', 'viper', 'sidewinder'],
    columns=['max_speed', 'shield']
)

print(df)
c()
print(df.loc[['viper', 'sidewinder']])
c()
print(df.loc[df['shield'] > 4])
c()
print(df.loc[(df['max_speed'] > 1) & (df['shield'] < 8)])
c()
print(df.loc[(df['max_speed'] > 4) | (df['shield'] < 5)])
c()

#pandas.DataFrame.iloc
mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
test = pd.DataFrame(mydict)
print(test)
print(type(test.iloc[1]))
c()
print(test.iloc[1]) #scalar
c()
print(test.iloc[[0]]) #list
c()
print(test.iloc[[True, False, True]])
c()

#data types
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2.dtypes)
c()
c()
c()
##################################################################################################################### Section 2
# Creating a sample DataFrame
data = {'name': ['Ayhan', 'Beyhan', 'Ceyhan', 'Deyhan'],
        'age': [25, 30, 31, 44],
        'gender': ['M', 'M', 'F', 'F']}
df3 = pd.DataFrame(data)
print(df3)
c()

# 1. Selection:
# Select specific rows or columns based on conditions using boolean indexing
specific_rows = df3[df3['age'] > 30]  # Select rows where 'age' is greater than 30
print("\nSpecific Rows:")
print(specific_rows)

specific_columns = df3[['name', 'gender']]  # Select the 'name' and 'gender' columns
print("\nSpecific Columns:")
print(specific_columns)
c()
# Utilize methods like .head(), .tail(), and .sample() to display subsets of the DataFrame
first_rows = df3.head(2)  # Display the first 2 rows
last_rows = df3.tail(2)   # Display the last 2 rows
random_sample = df3.sample(n=2)  # Display a random sample of 2 rows
print("\nFirst Rows")
print(first_rows)
print("\nLast Rows:")
print(last_rows)
print("\nRandom Sample:")
print(random_sample)
c()
# 2. Filtering:
# Boolean Indexing
boolean_mask = df3[df3['gender'] == 'M']  # Filter rows where 'gender' is 'M'
print("\nBoolean Mask:")
print(boolean_mask)
# .loc and .iloc
filtered_loc = df3.loc[df3['age'] > 30]  # Filter using labels (.loc)
print("\nFiltered using .loc:")
print(filtered_loc)
filtered_iloc = df3.iloc[(df3['age'] > 30).values]  # Filter using positions (.iloc)
print("\nFiltered using .iloc:")
print(filtered_iloc)
c()
# Comparison Operators
filtered_comparison = df3[df3['age'] < 35]  # Filter based on comparison operators
print("\nFiltered using comparison operators:")
print(filtered_comparison)
# .isin() Method
filter_isin = df3[df3['name'].isin(['Ayhan', 'Deyhan'])]  # Filter based on whether a value exists in a specific list/collection
print("\nFiltered using .isin() method:")
print(filter_isin)
# .query()
query_filter = df3.query('age > 30')  # Filter using concise string-based method
print("\nFiltered using .query():")
print(query_filter)
c()
# 3. Modification:
# Add new columns using assignment
df3['city'] = ['Ankara', 'Bolu', 'Corum', 'Duzce']  # Add a new column to the DataFrame
print(df3)
