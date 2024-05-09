import numpy as np
import math
def average_leaf_structure_graph(average_window_size, depth):
    average_leaf_structure = []
    tuned_window = average_window_size - math.ceil(average_window_size / 3)
    for i in range(len(depth[1]) - tuned_window + 1):  # calcolo media mobile per struttura foglie
        average_leaf_structure.append(np.mean(depth[1][i:i + tuned_window]))
    for i in range(tuned_window - 1):
        average_leaf_structure.insert(0, np.nan)
    return average_leaf_structure


def running_average(average_window_size,measures_in_hops):
    average_y = []
    tuned_window = average_window_size - math.ceil(average_window_size / 3)
    for i in range(len(measures_in_hops[0]) - tuned_window + 1):
        average_y.append(np.mean(measures_in_hops[0][i:i + tuned_window]))
    for i in range(tuned_window - 1):
        average_y.insert(0, np.nan)
    return average_y

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

def equivalent_full_balanced_binary_tree(dim_depth, number_of_elements):
    perfect_balanced_height = -1 * (math.ceil(math.log2(number_of_elements + 1)))
    # coordinate per albero binario equivalente ma idealmente bilanciato
    balanced_line = np.zeros((1, dim_depth))
    for i in range(0, dim_depth):
        balanced_line[0, i] = perfect_balanced_height
    return balanced_line, perfect_balanced_height