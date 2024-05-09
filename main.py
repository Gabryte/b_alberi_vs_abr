from Classi.Abr import Abr
import sys
from utilità_e_test.abr_tests import random_case_binary_tree_insertion_and_search_tests, worst_case_binary_search_tree_insertion_and_search_tests
from utilità_e_test.btree_tests import *
sys.setrecursionlimit(100000)


childPerNode = 4
rand_binary_tree = Abr()
rand_btree = BTree(childPerNode)
worst_binary_tree = Abr()

elements = 500
searches = 400
graph_x_length = 20
graph_y_length = 20

random_case_binary_tree_insertion_and_search_tests(rand_binary_tree, elements, graph_x_length, graph_y_length, searches)
worst_case_binary_search_tree_insertion_and_search_tests(worst_binary_tree, elements, graph_x_length, graph_y_length, searches)
random_case_btree_insert_and_search_tests(rand_btree, elements, graph_x_length, graph_y_length, searches)