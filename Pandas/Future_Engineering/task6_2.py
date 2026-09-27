import pandas as pd

df = pd.DataFrame({
    'email': ['alice@mail.ru', 'BOB@GMAIL.COM', 'charlie@yandex.ru', None, 'eve@mail.ru'],
    'name': ['  Alice  ', 'Bob', 'Charlie ', None, 'Eve']
})

df['email'] = df['email'].str.lower()
print(df['email'].str.split('@').str[1])
print(df[df['email'].str.contains('@mail.ru')])
print(df[df['email'].str.startswith('alice')])
df['name'] = df['name'].str.strip()
print(df['name'].str.len())