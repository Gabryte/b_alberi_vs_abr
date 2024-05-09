from Classi.BTreeNode import BTreeNode


class BTree:

    def __init__(self,t):
        self.root = BTreeNode(True)
        self.t = t
        self.search_hops = 0


    def BTreeInsert(self, k):
        r = self.root
        hop = 1
        if r.n == 2 * self.t - 1:
            s = BTreeNode(False)
            s.child[0] = r
            self.root = s
            hop = hop + 3
            hop = hop + self.BTreeSplitChild(s, 0)
            hop = hop + self.BTreeInsertNonfull(s, k)
        else:
            hop = hop + self.BTreeInsertNonfull(r, k)
        return hop


    def BTreeInsertNonfull(self,x, k):
        i = x.n
        hop = 1
        if x.leaf:
            while i >= 1 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i = i - 1
                hop = hop + 2
            x.keys[i + 1] = k
            x.n = x.n + 1
            hop = hop + 2
        else:
            while i >= 1 and k < x.keys[i]:
                i = i - 1
                hop = hop + 1
            i = i + 1
            hop = hop + 1
            if x.child[i].n == 2 * self.t - 1:
                hop = hop + self.BTreeSplitChild(x, i)
                if k > x.keys[i]:
                    i = i + 1
                    hop = hop + 1
            hop = hop + self.BTreeInsertNonfull(x.child[i], k)
        return hop

    def BTreeSplitChild(self, x, i):
        z = BTreeNode(x.child[i].leaf)
        z.n = self.t - 1
        hop = 2
        for j in range(1, self.t - 1):
            z.keys[j] = x.child[i].keys[j + self.t]
            hop = hop + 1
        if not x.child[i].leaf:
            for j in range(1, self.t):
                z.child[j] = x.child[i].child[j + self.t]
                hop = hop + 1
        x.child[i].n = self.t - 1
        j = x.n + 1
        hop = hop +2
        while j >= i + 1:
            x.child[j + 1] = x.child[j]
            j = j - 1
            hop = hop + 2
        x.child[i + 1] = z
        j = x.n
        hop = hop + 2
        while j >= i:
            x.keys[j + 1] = x.keys[j]
            j = j - 1
            hop = hop + 2
        x.keys[i] = x.child[i].keys[self.t]
        x.n = x.n + 1
        hop = hop + 2
        return hop


    def BTreeSearch(self, x, k):
        i = 1
        self.search_hops = self.search_hops + 1
        while i <= x.n and k > x.keys[i]:
            i = i + 1
            self.search_hops = self.search_hops + 1
        if i <= x.n and k == x.keys[i]:
            return (x, i)
        elif x.leaf:
            return None
        else:
            return self.BTreeSearch(x.child[i], k)

    def find_leaf_depths(self, node, depth=0):
        # Se il nodo è una foglia, restituisci la profondità
        if node.leaf:
            return [(node, depth)]

        # Altrimenti, esegui la funzione ricorsivamente su ogni figlio
        depths = []
        for child in node.child:
            if child is not None:
                depths.extend(self.find_leaf_depths(child, depth + 1))

        return depths


    def get_search_hops(self):
        return self.search_hops

    def set_search_hops(self, hops):
        self.search_hops = hops

    def reset_search_hops(self):
        self.search_hops = 0

    def get_root(self):
        return self.root

