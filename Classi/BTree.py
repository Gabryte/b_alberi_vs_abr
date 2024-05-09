from Classi.BTreeNode import BTreeNode


class BTree:

    def __init__(self,t):
        self.root = BTreeNode(True)
        self.t = t

    def BTreeDelete(self, x, k):
        t = self.t
        i = 1
        while i <= x.n and k > x.key[i]:
            i = i + 1
        if x.leaf:
            if i <= x.n and k == x.key[i]:  # key k found in node x
                x.key.pop(i)
                x.n -= 1
            else:
                print("The key", k, "is not in the tree")
        else:
            if i <= x.n and k == x.key[i]:  # key k found in node x
                y = x.child[i]
                z = x.child[i + 1]
                if y.n >= t:  # case 2a
                    x.key[i] = self.BTreeDeleteMax(y)
                    x.child[i] = y
                elif z.n >= t:  # case 2b
                    x.key[i] = self.BTreeDeleteMin(z)
                    x.child[i + 1] = z
                else:  # case 2c
                    x.key.pop(i)
                    x.child.pop(i)
                    x.n -= 1
                    x = self.BTreeMergeChildren(x, i, y, z)
                    self.BTreeDelete(x, k)
            else:  # key k not found in node x
                if x.child[i].n >= t:
                    self.BTreeDelete(x.child[i], k)
                else:
                    if i > 1 and x.child[i - 1].n >= t:  # case 3a
                        self.BTreeShiftRight(x, i)
                        self.BTreeDelete(x.child[i], k)
                    elif i < x.n and x.child[i + 1].n >= t:  # case 3a
                        self.BTreeShiftLeft(x, i)
                        self.BTreeDelete(x.child[i], k)
                    else:  # case 3b
                        if i < x.n:
                            x = self.BTreeMergeChildren(x, i, x.child[i], x.child[i + 1])
                        else:
                            x = self.BTreeMergeChildren(x, i - 1, x.child[i - 1], x.child[i])
                        self.BTreeDelete(x, k)
        return x

    def BTreeShiftLeft(self, x, i):
        y = x.children[i]  # node
        z = x.children[i + 1]  # right sibling

        # Move a key from the parent to y
        y.keys.append(x.keys[i - 1])

        # Move a key from z to the parent
        x.keys[i - 1] = z.keys.pop(0)

        # If not leaf nodes, move a child from z to y
        if not z.leaf:
            y.children.append(z.children.pop(0))


    def BTreeDeleteMax(self, x):
        if x.leaf:
            return x.keys.pop(-1)
        else:
            return self.BTreeDeleteMax(x.children[-1])

    def BTreeDeleteMin(self, x):
        if x.leaf:
            return x.keys.pop(0)
        else:
            return self.BTreeDeleteMin(x.children[0])

    def BTreeShiftRight(self, x, i):
        y = x.children[i - 1]  # left sibling
        z = x.children[i]  # node

        # Move a key from the parent to z
        z.keys.insert(0, x.keys[i - 1])

        # Move a key from y to the parent
        x.keys[i - 1] = y.keys.pop()

        # If not leaf nodes, move a child from y to z
        if not y.leaf:
            z.children.insert(0, y.children.pop())

    def BTreeMergeChildren(self, x, i, y, z):
        # Move a key from the parent to y
        y.keys.append(x.keys[i - 1])

        # Merge keys from z to y
        y.keys.extend(z.keys)

        # If not leaf nodes, merge children from z to y
        if not z.leaf:
            y.children.extend(z.children)

        # Remove key and pointer to z from x
        x.keys.pop(i - 1)
        x.children.pop(i)

        return y


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

