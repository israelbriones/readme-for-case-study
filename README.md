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


