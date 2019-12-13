import csv
import multiprocessing
import sys
import warnings
import output_change

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from deap import base
from deap import creator
from deap import gp
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import pairwise_distances
from sklearn.metrics import silhouette_score

import ea_simple_elitism
import multi_tree as mt
import vector_tree as vt
from ParallelToolbox import ParallelToolbox
from read_data import read_data
from selection import *

POP_SIZE = 1024
NGEN = 1
CXPB = 0.8
MUTPB = 0.2
ELITISM = 10
MAX_HEIGHT = 8
SEED= 100
REP = mt  # individual representation {mt (multi-tree) or vt (vector-tree)}
N_TREES = 1
DATA_DIR = '.'  # "/home/schofifinn/PycharmProjects/SSResearch/data"
METRIC = 'intra'
MAXIMISE = METRIC != 'intra'
#######################################################################3
#make feature for result 

from get_features import FeatureMaker
import random
import copy
import numpy as np
from scipy.spatial import distance
from clustering import cluster



def make_feature_file(fm, input_data_name):
    feature_file = open(input_data_name+".data", 'w')
    feature_file.write("classLast,{0},{1},space\n".format(fm.term_num(), fm.class_num()))
    for test_case_info in fm.case_info_list:
        str_vector = map(str, test_case_info.get_vector())
        feature_file.write("{0} {1}\n".format(" ".join(str_vector), test_case_info.get_classification()))
    feature_file.close()



##################################################################






def connectedness(cluster):
    print(cluster)
 

def evaluate(individual, toolbox, data, k, metric, maximise, distance_vector=None, labels_true=None):
    """
    Evaluates an individuals fitness. The fitness is the clustering performance on the data
    using the metric.

    :param individual: the individual to be evaluated
    :param toolbox: the evolutionary toolbox
    :param data: the data to be used to evaluate the individual
    :param k: the number of clusters for k-means
    :param metric: the metric to be used to evaluate clustering performance
    :param distance_vector: a pre-computed distance vector, required for silhouette-pre metric
    :param labels_true: the ground truth cluster labels, required for ari metric
    :return: the fitness of the individual
    """
    X = REP.process_data(individual, toolbox, data, MAX_HEIGHT)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        #print("Kmenas SEED",SEED)
        kmeans = KMeans(n_clusters=k, random_state=SEED).fit(X)
    labels = kmeans.labels_
    #print(labels)
    #print("\n")
    #print("\n")	
    #print("\n")
    # individuals that find single cluster are unfit
    nlabels = len(set(labels))
    if nlabels == 1:
        return [np.inf] if maximise else [-1]
    # uses precomputed distances of original data to avoid trending towards single dimension to
    # minimise silhouette.
    if metric == 'silhouette_pre':
        if distance_vector is None:
            raise Exception("Must provide distance vector for silhouette-pre metric.")
        return [silhouette_score(distance_vector, labels, metric='precomputed')]
    elif metric == 'silhouette':
        return [silhouette_score(X, labels, metric='euclidean')]
    elif metric == 'ari':
        if labels_true is None:
            raise Exception("Must provide ground truth labels for ARI")
        return [adjusted_rand_score(labels_true, labels)]
    elif metric == 'intra':
        sum = 0.
        for l in np.unique(labels):
            pts = data[labels == l]
            avg = pts.mean(axis=0)
            diff = np.linalg.norm(pts - avg)
            sum += diff
        return [sum]
    elif metric == 'connectedness':
        sum = 0.
        for l in np.unique(labels):
            idxs = labels == l
            dists = distance_vector[idxs][:, idxs]
            # not a single point in a cluster by itself
            if dists.shape[0] > 1:
                dists = np.divide(1., dists, out=np.zeros_like(dists), where=dists != 0)
                dists = np.minimum(dists, 10)
                np.fill_diagonal(dists, 0)
                sum += dists[dists > 0].sum() / dists.shape[0]  # .mean()
        return [sum / nlabels]
    else:
        raise Exception("invalid metric: {}".format(metric))

def write_ind_to_file(ind, run_num, results,datafile,data,toolbox):
    """
    Writes the attributes of an individual to file.

    :param run_num: the number of the current run
    :param ind: the individual
    :param results: a dictionary of results, titles to values
    """
    line_list = []
    # add constructed features to lines
    if REP is mt:
        for cf in [str(tree) for tree in ind]:
            line_list.append(cf + "\n")
    elif REP is not vt:
        raise Exception("Invalid representation")
    line_list.append("\n")
    fl = open("%d_ind.txt" % run_num, 'w')
    if REP is mt:
        fl.writelines(line_list)
    else:
        for i in ind:
            fl.write(str(i))
            fl.write("\n")
    fl.close()
    the_rep=0
    if REP is vt:
        the_rep=1
    output_change.change_output(str(run_num)+"_ind.txt",N_TREES,datafile+".data",run_num,the_rep)

def init_toolbox(toolbox, pset):
    """
    Initialises the toolbox with operators.
    :param toolbox: the toolbox to initialise
    :param pset: primitive set for evolution
    """
    REP.init_toolbox(toolbox, pset, N_TREES)
    toolbox.register("select", selElitistAndTournament, tournsize=7, elitism=ELITISM)

def init_stats():
    """
    Initialises a MultiStatistics object to capture data.
    :return: the MultiStatistics object
    """
    fitness_stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats = tools.MultiStatistics(fitness=fitness_stats)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    return stats

def final_evaluation(best, data, labels, num_classes, toolbox, print_output=True):
    """
    Performs a final performance evaluation on an individual.

    :param best: the individual to evaluate
    :param data: the dataset associated with the individual
    :param labels: the ground-truth labels of the dataset
    :param num_classes: the number of classes of the dataset
    :param toolbox: the evolutionary toolbox
    :param print_output: whether or not to print output
    :return: a dictionary of results, titles to values
    """
    return

rd = {}

def eval_wrapper(*args, **kwargs):
    return evaluate(*args, **kwargs, toolbox=rd['toolbox'], data=rd['data'], k=rd['num_classes'],metric=rd['metric'], maximise=rd['maximise'], distance_vector=rd['distance_vector'])

# copies data over from parent process
def init_data(rundata):
    global rd
    rd = rundata

def maingptree(datafile, run_num):
    print("maing tree NGEN",NGEN)
    print("maing tree SEED",SEED)
    random.seed(SEED)
    all_data = read_data("%s/%s.data" % (DATA_DIR, datafile))
    rd['data'] = all_data["data"]
    rd['labels'] = all_data["labels"]
    rd['num_classes'] = len(set(rd['labels']))
    print("%d classes found." % rd['num_classes'])
    rd['distance_vector'] = pairwise_distances(rd['data'])
    rd['num_instances'] = rd['data'].shape[0]
    rd['num_features'] = rd['data'].shape[1]
    rd['metric'] = METRIC
    rd['maximise'] = MAXIMISE
    pset = gp.PrimitiveSet("MAIN", rd['num_features'], prefix="f")
    pset.context["array"] = np.array
    REP.init_primitives(pset)
    weights = (1.0,) if MAXIMISE else (-1.,)
    creator.create("FitnessMax", base.Fitness, weights=weights)
    # set up toolbox
    toolbox = ParallelToolbox()  # base.Toolbox()
    init_toolbox(toolbox, pset)
    toolbox.register("evaluate", eval_wrapper)
    rd['toolbox'] = toolbox
    pop = toolbox.population(n=POP_SIZE)
    hof = tools.HallOfFame(1)
    if REP is vt:
        hof = tools.HallOfFame(N_TREES)
    stats = init_stats()
    with multiprocessing.Pool(initializer=init_data, initargs=[rd]) as pool:
        toolbox.map = pool.map
        pop, logbook = ea_simple_elitism.eaSimple(pop, toolbox, CXPB, MUTPB, ELITISM, NGEN, stats,
                                                  halloffame=hof, verbose=True)
    if REP is not vt:
        best = hof[0]
    else:
        best = []
        for i in range(N_TREES):
            if i<len(hof):
                best.append(hof[i])
    res = final_evaluation(best, rd['data'], rd['labels'], rd['num_classes'], toolbox)
    write_ind_to_file(best, run_num, res,datafile,rd['data'],toolbox)
    return pop, stats, hof

"""
[seed] [data file]
"""


if __name__ == "__main__":
    
    print("input your new data name for feature generation from pintos")
    #input_data_name ="feature_information"
    input_data_name= input()

    feature_maker = FeatureMaker()
    make_feature_file(feature_maker,input_data_name)

    print("")
    print("we get feature from pintos")
    print("")

    print("input how many generation you will do, NGEN")
    NGEN= input()
    NGEN= int(NGEN)
    print("main NGEN", NGEN)
    
    print("input how many Trees you will do, N_TREES")
    N_TREES= input()
    N_TREES=int(N_TREES)
    print("main N_TREES", N_TREES)

    print("input how many SEEDS you will do, SEED")
    SEED= input()
    SEED= int(SEED)
    print("main SEED", SEED)
    




    maingptree(input_data_name, SEED)

    print("==================  clustering ========================")

    print("input how many K klustering you will do, K")
    k= input()
    k= int(k)
    print("main K", k)
    

    cluster("result_"+str(SEED)+".txt", k, method='random', num_iter=10)




