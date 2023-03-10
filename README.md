# Case Study: Trajectory Data Analysis, Part I

## General Information

This Case Study is about creating algorithms that carry out numerous analyses of trajectory data. Beyond designing algorithms, we will implement and analyze them in order to complete three tasks. Each of which entails modeling a problem and running experiments on the implemented algorithm to analyze the solution.

## Group Members
Alexis Cruz-Ayala, Nicole Romero Ospina, Rosine Uwineza, and Israel Briones

## Installation
Below is what should be installed to do the three tasks:
```
python -m pip install -U pip
python -m pip install -U matplotlib
```
## Technologies
* The datasets provided (geolife-cars.csv, geolife-cars-ten-percent.csv, geolife-cars-thirty-percent.csv, geolife-cars-sixty-percent.csv)
* Visual Studio Code
* Python 3.9.12
* matplotlib.pyplot

## Task 1
In this task,

## Task 2
In this task, we want to design an algorithm to compute d(q,e), the distance between a point q and a segment e. Then we use said algorithm to design the greedy algorithm TS-greedy(T,ε) to compute an ε-simplification of T. There is also code to plot two lines for the trajectory ID 128-20080503104400 and its simplification using the greedy algorithm for ε = 0.03,0.1,0.3 (kilometers). Lastly, there is code to report the compression ratio |T|/|T*| for trajectories 128-20080503104400, 010-20081016113953, 115-20080520225850, and 115-20080615225707 using TS-greedy for ε = 0.03 km. In order to create the plots matplotlib.pyplot will be needed. 


## Task 3
In this task, we want to design algorithms that compute dtw(P,Q) and fd(P,Q) along with assignments E<sub>avg</sub> and E<sub>max</sub> that realize the minimum values. In our code we are able to do the following:

*  Implement the algorithms to compute dtw(P,Q) and fd(P,Q)
* Run both algorithms for trajectory pairs (128-20080503104400, 128-20080509135846),(010-20081016113953, 010-20080923124453), and (115-20080520225850, 115-20080615225707). We use that to plot a histogram for each pair for both E<sub>avg</sub> and E<sub>max</sub> and their lengths of edges.
* Compute a simplification of each of T1 = 115-20080520225850, T2 = 115-20080615225707 for ε = 0.03,0.1,0.3 (kilometers).

Uisng our code in task3.py, we accomplished this by first using the function 'initialize' to create the arrays of the coordinate points that will be used in a trajectory that while still in the target trajectory, will add coordinate points to array. 

```
def initialize(gc, target):
    ans = []
    for i in range(1, len(gc)):
        single = gc[i].strip("\n").split(",")
        id = single[1]
        if(id == target):
            ans.append([float(single[2]), float(single[3])])
            i += 1
            while(id == target):
                single = gc[i].strip("\n").split(",")
                id = single[1]
                ans.append([float(single[2]), float(single[3])])
                i += 1
            break
    return ans
```
Then the function 'dist' is used to return the Euclidian distance formula and the 'dist2' function is used to return the square of the Euclidian distance formula. With x = 0 and y = 1 in both functions to represent their respective indices for the array retrieved from csv.
```
def dist(P, Q):
    x = 0
    y = 1
    return math.sqrt((float(P[x]) - float(Q[x]))**2 + (float(P[y]) - float(Q[y]))**2)
def dist2(p, q):
    x = 0
    y = 1
    return (float(p[x]) - float(q[x]))**2 + (float(p[y]) - float(q[y]))**2
```
This is where we coded out our 'E<sub>avg</sub>' function, the purpose being to return an array containing all of the edges and the dtw value. We used memoization and initalized an empty list 'e' that was the return array. Using 'pairs = set()' to ensure we aren't storing duplicate edge lengths. And assigning n and m to len(P) and Len(Q) respectively. We let the first element in the tuple as the score of the current subsequences and the second one being the number of edges used so far. We had a part in the code in case of a base case where one of the trajectories has no points. Then we iterated through the range of '1...n' and a nested loop '1...m' to find dtw at any point P[i], Q[j]. We based the calculations needed to make on using (P[i-1], Q[j]), (P[i], Q[j-1]), and (P[i-1], Q[j-1]). assigned the new dtw for current (P[i], Q[j]) to 'cost'. The next part of the code starting at 's = 0' was to update the amount of edges based on which option was the minimum and add chosen edge to set, as well as its length to e. We used 'mem[(i, j)] = (cost, s)' in the code to store the cost and number of edges. Then returned 'e' at the end.
```
def e_avg(P, Q):
    mem = {}


