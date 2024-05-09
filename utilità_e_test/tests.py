import math
import random
from timeit import default_timer as timer
from matplotlib import pyplot as plt
from Classi.Abr import Abr
from Classi.AbrNode import AbrNode
from utilità_e_test.funzioni_di_supporto import running_average
import numpy as np

def random_case_binary_tree_insertion_and_search_tests(rand_binary_search_tree,number_of_elements,average_window_size,subplots_dim_x,subplots_dim_y,display_tree_dim_x,display_tree_dim_y,number_of_searches):
    matrix_for_plotting = np.zeros((2, number_of_elements))
    n_downward_tree_hop_number = np.zeros((1,number_of_elements))
    accum_precision = float(0)

    'Inizializzazione inserimenti caso randomico albero binario di ricerca'
    for i in range(0, number_of_elements):
        rand_node = AbrNode(random.randint(0,number_of_elements))
        start = timer()
        hop_counter = rand_binary_search_tree.tree_insert(rand_node)
        end = timer()
        accum_precision = accum_precision + end - start
        accum = round(accum_precision, 4)
        matrix_for_plotting[0,i] = accum
        matrix_for_plotting[1,i] = i + 1
        n_downward_tree_hop_number[0, i] = hop_counter

    fig, ax = plt.subplots(2, 2, figsize=(subplots_dim_x, subplots_dim_y))

    ax[0][0].plot(matrix_for_plotting[0], matrix_for_plotting[1], label='Performance', color="r")
    ax[0][0].set_title('Rand ABR Insertion Performance')
    ax[0][0].set_xlabel('Time')
    ax[0][0].set_ylabel('Inserted Elements')
    ax[0][0].grid(linestyle=':')
    ax[0][0].legend(loc='upper left')

    # calcolo media mobile con finestra di osservazione
    average_y = running_average(average_window_size, n_downward_tree_hop_number)

    # n_downward_tree_hop_number.

    ax[0][1].plot(matrix_for_plotting[1], n_downward_tree_hop_number[0], label='Complexity of insertion',color="black")
    ax[0][1].plot(matrix_for_plotting[1], average_y, label='Running average', color="r")
    ax[0][1].fill_between(matrix_for_plotting[1], 0, average_y, color='r', alpha=0.1)
    ax[0][1].grid(linestyle=':')
    ax[0][1].legend(loc='upper left')
    ax[0][1].set_title('Rand ABR Insertion Complexity')
    ax[0][1].set_xlabel('Inserted Elements')
    ax[0][1].set_ylabel('Downward Hops per inserted element')

    # Misurazione numero di hops in discesa durante un certo numero di ricerche
    downward_search_hops, x_searches = binary_search_test(number_of_elements, number_of_searches,rand_binary_search_tree)

    average_y_search = running_average(average_window_size, downward_search_hops)  # hops medi per la ricerca

    downward_subgraph, upward_subgraph = on_average_subgraph_splitter(average_y_search,downward_search_hops)  # separa la parte superiore dalla parte inferiore del grafico

    ax[1][0].plot(x_searches[0], downward_search_hops[0], label='Hops per search', color="black")
    ax[1][0].plot(x_searches[0], average_y_search, label='Running average', color="r")
    ax[1][0].fill_between(x_searches[0], average_y_search, upward_subgraph[0], color='blue', alpha=0.3)
    ax[1][0].fill_between(x_searches[0], average_y_search, downward_subgraph[0], color='r', alpha=0.3)
    ax[1][0].legend(loc='upper left')
    ax[1][0].grid(linestyle=':')
    ax[1][0].set_title('Rand ABR Search Performance')
    ax[1][0].set_xlabel('Number of searches')
    ax[1][0].set_ylabel('Downward hops')

    depth = rand_binary_search_tree.find_leafs(rand_binary_search_tree.get_root(), number_of_elements)

    dim_depth = len(depth[1])

    balanced_line, perfect_balanced_height = equivalent_full_balanced_binary_tree(dim_depth, number_of_elements)

    lower_graph, upper_graph = leafs_graph_splitter(depth, dim_depth, perfect_balanced_height)

    average_leaf_structure = average_leaf_structure_graph(average_window_size, depth)

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


def equivalent_full_balanced_binary_tree(dim_depth, number_of_elements):
    perfect_balanced_height = -1 * (math.ceil(math.log2(number_of_elements + 1)))
    # coordinate per albero binario equivalente ma idealmente bilanciato
    balanced_line = np.zeros((1, dim_depth))
    for i in range(0, dim_depth):
        balanced_line[0, i] = perfect_balanced_height
    return balanced_line, perfect_balanced_height

def binary_search_test(number_of_elements, number_of_searches, rand_binary_search_tree):
    downward_search_hops = np.zeros((1, number_of_searches))
    x_searches = np.zeros((2, number_of_searches))
    for i in range(0, number_of_searches):
        result = rand_binary_search_tree.iterative_tree_search(rand_binary_search_tree.get_root(),random.randint(0, 2 * number_of_elements))
        x_searches[0, i] = i
        downward_search_hops[0, i] = result[1]
    return downward_search_hops, x_searches

def on_average_subgraph_splitter(average_y, downward_hops):
    upward_subgraph = np.zeros((1, len(downward_hops[0])))
    downward_subgraph = np.zeros((1, len(downward_hops[0])))
    for i in range(0, len(downward_hops[0])):
        if downward_hops[0, i] > average_y[i]:
            upward_subgraph[0, i] = downward_hops[0, i]
            downward_subgraph[0, i] = average_y[i]
        elif downward_hops[0, i] < average_y[i]:
            upward_subgraph[0, i] = average_y[i]
            downward_subgraph[0, i] = downward_hops[0, i]
        else:
            upward_subgraph[0, i] = average_y[i]
            downward_subgraph[0, i] = average_y[i]
    return downward_subgraph, upward_subgraph

def leafs_graph_splitter(depth, dim_depth, perfect_full_balanced_height):
    lower_graph = np.zeros((1, dim_depth))
    upper_graph = np.zeros((1, dim_depth))
    # minor_length = 0
    for i in range(0, dim_depth):  # suddivisione sezione superiore ed inferiore alla retta del bilanciamento
        if depth[1, i] < perfect_full_balanced_height:
            # minor_length+=1
            lower_graph[0, i] = depth[1, i]
            upper_graph[0, i] = perfect_full_balanced_height
        elif depth[1, i] > perfect_full_balanced_height:
            lower_graph[0, i] = perfect_full_balanced_height
            upper_graph[0, i] = depth[1, i]
        else:
            lower_graph[0, i] = perfect_full_balanced_height
            upper_graph[0, i] = perfect_full_balanced_height
    return lower_graph, upper_graph

def average_leaf_structure_graph(average_window_size, depth):
    average_leaf_structure = []
    tuned_window = average_window_size - math.ceil(average_window_size / 3)
    for i in range(len(depth[1]) - tuned_window + 1):  # calcolo media mobile per struttura foglie
        average_leaf_structure.append(np.mean(depth[1][i:i + tuned_window]))
    for i in range(tuned_window - 1):
        average_leaf_structure.insert(0, np.nan)
    return average_leaf_structure