import math
import numpy as np

from Classi.AbrNode import AbrNode

class Abr:
    'Classe base di un albero binario di ricerca'

    def __init__(self):
        self.root = None

    def set_root(self,key):
        self.root = AbrNode(key)

    def inorder_tree_walk(self,node):
        if node is not None:
            self.inorder_tree_walk(node.get_left())
            print(f"{node.get_key()}", end=" ")
            self.inorder_tree_walk(node.get_right())

    def postorder_tree_walk(self,node):
        if node is not None:
            self.inorder_tree_walk(node.get_left())
            self.inorder_tree_walk(node.get_right())
            print(f"{node.get_key()}", end=" ")

    def preorder_tree_walk(self,node):
        if node is not None:
            print(f"{node.get_key()}", end=" ")
            self.inorder_tree_walk(node.get_left())
            self.inorder_tree_walk(node.get_right())

    def tree_search(self,node,key):
            if node is None or key==node.get_key():
                return node
            if key < node.get_key():
                return self.tree_search(node.get_left(),key)
            else:
                return self.tree_search(node.get_right(),key)

    def iterative_tree_search(self,node,key):
        hops=0
        result = []
        while node is not None and key != node.get_key():
            if key < node.get_key():
                node = node.get_left()
                hops+=1
            else:
                node = node.get_right()
                hops+=1
        result.append(node)
        result.append(hops)
        return result

    def tree_minimum(self,node):
        while node.get_left() is not None:
            node = node.get_left()
        return node

    def tree_maximum(self,node):
        while node.get_right() is not None:
            node = node.get_right()
        return node


    def tree_successor(self,node):
        if node.get_right() is not None:
            return self.tree_minimum(node.get_right())
        y = node.get_p()
        while y is not None and node == y.get_right():
            node = y
            y = y.get_p()
        return y

    def tree_predecessor(self,node):
        if node.get_left() is not None:
            return self.tree_maximum(node.get_left())
        y = node.get_p()
        while y is not None and node == y.get_left():
            node = y
            y = y.get_p()
        return y

    def tree_insert(self,node):
        y = None
        x = self.root
        hop = 2
        while x is not None:
            y = x
            if node.get_key() < x.get_key():
                x = x.get_left()
            else:
                x = x.get_right()
            hop = hop + 2
        node.set_parent(y)
        if y is None:
            self.root = node
            hop = hop + 1
        elif node.get_key() < y.get_key():
            y.set_left_child(node)
        else:
            y.set_right_child(node)
        return hop

    def transplant(self, u, v):
        if u.get_p() is None:
            self.root = v
        elif u == u.get_p().get_left():
            u.get_p().set_left_child(v)
        else:
            u.get_p().set_right_child(v)
        if v is not None:
            v.set_parent(u.get_p())

    def tree_delete(self, node):
        'caso 1 e 2 in cui il figlio destro o sinistro è vuoto sostituiamo il nodo con ciò che è presente come figlio opposto'
        '(potrebbe essere nil implementando così anche la casistica in cui il nodo da elidere non abbia figli)'
        if node.get_left() is None:
            self.transplant(node,node.get_right())
        elif node.get_right() is None:
            self.transplant(node,node.get_left())
        else:
            y = self.tree_minimum(node.get_right())
            'caso 3 ci riconduciamo alla casistica in cui il successore è figlio destro del nodo da elidere nel caso in cui non lo fosse'
            if node != y.get_p():
                self.transplant(y,y.get_right())
                y.set_right_child(node.get_right())
                y.get_right().set_parent(y)
                'casistica in cui il successore (da rimpiazzare col nodo da elidere) è direttamente figlio destro del nodo da elidere'
            self.transplant(node,y)
            y.set_left_child(node.get_left())
            y.get_left().set_parent(y)

    def PT(self,node):
        if node is not None:
            print(f"{node.get_key()}", end=" ")
            print("(", end=" ")
            self.PT(node.get_left())
            print(",", end=" ")
            self.PT(node.get_right())
            print(")", end=" ")
        else:
            print("-", end=" ")

    def get_root(self):
        return self.root

    def serialization(self,node):
        if node is not None:
            return str(node.get_key()) + "," + self.serialization(node.get_left()) + "," + self.serialization(node.get_right())
        else:
            return "-"

    def find_leafs(self, node):

        keys = []
        counted_hops = []

        def sub_recursive_function(node, hops, keys,counted_hops):
            if node.get_left() is not None:
                hops -= 1
                sub_recursive_function(node.get_left(), hops, keys,counted_hops)
                hops += 1
            if node.get_right() is not None:
                hops -= 1
                sub_recursive_function(node.get_right(), hops, keys,counted_hops)
                hops += 1
            if node.get_left() is None and node.get_right() is None:
                keys.append(node.get_key())
                counted_hops.append(hops)

        hops = 0
        sub_recursive_function(node,hops,keys,counted_hops)

        return keys, counted_hops


