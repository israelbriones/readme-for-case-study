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

Uisng the code in task3.py, you're able to accomplish the first bullet point by computing the algorithms needed to do E<sub>avg</sub> and E<sub>max</sub>. As well as compute dtw(P,Q) and fd(P,Q).

Using the code in the files in e_avg1.py, e_avg2.py, and e_avg3.py to create the histograms for E<sub>avg</sub>. Then the code in the files e_max1.py, e_max2.py, and e_max3.py to create the histograms for E<sub>max</sub>. In order to create the plots matplotlib.pyplot will be needed.

The code in the file e_avg_simp.py is what is needed to compute the simplification of each of T1 and T2 for ε = 0.03,0.1,0.3 (kilometers).
 
