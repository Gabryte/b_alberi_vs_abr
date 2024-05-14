import random

from Classi.Abr import Abr
from Classi.AbrNode import AbrNode
from Classi.BTree import BTree
from utilità_e_test.funzioni_di_supporto import find_median_index
from timeit import default_timer as timer
from matplotlib import pyplot as plt

def search_comparison_between_random_binary_tree_and_random_BTree(rand_binary_tree, rand_btree, elements):
    time_binary_tree = []
    time_b_tree = []
    x = []
    keys = []
    accum_precision = float(0)

    for i in range(0, elements):
        keys.append(random.randint(0,elements))
        rand_btree.BTreeInsert(keys[i])
        rand_binary_tree.tree_insert(AbrNode(keys[i]))

    for i in range(0, elements):
        max_searches = i
        key_to_search = []
        for j in range(0, max_searches):
            key_to_search.append(random.randint(0,2*elements))

        start = timer()
        for j in range(0, max_searches):
            rand_btree.BTreeSearch_no_tracking(rand_btree.root,key_to_search[j])
        end = timer()
        accum_precision = end - start
        accum = round(accum_precision, 8)
        time_b_tree.append(accum)


        start = timer()
        for j in range(0, max_searches):
            rand_binary_tree.tree_search(rand_binary_tree.root,key_to_search[j])
        end = timer()
        accum_precision = end - start
        accum = round(accum_precision, 8)
        time_binary_tree.append(accum)
        x.append(i)

    plt.plot(x, time_binary_tree, label="Random Binary Tree", color="Black")
    plt.plot(x, time_b_tree, label="Random BTree", color="Red")
    plt.xlabel('Number of searches')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

def insert_comparison_between_random_binary_tree_and_random_BTree(elements,t_param):
    time_binary_tree = []
    time_b_tree = []
    x = []


    for i in range(0, elements):

        max_inserts = i
        key_to_insert = []
        for j in range(0, max_inserts):
            key_to_insert.append(random.randint(0,2*elements))

        rand_btree = BTree(t_param)
        start = timer()
        for j in range(0, max_inserts):
            rand_btree.BTreeInsert(key_to_insert[j])
        end = timer()

        accum_precision = end - start
        accum = round(accum_precision, 8)

        time_b_tree.append(accum)

        rand_binary_tree = Abr()
        start = timer()
        for j in range(0, max_inserts):
            rand_binary_tree.tree_insert(AbrNode(key_to_insert[j]))
        end = timer()

        accum_precision = end - start
        accum = round(accum_precision, 8)
        time_binary_tree.append(accum)

        x.append(i)

    plt.plot(x, time_binary_tree, label="Random Binary Tree", color="Black")
    plt.plot(x, time_b_tree, label="Random BTree", color="Red")
    plt.xlabel('Number of insertions')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

def insert_comparison_between_worst_binary_tree_and_worst_BTree(elements, t_param):
    time_binary_tree = []
    time_b_tree = []
    x = []


    for i in range(0, elements):

        max_insertion = i
        worst_btree = BTree(t_param)
        start = timer()
        for j in range(0, max_insertion):
            worst_btree.BTreeInsert(j)
        end = timer()
        accum_precision = end - start
        accum = round(accum_precision, 8)
        time_b_tree.append(accum)

        worst_binary_tree = Abr()
        start = timer()
        for j in range(0, max_insertion):
            worst_binary_tree.tree_insert(AbrNode(j))
        end = timer()
        accum_precision = end - start
        accum = round(accum_precision, 8)
        time_binary_tree.append(accum)
        x.append(i)

    plt.plot(x, time_binary_tree, label="Worst Binary Tree", color="Black")
    plt.plot(x, time_b_tree, label="Worst binary applied to Btree", color="Red")
    plt.xlabel('Number of insertions')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

def search_comparison_between_worst_binary_tree_and_worst_BTree(worst_binary_tree,worst_btree,elements):
    time_binary_tree = []
    time_b_tree = []
    x = []
    accum_precision = float(0)

    for i in range(0, elements):
        worst_btree.BTreeInsert(i)
        worst_binary_tree.tree_insert(AbrNode(i))

    for i in range(0, elements):
        max_searches = i
        keys_to_search = []

        for j in range(0, max_searches):
            keys_to_search.append(random.randint(0,2*elements))


        start = timer()
        for j in range(0, max_searches):
            worst_btree.BTreeSearch_no_tracking(worst_btree.root,keys_to_search[j])
        end = timer()
        accum_precision = end - start
        accum = round(accum_precision, 8)
        time_b_tree.append(accum)


        start = timer()
        for j in range(0, max_searches):
            worst_binary_tree.tree_search(worst_binary_tree.root,keys_to_search[j])
        end = timer()
        accum_precision = end - start
        accum = round(accum_precision, 8)
        time_binary_tree.append(accum)
        x.append(i)

    plt.plot(x, time_binary_tree, label="Worst Binary Tree", color="Black")
    plt.plot(x, time_b_tree, label="Worst binary applied to Btree", color="Red")
    plt.xlabel('Number of searches')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

def search_comparison_between_worst_binary_tree_and_random_b_tree(worst_binary_tree,random_btree,elements):
    time_binary_tree = []
    time_b_tree = []
    x = []
    accum_precision = float(0)

    for i in range(0, elements):
        random_btree.BTreeInsert(random.randint(0,elements))
        worst_binary_tree.tree_insert(AbrNode(i))

    for i in range(0, elements):
        max_searches = i
        keys_to_search = []
        for j in range(0, max_searches):
             keys_to_search.append(random.randint(0,2*elements))


        start = timer()
        for j in range(0, max_searches):
            random_btree.BTreeSearch_no_tracking(random_btree.root,keys_to_search[j])
        end = timer()
        accum_precision = end - start
        accum = round(accum_precision, 8)
        time_b_tree.append(accum)


        start = timer()
        for j in range(0, max_searches):
            worst_binary_tree.tree_search(worst_binary_tree.root,keys_to_search[j])
        end = timer()
        accum_precision = end - start
        accum = round(accum_precision, 8)
        time_binary_tree.append(accum)
        x.append(i)

    plt.plot(x, time_binary_tree, label="Worst Binary Tree", color="Black")
    plt.plot(x, time_b_tree, label="Random BTree", color="Red")
    plt.xlabel('Number of searches')
    plt.ylabel('Time')
    plt.legend()
    plt.show()
