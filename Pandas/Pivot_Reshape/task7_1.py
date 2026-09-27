import pandas as pd

df = pd.DataFrame({
    'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-01', '2024-01-02'],
    'city': ['Moscow', 'SPb', 'Moscow', 'SPb', 'Moscow', 'SPb'],
    'product': ['A', 'A', 'A', 'A', 'B', 'B'],
    'sales': [100, 200, 150, 250, 120, 180]
})

print(df.pivot_table(
    values='sales',
    index='date',
    columns='city',
    aggfunc='sum'))
print(df.pivot_table(
    values='sales',
    index='date',
    columns='product',
    aggfunc='mean'))
print(df.pivot_table(
    values='sales',
    index='date',
    columns='city',
    aggfunc=['sum', 'mean']))
print(df.pivot_table(
    values='sales',
    index='date',
    columns='city',
    aggfunc='sum',
    fill_value=0))
print(df.pivot_table(
    values='sales',
    index='date',
    columns='city',
    aggfunc='sum',
    margins=True))