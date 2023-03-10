import sys
import math


# creating arrays of coordinate points in a trajectory
def initialize(gc, target):
    ans = []
    for i in range(1, len(gc)):
        single = gc[i].strip("\n").split(",")
        id = single[1]
        if(id == target):
            ans.append([float(single[2]), float(single[3])])
            i += 1
            while(id == target): #while still in the target trajectory, add coordinate points to array
                single = gc[i].strip("\n").split(",")
                id = single[1]
                ans.append([float(single[2]), float(single[3])])
                i += 1
            break
    return ans
            

# returns the Euclidian distance
def dist(P, Q):
    # x=0 and y=1 are their respective indices in array retrieved from csv
    x = 0
    y = 1
    return math.sqrt((float(P[x]) - float(Q[x]))**2 + (float(P[y]) - float(Q[y]))**2)

# returns the square of the Euclidian distance formula
def dist2(p, q):
    # x=0 and y=1 are their respective indices in array retrieved from csv
    x = 0
    y = 1
    return (float(p[x]) - float(q[x]))**2 + (float(p[y]) - float(q[y]))**2


# returns an array containing all of the edges and the dtw value
def e_avg(P, Q):
    mem = {}
    e = [] # return array 
    pairs = set() #set to ensure we aren't storing duplicate edge lengths
   
    n, m = len(P), len(Q)

    # first element in tuple is the score of the current subsequences, 
    # and the second one is the number of edges used so far 
    mem[(0, 0)] = (0.0, 0)
    
    # base case 0: one of the trajectories has no points
    for i in range(1, n):
        mem[(i, 0)] = (sys.float_info.max, 0)
    for j in range(1, m):
        mem[(0, j)] = (sys.float_info.max, 0)

    # finding dtw at any point P[i], Q[j]
    for i in range(1, n):
        for j in range(1, m):
            # d^2 (p_i, 1_j)
            distance = dist2(P[i], Q[j])
            # calculation using (P[i-1], Q[j]), (P[i], Q[i-1]), and (P[i-1], Q[i-1])
            p_less = (distance + (mem[(i-1, j)])[1] * (mem[(i-1, j)])[0])/ ((mem[(i-1, j)])[1] + 1)
            q_less = (distance + (mem[(i, j-1)])[1] * (mem[(i, j-1)])[0])/ ((mem[(i, j-1)])[1] + 1)
            both_less = (distance + (mem[(i-1, j-1)])[1] * (mem[(i-1, j-1)])[0])/ ((mem[(i-1, j-1)])[1] + 1)

            # new dtw for current (P[i], Q[j])
            cost = min(p_less, q_less, both_less)

            #update amount of edges based on which option was the minimum and add chosen edge to set, as well as its length to e
            s = 0
            if cost == p_less:
                s = (mem[(i-1, j)])[1] + 1
                if (i-1, j) not in pairs:
                    pairs.add((i-1,j)) 
                    e.append((P[i-1], Q[j]))
            elif cost == q_less:
                s = (mem[(i, j-1)])[1] + 1
                if (i, j-1) not in pairs:
                    pairs.add((i,j-1)) 
                    e.append((P[i], Q[j-1]))
            else:
                s = (mem[(i-1, j-1)])[1] + 1
                if (i-1, j-1) not in pairs:
                    pairs.add((i-1,j-1)) 
                    e.append((P[i-1], Q[j-1]))

            mem[(i, j)] = (cost, s) # storing cost and number of edges
    
    e.append(mem[(n-1, m-1)][0])
    return e

# returns the last element in an array, which will be the dtw for two trajectories
def dtw(arr):
    return arr[-1]


def e_max(P, Q):
    mem = {}
    edge_set = []

    n, m = len(P), len(Q)

    # first element in tuple is the score of the current subsequences,
    # and the second one is the number of edges used so far
    mem[(0, 0)] = (0.0, 0)

    # base case 0: one of the trajectories has no points
    for i in range(1, n):
        mem[(i, 0)] = (sys.float_info.max, 0)
    for j in range(1, m):
        mem[(0, j)] = (sys.float_info.max, 0)

    # e_max at any point p_i, q_j
    for i in range(1, n):
        for j in range(1, m):
            # d^2 (p_i, 1_j)
            distance = dist(P[i], Q[j])

            # calculation using p_i-1, q_i-1, and both, respectively
            p_less = (mem[(i-1, j)])[0]
            q_less = (mem[(i, j-1)])[0]
            both_less = (mem[(i-1, j-1)])[0]

            # 4 3 5 6
            # new e_max for (p_i, q_i)
            cost = min(distance, max(p_less, q_less, both_less))

            # update amount of edges based on which one of the above were the minimum and add chosen edge to array
            s = 0
            if cost == p_less:
                s = (mem[(i-1, j)])[1] + 1
                edge_set.append((P[i-1], Q[j]))
            elif cost == q_less:
                s = (mem[(i, j-1)])[1] + 1
                edge_set.append((P[i], Q[j-1]))
            else:
                s = (mem[(i-1, j-1)])[1] + 1
                edge_set.append((P[i-1], Q[j-1]))

            mem[(i, j)] = (cost, s)

    edge_set.append(mem[(n-1, m-1)][0])
    return edge_set

# returns the last element in an array, which will be the fd for two trajectories
def fd(arr):
    return arr[-1]


# returns an array of edge lengths for an assignment of two trajectories
def edge_lengths(arr):
    ans = []
    for edge in arr[:-1]:
        ans.append(dist(edge[0], edge[1]))
    return ans



#---------------------------------------------------------------

# pre-processing
with open("./geolife-cars.csv", "r") as f:
    gc = f.readlines()


ids = ["128-20080503104400", "128-20080509135846", "010-20081016113953", "010-20080923124453", "115-20080520225850", "115-20080615225707"]

# getting the different required trajectories by calling initialize()
P1 = initialize(gc, ids[0])
Q1 = initialize(gc, ids[1])


P2 = initialize(gc, ids[2])
Q2 = initialize(gc, ids[3])

P3 = initialize(gc, ids[4])
Q3 = initialize(gc, ids[5])

