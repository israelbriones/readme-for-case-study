import matplotlib.pyplot as plt
from task3 import *        
        
edges = e_avg(P3, Q3)
data = edge_lengths(edges)

fig, ax = plt.subplots(figsize =(12, 7))
ax.hist(data, bins = 100)

plt.title("Edge Lengths Between Trajectories P3 and Q3")
plt.xlabel("Edge Lengths in Kilometers")
plt.ylabel("Frequency")

print(dtw(edges))
plt.show()
