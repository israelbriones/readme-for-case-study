import matplotlib.pyplot as plt
from task3 import *
      
edges = e_max(P2, Q2)
data = edge_lengths(edges)

fig, ax = plt.subplots(figsize =(12, 7))
ax.hist(data, bins = 100, color="green")

plt.title("Edge Lengths Between Trajectories P2 and Q2")
plt.xlabel("Edge Lengths in Kilometers")
plt.ylabel("Frequency")

print(fd(edges))
plt.show()
