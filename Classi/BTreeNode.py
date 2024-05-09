

class BTreeNode:
    def __init__(self, leaf):
        self.keys = []
        self.children = []
        self.leaf = leaf
        self.n = 0
