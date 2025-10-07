class UnionFind:
    def __init__(self, n: int):
        # each node is its own parent initially
        self.par = [i for i in range(n)]
        # rank here stores the size of each set
        self.rank = [1] * n

    def find(self, x: int) -> int:
        # path compression: flatten the tree
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]  # point to grandparent
            x = self.par[x]
        return x

    def union(self, x1: int, x2: int) -> bool:
        p1, p2 = self.find(x1), self.find(x2)

        if p1 == p2:
            return False  # already in the same set

        # union by size
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True


class Solution:
    # study
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}                     # email -> index of acc

        # union accounts that share an email
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        emailGroup = defaultdict(list)      # index of acc -> list of emails
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))  # array concat

        return res