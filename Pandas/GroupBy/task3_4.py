import pandas as pd

df = pd.DataFrame({
    'city': ['Moscow', 'SPb', 'Moscow', 'Moscow', 'SPb', 'Moscow'],
    'dept': ['IT', 'IT', 'Sales', 'IT', 'Sales', 'Sales'],
    'salary': [80000, 95000, 120000, 90000, 150000, 100000]
})

print(df.groupby(['city', 'dept']).agg('mean'))
print(df.groupby(['city', 'dept'], as_index=False).agg('mean'))
print(df.groupby(['city', 'dept']).agg('mean').reset_index())
print(df.groupby(['city', 'dept']).get_group(('Moscow', 'IT')))