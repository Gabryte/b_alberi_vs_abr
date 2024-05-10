from Classi.Abr import Abr
import sys
from utilità_e_test.abr_tests import random_case_binary_tree_insertion_and_search_tests, worst_case_binary_search_tree_insertion_and_search_tests
from utilità_e_test.btree_tests import *
sys.setrecursionlimit(999999999)




elements = 1000
searches = 40
graph_x_length = 20
graph_y_length = 20
childPerNode = 5



elements = get_integer_input("Insert number of elements that will be present into the trees (btree and binarytree ps.much better if it is >= 15): ", min_value=15)
searches = get_integer_input("Insert number of searches that will be performed on the trees (btree and binarytree ps.much better if it is >= 15): ", min_value=15)
childPerNode = get_integer_input("Insert number of children per node that will be present into the BTree (ps.much better if it is >= 2): ", min_value=2)
graph_x_length = get_integer_input("Insert the x length of the graph (ps.much better if it is >= 10 and <=30): ", min_value=10, max_value=30)
graph_y_length = get_integer_input("Insert the y length of the graph (ps.much better if it is >= 10 and <=30): ", min_value=10, max_value=30)


rand_binary_tree = Abr()
rand_btree = BTree(childPerNode)
worst_binary_tree = Abr()

random_case_binary_tree_insertion_and_search_tests(rand_binary_tree, elements, graph_x_length, graph_y_length, searches)
worst_case_binary_search_tree_insertion_and_search_tests(worst_binary_tree, elements, graph_x_length, graph_y_length, searches)
random_case_btree_insert_and_search_tests(rand_btree, elements, graph_x_length, graph_y_length, searches)
worst_case_binary_tree_applied_to_btree_insert_and_search_test(rand_btree, elements, graph_x_length, graph_y_length, searches)