import pandas as pd

df = pd.DataFrame({
    'user_id': range(1, 11),
    'age': [17, 22, 35, 42, 28, 55, 61, 33, 47, 19]
})

df['type'] = pd.cut(df['age'], bins=[0, 18, 35, 60, 100], labels=['minor', 'young', 'adult', 'senior'])
print(pd.qcut(df['age'], q=4))
print(df.groupby('type')['type'].count())
print(df.groupby('type')['age'].mean())