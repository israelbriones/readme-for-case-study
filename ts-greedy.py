import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
import io



with open('./geolife-cars.csv', 'r') as f:
    csv_reader = f.readlines()
        
def initialize(csv_reader, target):
    ans = []
    for i in range(1, len(csv_reader)):
        single = csv_reader[i].strip("\n").split(",")
        id = single[1]
        if(id == target):
            ans.append([id, float(single[2]), float(single[3])])
            i += 1
            while(id == target): #while still in the target trajectory, add coordinate points to array
                single = csv_reader[i].strip("\n").split(",")
                id = single[1]
                ans.append([id, float(single[2]), float(single[3])])
                i += 1
            break
    return ans


def get_all_points_by_id(csv_reader):
  line_count = 0
  id_traj = {'': [0, 0]}
  for row in csv_reader:
    if row[2] != 'x':
      line_count += 1
      if row[1] not in id_traj:
        id_traj[row[1]] = []
      id_traj[row[1]].append([float(row[2]), float(row[3])])
  return id_traj

csv_file = open('geolife-cars.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
id_traj = get_all_points_by_id(csv_reader)

csv_file.close()

#distance d(q,e)
def distance(p1, p2):
  return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))

def distPointToSegment(q, a, b):
  if a == b:
    return distance(q, a)
  v = [b[0] - a[0], b[1] - a[1]] #compute dx & dy
  w = [q[0] - a[0], q[1] - a[1]]
  proj = (v[0]*w[0] + v[1]*w[1]) / (v[0]*v[0] + v[1]*v[1]) #if proj q lies on v
  projPoint = [a[0] + proj*v[0], a[1] + proj*v[1]]
  if proj < 0:
    #point is closest to the start of v
    return distance(q, a)
  elif proj > 1:
    #point is closest to the end of v
    return distance(q, b)
  else:
    #return distance between q and the projection
    return distance(q, projPoint)

#ts-greedy algorithm
def simplify(T, eps):
  n = len(T)
  eSimp = []
  eSimp.append(T[0])
  for i in range(n):
    #Compute the distance between the current point and the last segment in eSimp
    dist = distPointToSegment(T[i], eSimp[len(eSimp)-1], eSimp[len(eSimp)-2])
    if dist > eps:
    #Add the current point to eSimp and update the last segment
      eSimp.append(T[i])
      eSimp[len(eSimp)-2] = T[i-1]
      eSimp[len(eSimp)-3] = T[i-1]
  return eSimp


#----------------------------------------------------------------------------------


#ratio function
def compression_ratio(T, Simp):
  return len(T) / len(Simp)


simp = simplify(id_traj['128-20080503104400'], 0.03)
#simp = simplify(id_traj['010-20081016113953'], 0.03)
#simp = simplify(id_traj['115-20080520225850'], 0.03)
#simp = simplify(id_traj['115-20080615225707'], 0.03)
T = id_traj['128-20080503104400']

print(compression_ratio(T, simp))


orginalX = []
orginalY = []
for i in id_traj['128-20080503104400']:
  orginalX.append(i[0])
  orginalY.append(i[1])

simp = simplify(id_traj['128-20080503104400'], 0.03)  
  
simpX = []
simpY = []
for i in simp:
  simpX.append(i[0])
  simpY.append(i[1])

plt.plot(orginalX, orginalY)
plt.scatter(simpX, simpY, s = 15, color = 'black')
plt.show()

