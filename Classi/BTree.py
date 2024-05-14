from Classi.BTreeNode import BTreeNode


class BTree:

    def __init__(self,t):
        self.root = BTreeNode(True)
        self.t = t
        self.disk_operations = 0


    def BTreeInsert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            root = self.BTreeSplitRoot()
        self.BTreeInsertNonfull(root, k)
        reads = self.disk_operations
        self.reset_disk_operations()
        return reads


    def BTreeInsertNonfull(self,x, k):
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i = i + 1
            self.disk_operations += 1
        if x.leaf:
            x.keys.insert(i, k)
            self.disk_operations += 1
        else:
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self.BTreeSplitChild(x, i)
                if k > x.keys[i]:
                    i = i + 1
                    self.disk_operations += 1
            self.BTreeInsertNonfull(x.children[i], k)


    def BTreeSplitRoot(self):
        new_root = BTreeNode(False)
        new_root.children.append(self.root)
        self.disk_operations += 1
        self.root = new_root
        self.BTreeSplitChild(new_root, 0)
        return new_root


    def BTreeSplitChild(self, x, i):
        t = self.t
        full_node = x.children[i]
        new_node = BTreeNode(full_node.leaf)
        new_node.keys = full_node.keys[t:]

        if not full_node.leaf:
            new_node.children = full_node.children[t:]

        x.children.insert(i + 1, new_node)
        x.keys.insert(i, full_node.keys[t - 1]) # median key
        full_node.keys = full_node.keys[:t - 1]
        full_node.children = full_node.children[:t]

        self.disk_operations += 3

    def BTreeSearch(self, x, k):
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i = i + 1
        if i < len(x.keys) and k == x.keys[i]:
            return (x,i)
        elif x.leaf:
            return None
        self.disk_operations += 1
        return self.BTreeSearch(x.children[i], k)


    def BTreeSearch_no_tracking(self, x, k):
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i = i + 1
        if i < len(x.keys) and k == x.keys[i]:
            return (x,i)
        elif x.leaf:
            return None
        return self.BTreeSearch_no_tracking(x.children[i], k)



    def find_leaf_depths(self, node, depth=0):
        if node.leaf:
            return [(key, depth) for key in node.keys]
        else:
            depths = []
            for child in node.children:
                depths.extend(self.find_leaf_depths(child, depth - 1))
            return depths


    def get_search_hops(self):
        return self.disk_operations

    def set_search_hops(self, hops):
        self.disk_operations = hops

    def reset_disk_operations(self):
        self.disk_operations = 0

    def get_root(self):
        return self.root

