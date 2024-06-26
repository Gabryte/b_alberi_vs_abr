from Classi.Abr import Abr
import sys
import webbrowser
from utilità_e_test.abr_tests import random_case_binary_tree_insertion_and_search_tests, worst_case_binary_search_tree_insertion_and_search_tests
from utilità_e_test.btree_tests import *
from utilità_e_test.comparison_tests import search_comparison_between_random_binary_tree_and_random_BTree, \
    insert_comparison_between_random_binary_tree_and_random_BTree, \
    insert_comparison_between_worst_binary_tree_and_worst_BTree, \
    search_comparison_between_worst_binary_tree_and_worst_BTree, \
    search_comparison_between_worst_binary_tree_and_random_b_tree

sys.setrecursionlimit(999999999)

elements = 1
searches = 1
graph_x_length = 20
graph_y_length = 20
t_param = 2
number_of_searches_comparison_test = 3000
number_of_insertions_comparison_test = 3000



elements = get_integer_input("Insert number of elements that will be present into the trees (btree and binarytree ps.much better if it is >= 25): ", min_value=25)
searches = get_integer_input("Insert number of searches that will be performed on the trees (btree and binarytree ps.much better if it is >= 25): ", min_value=25)
t_parameter = get_integer_input("Insert param t of the B-Tree, remember that if t=2 you have 1<=children<=4 (ps.much better if it t is >= 2): ", min_value=2)
graph_x_length = get_integer_input("Insert the x length of the graph (ps.much better if it is >= 5 and <=30): ", min_value=10, max_value=30)
graph_y_length = get_integer_input("Insert the y length of the graph (ps.much better if it is >= 5 and <=30): ", min_value=10, max_value=30)
number_of_searches_comparison_test = get_integer_input("Insert the number of searches that will be performed for the comparison test (ps.much better if it is >= 15): ", min_value=15)
number_of_insertions_comparison_test = get_integer_input("Insert the number of insertions that will be performed for the comparison test (ps.much better if it is >= 15): ", min_value=15)


rand_binary_tree = Abr()
rand_btree = BTree(t_param)
worst_binary_tree = Abr()

random_case_binary_tree_insertion_and_search_tests(rand_binary_tree, elements, graph_x_length, graph_y_length, searches)

worst_case_binary_search_tree_insertion_and_search_tests(worst_binary_tree, elements, graph_x_length, graph_y_length, searches)

random_case_btree_insert_and_search_tests(rand_btree, elements, graph_x_length, graph_y_length, searches)

rand_btree = BTree(t_param)
worst_case_binary_tree_applied_to_btree_insert_and_search_test(rand_btree, elements, graph_x_length, graph_y_length, searches)

rand_binary_tree = Abr()
rand_btree = BTree(t_param)
search_comparison_between_random_binary_tree_and_random_BTree(rand_binary_tree, rand_btree, number_of_searches_comparison_test)

worst_binary_tree = Abr()
worst_btree = BTree(t_param)
search_comparison_between_worst_binary_tree_and_worst_BTree(worst_binary_tree, worst_btree, number_of_searches_comparison_test)

insert_comparison_between_random_binary_tree_and_random_BTree(number_of_insertions_comparison_test, t_param)

insert_comparison_between_worst_binary_tree_and_worst_BTree(number_of_insertions_comparison_test, t_param)

rand_btree = BTree(t_param)
worst_binary_tree = Abr()
search_comparison_between_worst_binary_tree_and_random_b_tree(worst_binary_tree, rand_btree, number_of_searches_comparison_test)

webbrowser.open("Random_Case_Binary_Insertion_Search.html")
webbrowser.open("Random_Case_BTree_Insertion_Search.html")
webbrowser.open("Worst_Case_Binary_Insertion_Search.html")
webbrowser.open("Worst_Case_Applied_BTree_Insertion_Search.html")
webbrowser.open("Insert_comparison_RAND_RAND.html")
webbrowser.open("Insert_comparison_WORST_WORST.html")
webbrowser.open("Search_Comparison_RAND_RAND.html")
webbrowser.open("Search_comparison_WORST_WORST.html")
webbrowser.open("Search_comparison_WORST_RAND.html")