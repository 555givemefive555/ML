import pandas as pd

df = pd.DataFrame({
    'city': ['Moscow', 'SPb', 'Moscow', 'Kazan', 'SPb', 'Moscow'],
    'name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'salary': [80000, 95000, 120000, 70000, 150000, 90000],
    'age': [25, 30, 35, 28, 42, 33]
})

print(df.groupby('city')['salary'].agg(['mean', 'std', 'count']))
print(df.groupby('city').agg({
    'salary': 'mean',
    'age': 'max'
    }))
print(df.groupby('city').agg(
    avg_salary=('salary', 'mean'),
    max_age=('age', 'max')
    ))
print(df.groupby('city')['salary'].agg(lambda x: x.max() - x.min()))