import pandas as pd

df = pd.DataFrame({
    'city': ['Moscow', 'SPb', 'Moscow', 'Kazan', 'SPb', 'Moscow'],
    'name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'salary': [80000, 95000, 120000, 70000, 150000, 90000],
    'age': [25, 30, 35, 28, 42, 33]
})

df['city_avg_salary'] = df.groupby('city')['salary'].transform('mean')
df['salary_diff'] = df.groupby('city')['salary'].transform(lambda x: x - x.mean())
df['city_size'] = df.groupby('city')['name'].transform('size')
df['share'] = df.groupby('city')['salary'].transform(lambda x: x / x.sum() * 100)
print(df)