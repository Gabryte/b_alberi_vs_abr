
import random
from timeit import default_timer as timer
from matplotlib import pyplot as plt
from Classi.BTreeNode import BTreeNode
from Classi.BTree import BTree
from utilità_e_test.funzioni_di_supporto import *
import numpy as np



def random_case_btree_insert_and_search_tests(random_btree,elements,subplots_dim_x,subplots_dim_y,number_of_searches):
    matrix_for_plotting = np.zeros((2, elements))
    reads = np.zeros((1, elements))
    accum_precision = float(0)
    'test di inserimento in BTree'
    for i in range(0,elements):
        start = timer()
        reads_counter = random_btree.BTreeInsert(random.randint(0, elements))
        end = timer()
        accum_precision = accum_precision + end - start
        accum = round(accum_precision, 4)
        matrix_for_plotting[0, i] = accum
        matrix_for_plotting[1, i] = i + 1
        reads[0, i] = reads_counter

    fig, ax = plt.subplots(2, 2, figsize=(subplots_dim_x, subplots_dim_y))
    #performance insertion of random elements
    ax[0][0].plot(matrix_for_plotting[0], matrix_for_plotting[1], label="Performance", color="Black")
    ax[0][0].grid(linestyle=':')
    ax[0][0].legend(loc='upper left')
    ax[0][0].set_title('Random BTree Insertion Performance')
    ax[0][0].set_xlabel('Time')
    ax[0][0].set_ylabel('Inserted Elements')

    # calcolo media mobile con finestra di osservazione
    avg_window_size = math.ceil(len(matrix_for_plotting[1]) * 0.15)
    average_y = running_average(avg_window_size, reads)

    ax[0][1].plot(matrix_for_plotting[1], reads[0], label="Complexity of Insertion", color="Black")
    ax[0][1].plot(matrix_for_plotting[1], average_y, label='Running average', color="r")
    ax[0][1].fill_between(matrix_for_plotting[1], 0, average_y, color='r', alpha=0.1)
    ax[0][1].grid(linestyle=':')
    ax[0][1].legend(loc='upper left')
    ax[0][1].set_title('Random BTree Insertion Complexity')
    ax[0][1].set_xlabel('Inserted Elements')
    ax[0][1].set_ylabel('Reads per inserted element')

    # Misurazione numero di letture durante un certo numero di ricerche
    reads, x_searches = btree_test(elements, number_of_searches, random_btree)

    average_y_search = running_average(math.ceil(len(x_searches[0]) * 0.15), reads)

    reads_subgraph, upward_subgraph = on_average_subgraph_splitter(average_y_search, reads)

    ax[1][0].plot(x_searches[0], reads[0], label='Hops per search', color="black")
    ax[1][0].plot(x_searches[0], average_y_search, label='Running average', color="r")
    ax[1][0].fill_between(x_searches[0], average_y_search, upward_subgraph[0], color='blue', alpha=0.3)
    ax[1][0].fill_between(x_searches[0], average_y_search, reads[0], color='r', alpha=0.3)
    ax[1][0].legend(loc='upper left')
    ax[1][0].grid(linestyle=':')
    ax[1][0].set_title('Rand Btree Search Performance')
    ax[1][0].set_xlabel('Number of searches')
    ax[1][0].set_ylabel('Downward hops')

    leaf_depths = random_btree.find_leaf_depths(random_btree.get_root())

    # Estrai le chiavi dei nodi e le profondità in due liste separate
    keys = [node.key for node, depth in leaf_depths]
    hop_counter = [depth for node, depth in leaf_depths]

    # Crea un array numpy con le chiavi e le profondità
    depth = np.array((keys, hop_counter))

    dim_depth = len(hop_counter)

    balanced_line, perfect_balanced_height = full_balanced_binary_tree(dim_depth, elements)

    lower_graph, upper_graph = leafs_graph_splitter(depth, dim_depth, perfect_balanced_height)

    avg_window_size = math.ceil(len(depth[0]) * 0.15)
    average_leaf_structure = average_leaf_structure_graph(avg_window_size, depth)

    ax[1][1].plot(depth[0], depth[1], label="Hops per leaf", color="black", linestyle='dashdot')
    ax[1][1].plot(depth[0], balanced_line[0], label="Equivalent perfect balanced tree", color="Black")
    ax[1][1].plot(depth[0], average_leaf_structure, label="Running Average", color="r")
    ax[1][1].fill_between(depth[0], perfect_balanced_height, upper_graph[0], color='blue', alpha=0.1)
    ax[1][1].fill_between(depth[0], perfect_balanced_height, lower_graph[0], color='r', alpha=0.1)
    ax[1][1].fill_between(depth[0], perfect_balanced_height, average_leaf_structure, color='Green', alpha=0.1)
    ax[1][1].legend(loc='upper left')
    ax[1][1].grid(linestyle=':')
    ax[1][1].set_title('Rand ABR Leaf Structure')
    ax[1][1].set_xlabel('Leaf key')
    ax[1][1].set_ylabel('Downward hops')

    plt.show()


def btree_test(number_of_elements, number_of_searches, rand_btree):

    reads = np.zeros((1, number_of_searches))
    x_searches = np.zeros((2, number_of_searches))

    for i in range(0, number_of_searches):
        rand_btree.BTreeSearch(rand_btree.get_root(), random.randint(0, number_of_elements))
        x_searches[0, i] = i
        reads[0, i] = rand_btree.get_search_hops()
        rand_btree.set_search_hops(0)

    return reads, x_searches





