import matplotlib.pyplot as plt
from task2 import *
from task3 import *

e1 = 0.03
e2 = 0.1
e3 = 0.3

T1 = P3
T2 = Q3
simp1_1 = simplify(T1, e1)
simp1_2 = simplify(T2, e1)
pairs1 = e_avg(simp1_1, simp1_2)
data1 = edge_lengths(pairs1)

simp2_1 = simplify(T1, e2)
simp2_2 = simplify(T2, e2)
pairs2 = e_avg(simp2_1, simp2_2)
data2 = edge_lengths(pairs2)

simp3_1 = simplify(T1, e3)
simp3_2 = simplify(T2, e3)
pairs3 = e_avg(simp3_1, simp3_2)
data3 = edge_lengths(pairs3)

plt.hist(data1, bins=200, color="red", label='ε = 0.03')
plt.hist(data2, bins=200, color="blue", label='ε = 0.1')
plt.hist(data3, bins=200, color="green", label='ε = 0.3')

plt.legend(loc='upper right')
plt.title("Edge Lengths Between Trajectories with Different Simplifications")
plt.xlabel('Edge Lengths in Kilometers')
plt.ylabel('Frequency')

plt.show()