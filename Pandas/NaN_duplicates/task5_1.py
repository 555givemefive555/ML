import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', None, 'Diana', 'Eve', 'Bob'],
    'age': [25, None, 35, 28, None, 30],
    'salary': [80000, 95000, 120000, None, 150000, 95000]
})

print(df.isna().sum())
print(df.isna().sum().sum())
s = df.isna().sum(axis=1)
print(df.iloc[s[s > 0].index])
print(df.dropna())
ss = df['salary'].isna()
print(df.iloc[ss[ss == True].index])