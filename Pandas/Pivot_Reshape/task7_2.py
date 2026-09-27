import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'math': [5, 4, 3],
    'physics': [4, 5, 5],
    'chemistry': [3, 3, 4]
})

df1 = df.melt(
    id_vars=['name'],
    value_vars=['math', 'physics', 'chemistry'],
    var_name='subject',
    value_name='score')
print(df1)
df2 = df1.pivot_table(
    values='score',
    index='name',
    columns='subject')
print(df, df2)
