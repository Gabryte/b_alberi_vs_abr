
import random
from timeit import default_timer as timer
from matplotlib import pyplot as plt
from Classi.AbrNode import AbrNode
from utilità_e_test.funzioni_di_supporto import *
import numpy as np

def worst_case_binary_search_tree_insertion_and_search_tests(worst_binary_search_tree,number_of_elements,subplots_dim_x,subplots_dim_y,number_of_searches):
    n_downward_tree_hop_number = np.zeros((1,number_of_elements))
    matrix_for_plotting = np.zeros((2, number_of_elements))
    accum_precision = float(0)

    'Inizializzazione caso peggiore albero binario di ricerca'
    i = random.randint(0, 9)
    call_counter = 0
    while call_counter < number_of_elements:
        worst_node = AbrNode(i)
        start = timer()
        hop_counter = worst_binary_search_tree.tree_insert(worst_node)
        end = timer()
        accum_precision = accum_precision + end - start
        accum = round(accum_precision, 4)
        matrix_for_plotting[0, call_counter] = accum
        matrix_for_plotting[1, call_counter] = call_counter + 1
        i = i + 1
        n_downward_tree_hop_number[0, call_counter] = hop_counter
        call_counter = call_counter + 1

    fig, ax = plt.subplots(2, 2, figsize=(subplots_dim_x, subplots_dim_y))

    ax[0][0].plot(matrix_for_plotting[1],matrix_for_plotting[0], label="Performance", color="Black")
    ax[0][0].grid(linestyle=':')
    ax[0][0].legend(loc='upper left')
    ax[0][0].set_title('Worst ABR Insertion Performance')
    ax[0][0].set_xlabel('Inserted Elements')
    ax[0][0].set_ylabel('Time')

    ax[0][1].plot(matrix_for_plotting[1], n_downward_tree_hop_number[0], label="Complexity of Insertion", color="Black")
    ax[0][1].grid(linestyle=':')
    ax[0][1].legend(loc='upper left')
    ax[0][1].set_title('Worst ABR Insertion Complexity')
    ax[0][1].set_xlabel('Inserted Elements')
    ax[0][1].set_ylabel('Downward Hops per inserted element')

    # Misurazione numero di hops in discesa durante un certo numero di ricerche
    downward_search_hops, x_searches = binary_search_test(number_of_elements, number_of_searches,worst_binary_search_tree)
    average_y_search = running_average(math.ceil(len(x_searches[0]) * 0.15), downward_search_hops)
    downward_subgraph, upward_subgraph = on_average_subgraph_splitter(average_y_search, downward_search_hops)

    while (len(x_searches[0]) < len(average_y_search)):
        average_y_search.pop(-1)

    ax[1][0].plot(x_searches[0], downward_search_hops[0], label='Hops per search', color="black")
    ax[1][0].plot(x_searches[0], average_y_search, label='Running average', color="r")
    ax[1][0].fill_between(x_searches[0], average_y_search, upward_subgraph[0], color='blue', alpha=0.3)
    ax[1][0].fill_between(x_searches[0], average_y_search, downward_search_hops[0], color='r', alpha=0.3)
    ax[1][0].legend(loc='upper left')
    ax[1][0].grid(linestyle=':')
    ax[1][0].set_title('Worst ABR Search Performance')
    ax[1][0].set_xlabel('Number of searches')
    ax[1][0].set_ylabel('Downward hops')

    # Leaf structure
    keys , hop_counter = worst_binary_search_tree.find_leafs(worst_binary_search_tree.get_root())
    dim_depth = len(keys)

    depth = np.array((keys, hop_counter))

    balanced_line, perfect_balanced_height = full_balanced_binary_tree(dim_depth, number_of_elements)

    lower_graph, upper_graph = leafs_graph_splitter(depth, dim_depth, perfect_balanced_height)

    avg_window_size = math.ceil(depth[0]*0.15)
    average_leaf_structure = average_leaf_structure_graph(avg_window_size,depth)

    ax[1][1].plot(depth[0], depth[1], label="Hops per leaf", color="black", linestyle='solid')
    ax[1][1].plot(depth[0], balanced_line[0], label="Equivalent full balanced tree", color="Black")
    ax[1][1].fill_between(depth[0], perfect_balanced_height, upper_graph[0], color='blue', alpha=0.1)
    ax[1][1].fill_between(depth[0], perfect_balanced_height, lower_graph[0], color='r', alpha=0.1)
    ax[1][1].fill_between(depth[0], perfect_balanced_height, average_leaf_structure, color='Green', alpha=0.1)
    ax[1][1].legend(loc='upper left')
    ax[1][1].grid(linestyle=':')
    ax[1][1].set_title('Worst Abr Leaf Structure')
    ax[1][1].set_xlabel('Leaf key')
    ax[1][1].set_ylabel('Downward hops')

    plt.show()


def random_case_binary_tree_insertion_and_search_tests(rand_binary_search_tree,number_of_elements,subplots_dim_x,subplots_dim_y,number_of_searches):
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

    ax[0][0].plot(matrix_for_plotting[1],matrix_for_plotting[0], label='Performance', color="r")
    ax[0][0].set_title('Rand ABR Insertion Performance')
    ax[0][0].set_xlabel('Inserted Elements')
    ax[0][0].set_ylabel('Time')
    ax[0][0].grid(linestyle=':')
    ax[0][0].legend(loc='upper left')

    # calcolo media mobile con finestra di osservazione
    avg_window_size = math.ceil(len(matrix_for_plotting[1]) * 0.15)
    average_y = running_average(avg_window_size, n_downward_tree_hop_number)

    while(len(matrix_for_plotting[1]) < len(average_y)):
        average_y.pop(-1)

    # n_downward_tree_hop_number.

    ax[0][1].plot(matrix_for_plotting[1], n_downward_tree_hop_number[0], label='Complexity of insertion',color="black")
    ax[0][1].plot(matrix_for_plotting[1], average_y, label='Running average', color="r")
    ax[0][1].fill_between(matrix_for_plotting[1], 0, average_y, color='r', alpha=0.15)
    ax[0][1].grid(linestyle=':')
    ax[0][1].legend(loc='upper left')
    ax[0][1].set_title('Rand ABR Insertion Complexity')
    ax[0][1].set_xlabel('Inserted Elements')
    ax[0][1].set_ylabel('Downward Hops per inserted element')



    # Misurazione numero di hops in discesa durante un certo numero di ricerche
    downward_search_hops, x_searches = binary_search_test(number_of_elements, number_of_searches,rand_binary_search_tree)

    average_y_search = running_average(math.ceil(len(x_searches[0])*0.15), downward_search_hops)

    downward_subgraph, upward_subgraph = on_average_subgraph_splitter(average_y_search, downward_search_hops)

    while (len(x_searches[0]) < len(average_y_search)):
        average_y_search.pop(-1)


    ax[1][0].plot(x_searches[0], downward_search_hops[0], label='Hops per search', color="black")
    ax[1][0].plot(x_searches[0], average_y_search, label='Running average', color="r")
    ax[1][0].fill_between(x_searches[0], average_y_search, upward_subgraph[0], color='blue', alpha=0.3)
    ax[1][0].fill_between(x_searches[0], average_y_search, downward_search_hops[0], color='r', alpha=0.3)
    ax[1][0].legend(loc='upper left')
    ax[1][0].grid(linestyle=':')
    ax[1][0].set_title('Rand ABR Search Performance')
    ax[1][0].set_xlabel('Number of searches')
    ax[1][0].set_ylabel('Downward hops')


    keys , hop_counter = rand_binary_search_tree.find_leafs(rand_binary_search_tree.get_root())


    depth = np.array((keys,hop_counter))

    dim_depth = len(hop_counter)

    balanced_line, perfect_balanced_height = full_balanced_binary_tree(dim_depth, number_of_elements)

    lower_graph, upper_graph = leafs_graph_splitter(depth, dim_depth, perfect_balanced_height)

    avg_window_size = math.ceil(len(depth[0])*0.15)
    average_leaf_structure = average_leaf_structure_graph(avg_window_size, depth)

    while(len(depth[0]) < len(average_leaf_structure)):
        average_leaf_structure.pop(-1)


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



def binary_search_test(number_of_elements, number_of_searches, rand_binary_search_tree):
    downward_search_hops = np.zeros((1, number_of_searches))
    x_searches = np.zeros((2, number_of_searches))
    for i in range(0, number_of_searches):
        result = rand_binary_search_tree.iterative_tree_search(rand_binary_search_tree.get_root(),random.randint(0,number_of_elements))
        x_searches[0, i] = i
        downward_search_hops[0, i] = result[1]
    return downward_search_hops, x_searches





