class Solution:
    def validTree(self, n, edges):
        if not n:
            return True

        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)

# - In an **undirected** graph, each edge appears in both directions. The `prev` check prevents mislabeling the **back-to-parent** edge as a cycle.
    
# - If there’s a **cycle**, DFS will eventually try to enter an already visited node (not the parent) → returns `False`.
    
# - If the graph is **disconnected**, DFS from node `0` won’t reach all nodes, so `len(visit) < n`.