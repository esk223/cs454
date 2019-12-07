from scipy.spatial import distance


def intra_fitness(centers, clusters):
    intra = 0.0
    for i in range(len(centers)):
        cluster_i = clusters[i]
        for vector in cluster_i:
            intra += distance.euclidean(centers[i][:-1], vector[:-1])
    return intra


def conn_fitness(clusters):
    conn = 0.0
    for cluster in clusters:
        len_c = len(cluster)
        sum = 0.0
        for i in range(len_c):
            for j in range(i + 1, len_c):
                sum += inverse_d(cluster[i], cluster[j])
        sum /= len_c
        conn += sum
    conn /= len(clusters)
    return conn


def inverse_d(vec_a, vec_b):
    return min(1/(distance.euclidean(vec_a[:-1], vec_b[:-1]) + 0.000000001), 10)
