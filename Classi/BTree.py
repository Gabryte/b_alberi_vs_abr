from Classi.BTreeNode import BTreeNode


class BTree:

    def __init__(self,t):
        self.root = BTreeNode(True)
        self.t = t


    def BTreeInsert(self, k):
        r = self.root
        if r.n == 2 * self.t - 1:
            s = BTreeNode(False)
            s.child[1] = r
            self.root = s
            self.BTreeSplitChild(s, 1)
            self.BTreeInsertNonfull(s, k)
        else:
            self.BTreeInsertNonfull(r, k)


    def BTreeInsertNonfull(self,x, k):
        i = x.n
        if x.leaf:
            while i >= 1 and k < x.key[i]:
                x.key[i + 1] = x.key[i]
                i = i - 1
            x.key[i + 1] = k
            x.n = x.n + 1
        else:
            while i >= 1 and k < x.key[i]:
                i = i - 1
            i = i + 1
            if x.child[i].n == 2 * self.t - 1:
                self.BTreeSplitChild(x, i)
                if k > x.key[i]:
                    i = i + 1
            self.BTreeInsertNonfull(x.child[i], k)

    def BTreeSplitChild(self, x, i):
        z = BTreeNode(x.child[i].leaf)
        z.n = self.t - 1
        for j in range(1, self.t - 1):
            z.key[j] = x.child[i].key[j + self.t]
        if not x.child[i].leaf:
            for j in range(1, self.t):
                z.child[j] = x.child[i].child[j + self.t]
        x.child[i].n = self.t - 1
        j = x.n + 1
        while j >= i + 1:
            x.child[j + 1] = x.child[j]
            j = j - 1
        x.child[i + 1] = z
        j = x.n
        while j >= i:
            x.key[j + 1] = x.key[j]
            j = j - 1
        x.key[i] = x.child[i].key[self.t]
        x.n = x.n + 1


    def BTreeSearch(self, x, k):
        i = 1
        while i <= x.n and k > x.key[i]:
            i = i + 1
        if i <= x.n and k == x.key[i]:
            return (x, i)
        elif x.leaf:
            return None
        else:
            return self.BTreeSearch(x.child[i], k)

