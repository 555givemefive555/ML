import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

all_users = ["User1", "User2", "User3"]
all_movies = ['Movie1', 'Movie2', 'Movie3']

G = nx.Graph()
G.add_nodes_from(all_users+all_movies)

flag_accept = "Yes"

for i in range(len(all_users)):
    information = list(input().split())
    user = information[0]
    count_movies = int(information[1])
    movies = information[2:]
    movies.sort()
    if all_movies != movies:
        print(all_movies)
        print(movies)
        flag_accept = "No"
    for movie in movies:
        temp_tuple = tuple([user, movie])
        G.add_edges_from([temp_tuple])

plt.figure(figsize = (36, 12))
plt.subplot(366)
nx.draw(G, with_labels = 1)
plt.show()

print(flag_accept)
