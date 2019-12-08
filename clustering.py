import random
import copy
import numpy as np
from scipy.spatial import distance


# do k-means clustering until the cluster does not change
def cluster(file_name, k, method='random', num_iter=10):
    f = open(file_name, 'r')
    lines = f.readlines()[1:]
    vec_list = []
    for l in lines:
        vector = l.split()
        vec_list.append([float(v) for v in vector])
    vec_list = np.asarray(vec_list)
    f.close()
    upper = 1 << 31
    best_cluster = []
    best_center = []
    best_dist = upper
    for i in range(num_iter):
        min_sum_dist = upper
        center_list = initialize(copy.deepcopy(vec_list), k, method)
        while True:
            clusters = [[] for j in range(k)]
            sum_dist = 0.0
            for v in vec_list:
                dist = [distance.euclidean(v[:-1], center_list[x][:-1]) for x in range(k)]
                min_dist = min(dist)
                min_index = [index for index, value in enumerate(dist) if value == min_dist]
                min_values = [len(clusters[ind]) for ind in min_index]
                r_i = min_index[min_values.index(min(min_values))]
                clusters[r_i].append(v)
                sum_dist += min_dist

            if min_sum_dist > sum_dist:
                center_list = calculate_center(clusters)
                min_sum_dist = sum_dist
            else:
                if best_dist > min_sum_dist:
                    best_dist = min_sum_dist
                    best_center = center_list
                    best_cluster = clusters
                break
    """            
    for c in best_cluster:
        for v in c:
            print(v[-1])
        print("----------------------")
    """
    return best_center, best_cluster, best_dist


# select initial points for k-means clustering
def initialize(vec_list, k, method):
    init_points = []
    random.shuffle(vec_list)    # shuffle vectors to make it has random order
    if method == 'random':  # assign vectors to each cluster and calculate central point as a initial point
        clusters = [[] for i in range(k)]
        count = 0
        while count < len(vec_list):
            clusters[count % k].append(vec_list[count])
            count += 1
        init_points = calculate_center(clusters)
    elif method == 'forgy':     # pick random vectors as initial points (forgy method)
        for i in range(k):
            init_points.append(vec_list[i])
    elif method == 'k-means++':     # stochastically select a vector that is far from the previously selected vector
        init_points.append(vec_list.pop(0))
        while len(init_points) != k:
            current = init_points[-1]
            dist_list = []
            for v in vec_list:
                dist = distance.euclidean(v[:-1], current[:-1]) ** 2
                dist_list.append(dist)
            dist_list = np.cumsum(dist_list)
            dist_sum = dist_list[-1]
            dist_list = dist_list / dist_sum
            rand_p = random.random()
            for i, d in enumerate(dist_list):
                if rand_p < d:
                    init_points.append(vec_list.pop(i))
                    break
    return np.asarray(init_points)


def calculate_center(clusters):     # calculate center at each cluster
    center_points = []
    for c in clusters:
        if len(c) == 0:
            center_points.append(clusters[0][0])
            continue
        point = np.mean(np.array(c), axis=0)
        new_c = np.power(np.asarray(c) - point, 2)
        dist_c = [sum(j[:-1]) for j in new_c]
        center_points.append(c[np.argmin(dist_c)])
    return np.asarray(center_points)
