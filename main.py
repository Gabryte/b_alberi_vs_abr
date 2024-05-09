from Classi.Abr import Abr
import sys
from utilità_e_test.tests import random_case_binary_tree_insertion_and_search_tests, worst_case_binary_search_tree_insertion_and_search_tests

sys.setrecursionlimit(100000)

rand_binary_tree = Abr()
worst_binary_tree = Abr()

elements = 2000
searches = 4000
graph_x_length = 20
graph_y_length = 20

random_case_binary_tree_insertion_and_search_tests(rand_binary_tree, elements, graph_x_length, graph_y_length, searches)
worst_case_binary_search_tree_insertion_and_search_tests(worst_binary_tree, elements, graph_x_length, graph_y_length, searches)