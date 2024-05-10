from Classi.BTreeNode import BTreeNode


class BTree:

    def __init__(self,t):
        self.root = BTreeNode(True)
        self.t = t
        self.search_hops = 0


    def BTreeInsert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            root = self.BTreeSplitRoot()
        self.BTreeInsertNonfull(root, k)
        reads = self.search_hops
        self.reset_search_hops()
        return reads


    def BTreeInsertNonfull(self,x, k):
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i = i + 1
            self.search_hops += 1
        if x.leaf:
            x.keys.insert(i, k)
            self.search_hops += 1
        else:
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self.BTreeSplitChild(x, i)
                if k > x.keys[i]:
                    i = i + 1
                    self.search_hops += 1
            self.BTreeInsertNonfull(x.children[i], k)


    def BTreeSplitRoot(self):
        new_root = BTreeNode(False)
        new_root.children.append(self.root)
        self.search_hops += 1
        self.root = new_root
        self.BTreeSplitChild(new_root, 0)
        return new_root


    def BTreeSplitChild(self, x, i):
        t = self.t
        full_node = x.children[i]
        new_node = BTreeNode(full_node.leaf)
        new_node.keys = full_node.keys[t:]
        self.search_hops += t - 1
        if not full_node.leaf:
            new_node.children = full_node.children[t:]
            self.search_hops += t - 1
        x.children.insert(i + 1, new_node)
        x.keys.insert(i, full_node.keys[t - 1]) # median key
        full_node.keys = full_node.keys[:t - 1]
        full_node.children = full_node.children[:t]
        self.search_hops += 2*t +1

    def BTreeSearch(self, x, k):
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i = i + 1
            self.search_hops += 1
        if i < len(x.keys) and k == x.keys[i]:
            self.search_hops += 1
            return (x,i)
        elif x.leaf:
            self.search_hops += 1
            return None
        else:
            self.search_hops += 1
            return self.BTreeSearch(x.children[i], k)

    def find_leaf_depths(self, node, depth=0):
        if node.leaf:
            return [(key, depth) for key in node.keys]
        else:
            depths = []
            for child in node.children:
                depths.extend(self.find_leaf_depths(child, depth - 1))
            return depths


    def get_search_hops(self):
        return self.search_hops

    def set_search_hops(self, hops):
        self.search_hops = hops

    def reset_search_hops(self):
        self.search_hops = 0

    def get_root(self):
        return self.root

