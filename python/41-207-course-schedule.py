class Solution:
    # adjancency map called prerequisite map - hashmap (detecting cycles in a graph) + visited hash set
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list (course → prerequisites)
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()   # courses currently in DFS path

        def dfs(crs):
            if crs in visitSet:       # found a cycle
                return False
            if preMap[crs] == []:     # no prereqs left (already processed)
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):      # recurse prereqs
                    return False
            visitSet.remove(crs)
            preMap[crs] = []          # mark as done
            return True

        for crs in range(numCourses):
            if not dfs(crs):          # check each course
                return False
        return True
