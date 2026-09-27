import pandas as pd

df = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5],
    'signup_date': ['2023-01-15', '2023-06-20', '2023-12-01', '2024-03-10', '2024-07-04'],
    'amount': [100, 200, 150, 300, 250]
})

print(df['signup_date'].dt.year)
df['signup_date'] = pd.to_datetime(df['signup_date'])
df['year'] = df['signup_date'].dt.year
df['month'] = df['signup_date'].dt.month
df['day'] = df['signup_date'].dt.day
df['dayofweek'] = df['signup_date'].dt.dayofweek
df['day_name'] = df['signup_date'].dt.day_name()
df['is_weekend'] = df['dayofweek'] >= 5
df['days_since_signup'] = pd.Timestamp('today') - df['signup_date']