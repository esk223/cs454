import random
import copy
import numpy as np
from scipy.spatial import distance


# do k-means clustering until the cluster does not change
def cluster(vec_list, k, method='random'):
    center_list = initialize(copy.deepcopy(vec_list), k, method)
    min_sum_dist = 1 << 31
    while True:
        clusters = [[] for i in range(k)]
        sum_dist = 0
        for v in vec_list:
            min_dist = 1 << 31
            min_index = 0
            for i in range(k):
                dist = distance.euclidean(v, center_list[i])
                if min_dist > dist:
                    min_dist = dist
                    min_index = i
            clusters[min_index].append(v)
            sum_dist += min_dist
        if min_sum_dist > sum_dist:
            center_list = calculate_center(clusters)
            min_sum_dist = sum_dist
        else:
            break

    return clusters


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
                dist = distance.euclidean(v, current) ** 2
                dist_list.append(dist)
            dist_list = np.cumsum(dist_list)
            dist_sum = dist_list[-1]
            dist_list = dist_list / dist_sum
            rand_p = random.random()
            for i, d in enumerate(dist_list):
                if rand_p < d:
                    init_points.append(vec_list.pop(i))
                    break
    return init_points


def calculate_center(clusters):     # calculate center at each cluster
    center_points = []
    for c in clusters:
        size = len(c)
        point = [sum(x) / size for x in zip(*c)]
        center_points.append(point)
    return center_points


vectors = []
for i in range(10):
    vectors.append([random.randint(0, 6) for i in range(4)])
print(vectors)
clusters = cluster(vectors, 3, 'forgy')
for c in clusters:
    print(c)
