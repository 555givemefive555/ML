import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', None, 'Diana', 'Eve'],
    'age': [25, None, 35, 28, None],
    'salary': [80000, 95000, 120000, None, 150000]
})
print(df['age'].fillna(df['age'].mean()).astype(int))
print(df['salary'].fillna(df['salary'].median()))
print(df['name'].fillna('Unknown'))
print(df.dropna(subset=['salary']))
print(df.dropna(how='all'))
print(df.dropna(how='any', axis=1))