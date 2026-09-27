import pandas as pd

df = pd.DataFrame({
    'user_id': [1, 2, 2, 3, 3, 3, 4],
    'name': ['Alice', 'Bob', 'Bob', 'Charlie', 'Charlie', 'Charlie', 'Diana'],
    'amount': [100, 200, 200, 300, 300, 300, 400]
})

print(df.duplicated().sum())
print(len(df.drop_duplicates()))
print(df['user_id'].duplicated().sum())
print(df.drop_duplicates(subset=['user_id'], keep='first'))
print(df.drop_duplicates(subset=['user_id'], keep='last'))
print(df.drop_duplicates(keep=False))
print(pd.unique(df))
