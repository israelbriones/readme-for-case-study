import heapq as hq
import math
import random
import io
import csv
import time
from matplotlib import pyplot as plt


# Initializes values for class Node, with left and right pointers, the value stored in the node, 
# the level at which the node is found and the number of left and right children
class Node:
    def __init__(self, key, level):
        self.left = None
        self.right = None
        self.val = key
        self.level = level
        self.r_children = 0
        self.l_children = 0

# Defines a class for a k-dimensional tree used to preprocess data and store coordinates from a k-dimensional space
class KDTree:
    #initialization function 
    def __init__(self, val, k=2):
        self.root = Node(val, 0)
        self.k = k

    #function used to insert a node into the tree
    def insert(self, key):
        self.insert_h(self.root, key, 0)

    #function used to copy a tree
    def copy(self, tree):
        self.copy_h(self.root, tree)

    #function that contains the algorithm for copying a tree
    def copy_h(self, root, tree):
        if root != None:
            tree.insert(root.val)
            self.copy_h(root.left, tree)
            self.copy_h(root.right, tree)

    #function that defines the algorithm for inserting a node into a tree
    def insert_h(self, r, key, level):
        if r is None:
            r = Node(key, level)
        else:
            if r.val[level%self.k] < key[level%self.k]:
                r.right = self.insert_h(r.right, key, level+1)
                r.r_children = 1 + r.right.r_children + r.right.l_children
            elif r.val[level%self.k] > key[level%self.k]:
                r.left = self.insert_h(r.left, key, level+1)
                r.l_children = 1 + r.left.l_children + r.left.l_children
            elif r.val[level%self.k] == key[level%self.k]:
                if r.val[(level+1)%self.k] < key[(level+1)%self.k]:
                    r.right = self.insert_h(r.right, key, level+1)
                    r.r_children = 1 + r.right.r_children + r.right.l_children
                elif r.val[(level+1)%self.k] > key[(level+1)%self.k]:
                    r.left = self.insert_h(r.left, key, level+1)
                    r.l_children = 1 + r.left.l_children + r.left.l_children
                elif r.val[(level+1)%self.k] == key[(level+1)%self.k]:
                    return r
        return r

    # this function can be called to print an in-order traversal of a tree
    def inorder_print(self):
        self.inorder_print_h(self.root)
    # function that defines the algorithm for an in-order tree traversal 
    def inorder_print_h(self, r):
        if r:
            self.inorder_print_h(r.left)
            self.inorder_print_h(r.right)
            print("{} at level {}".format(r.val, r.level))

#euclidian distance formula
def distance(p1, p2):
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))

# function that returns an array of all coordinates in a csv file
# the return array is also shuffled in order to improve the efficiency of the KD Tree
def get_all_points(csv_reader):
    line_count = 0
    all_points = []
    for row in csv_reader:
        if row[2] != 'x':
            line_count += 1
            all_points.append([float(row[2]), float(row[3])])
    
    random.shuffle(all_points)
    return all_points

# class used in preprocessing which stores the geographic data from the data in a csv file 
class GeographicData:
    def __init__(self, all_points):
        self.minX = 0
        self.minY = 0
        self.tree = self.build_kd_tree(all_points)
        self.density_matrix = self.build_density_mat(all_points, self.tree)
        self.all_points = all_points

    #density function defined according to the requirements of task1
    def density(self, point):
        x = math.floor(point[0] + self.minX)
        y = math.floor(point[1] + self.minY)
        if self.density_matrix[x][y][0] == 0:
            self.density_matrix[x][y][0] = self.density_logn(point, self.tree.root, 5)
        return self.density_matrix[x][y][0]

    # finds density using kd tree
    def density_logn(self, p, root, r):
        if r == 0:
            return 0
        return self.number_of_nodes(p, root, r) / (math.pi * r*r)

    # finds all nodes that are in a circle centerd at p with radius r 
    def number_of_nodes(self, p, root, r):
        num_points = 0.0
        if root:
            if distance(p, root.val) < r:
                num_points = self.number_of_nodes(p, root.left, r) + 1 + self.number_of_nodes(p, root.right, r)
            elif p[root.level % 2] + r < root.val[root.level % 2]:
                num_points = self.number_of_nodes(p, root.left, r)
            elif p[root.level % 2] - r > root.val[root.level % 2]:
                num_points = self.number_of_nodes(p, root.right, r)
            else:
                num_points = self.number_of_nodes(p, root.left, r) + 0 + self.number_of_nodes(p, root.right, r)
        else:
            num_points = 0
        return num_points

    #builds the kd_tree using the coordinate points obtained from the data
    def build_kd_tree(self, all_points):
        tree = KDTree(all_points[0])
        for point in all_points:
            tree.insert(point)
        return tree

    #builds a matrix storing values from the density function 
    def build_density_mat(self, all_points, tree):
        max_x = -float('inf')
        min_x = float('inf')
        max_y = -float('inf')
        min_y = float('inf')
        for point in all_points:
            if point[0] < min_x:
                min_x = point[0]
            if point[0] > max_x:
                max_x = point[0]
            if point[1] < min_y:
                min_y = point[1]
            if point[1] > max_y:
                max_y = point[1]

        self.minX = min_x
        self.minY = min_y
        density_matrix = [[[0,0] for _ in range(math.floor(2*(max_y-min_y)))]]*math.floor(2*(max_x-min_x))
        for i in range(len(density_matrix)):
            for j in range(len(density_matrix[0])):
                for k in range(2):
                    density_matrix[i][j][k] = 0

        points_looked = []
        for point in all_points:
            x = math.floor(point[0]-min_x)
            y = math.floor(point[1]-min_y)
            if density_matrix[x][y][1] == 0:
                density_matrix[x][y][0] = self.density_logn(point, tree.root, 5)
                density_matrix[x][y][1] = 1
        return density_matrix

    def hubs(self, k, radius):
        arr = self.all_points
        size = len(arr)
        # Creating Min Heap for given
        # array with only k elements
        # Create min heap using heapq module
        minHeap = []
        index = 0
        while len(minHeap) < k:
            skip = False
            for point in minHeap:
                if distance(point, arr[index]) < radius:
                    skip = True
                    break 
            if skip:
                index += 1
                continue
            minHeap.append(arr[index])
            index += 1
        hq.heapify(minHeap)
    # Loop For each element in array
        # after the kth element
        index = 0
        for i in range(k, size):
            # If current element is smaller
            # # than minimum ((top element of 
            # # the minHeap) element, do nothing
            # 
            # # and continue to next element
            if self.density(minHeap[0]) > self.density(arr[i]):
                continue
            skip = False
            for point in minHeap:
                if distance(point, arr[i]) < radius:
                    skip = True
                    break
            if skip:
                continue

# Otherwise Change minimum element
# (top element of the minHeap) to
# current element by polling out
# the top element of the minHeap
            else:
    # deleting top element of the min heap
                minHeap[0] = minHeap[-1]
                minHeap.pop()
                minHeap.append(arr[i])
    #    maintaining heap again using
    # O(n) time operation....
                minHeap.sort(key=self.density)
                hq.heapify(minHeap)
                index += 1
        return minHeap

# importing csv file and pre-processing it 
csv_file = open('geolife-cars.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
all_points = get_all_points(csv_reader)
csv_file.close()


# make geo_data from the csv dataset
geo_data = GeographicData(all_points)


hubs_list = geo_data.hubs(10, 8)

####################################
# ploting code
X = []
Y = []
for i in geo_data.all_points:
    X.append(i[0])
    Y.append(i[1])

hubX = []
hubY = []
circles = []
for i in hubs_list:
    hubX.append(i[0])
    hubY.append(i[1])
    circles.append(plt.Circle((i[0], i[1]), 8, fill=False, color='k', linestyle='--'))

fig=plt.figure(figsize=(10, 7.5), dpi=80)
ax=fig.add_subplot()


ax.scatter(X,Y, s=1)
ax.set_label('Points of P')
ax.set_ylabel('Latitude')
ax.set_xlabel('Longitude')

for i in circles:
    ax.add_patch(i)

ax.axis("equal")
ax.scatter(hubX,hubY, s=10, facecolors='none', edgecolors='r')
ax.set_label('Hub Points H')
ax.legend()
plt.show()

################################

# get the csv file for the other subsets of data
csv_file_10 = open('geolife-cars-ten-percent.csv')
csv_file_30 = open('geolife-cars-thirty-percent.csv')
csv_file_60 = open('geolife-cars-sixty-percent.csv')
csv_reader_10 = csv.reader(csv_file_10, delimiter=',')
csv_reader_30 = csv.reader(csv_file_30, delimiter=',')
csv_reader_60 = csv.reader(csv_file_60, delimiter=',')
all_points_10 = get_all_points(csv_reader_10)
all_points_30 = get_all_points(csv_reader_30)
all_points_60 = get_all_points(csv_reader_60)

#close the files
csv_file_10.close()
csv_file_30.close()
csv_file_60.close()
# tree.inorder_print()​
#make geo_data datastructs from the files
geo_data_10 = GeographicData(all_points_10)
geo_data_30 = GeographicData(all_points_30)
geo_data_60 = GeographicData(all_points_60)


# code to time the data
begin = time.time()
geo_data.hubs(geo_data_10, 10, 8)
end = time.time()
print("The algorith's runtime in milliseconds is {}".format((end - begin)*1000))
begin = time.time()
geo_data.hubs(geo_data_30, 10, 8)
end = time.time()
print("The algorith's runtime in milliseconds is {}".format((end - begin)*1000))

begin = time.time()
geo_data.hubs(geo_data_60, 10, 8)
end = time.time()
print("The algorith's runtime in milliseconds is {}".format((end - begin)*1000))
begin = time.time()
geo_data.hubs(geo_data, 10, 8)
end = time.time()
print("The algorith's runtime in milliseconds is {}".format((end - begin)*1000))