from matplotlib import pyplot as plt
import numpy as np
import random

nums_rooms = [4, 1, 4, 2, 3, 5]
prices = [500, 120, 450, 230, 400, 700]

def square_trick(base_price, price_per_room, num_rooms, price, learning_rate):
    predicted_price = base_price + price_per_room*num_rooms
    base_price += learning_rate*(price-predicted_price)
    price_per_room += num_rooms*learning_rate*(price-predicted_price)
    return price_per_room, base_price
 
def absolute_trick(base_price, price_per_room, num_rooms, price, learning_rate):
    predicted_price = base_price + price_per_room*num_rooms
    if predicted_price > price:
        price_per_room -= learning_rate*num_rooms
        base_price -= learning_rate
    else:
        price_per_room += learning_rate*num_rooms
        base_price += learning_rate
    return price_per_room, base_price
    
plt.xlabel('Количество комнат')
plt.ylabel('Цена')
plt.title('Обучение линейной регрессии')
plt.plot(nums_rooms, prices, 'ro', label='Реальные данные')

#Линейная регрессия(квадратичный подход)
def linear_regression_square(nums_rooms, prices, learning_rate = 0.1, epochs = 1000):
    print(f"Квадратичный подход")
    base_price = random.uniform(0, 100)
    price_per_room = random.uniform(0, 200)
    for epoch in range(epochs):
        index = random.randint(0, len(nums_rooms)-1)
        price = prices[index]
        num_rooms = nums_rooms[index]
        price_per_room, base_price = square_trick(base_price, price_per_room, num_rooms, price, learning_rate)
        if epoch % 200 == 0:
            print(f"Эпоха №{epoch+1}")
            print(f"Цена за комнату: {price_per_room}")
            print(f"Начальная цена: {base_price}")
            
    x = np.linspace(0, 6, 10)
    y = base_price + price_per_room * x
    plt.plot(x, y, label='Модель с квадратичным подходом', color = "blue")
 
#Линейная регрессия(абсолютный подход)
def linear_regression_absolute(nums_rooms, prices, learning_rate = 0.1, epochs = 1000):
    print(f"Абсолютный подход")
    base_price = random.uniform(0, 100)
    price_per_room = random.uniform(0, 200)
    for epoch in range(epochs):
        index = random.randint(0, len(nums_rooms)-1)
        price = prices[index]
        num_rooms = nums_rooms[index]
        price_per_room, base_price = absolute_trick(base_price, price_per_room, num_rooms, price, learning_rate)
        if epoch % 200 == 0:
            print(f"Эпоха №{epoch+1}")
            print(f"Цена за комнату: {price_per_room}")
            print(f"Начальная цена: {base_price}")
       
    x = np.linspace(0, 6, 10)
    y = base_price + price_per_room * x
    plt.plot(x, y, label='Модель с абсолютным подходом', color = "green")

linear_regression_square(nums_rooms, prices)
linear_regression_absolute(nums_rooms, prices)
plt.legend()
plt.grid(True)
plt.show()
