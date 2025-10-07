class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        # store (distance, x, y)
        for x, y in points:
            dist = x**2 + y**2   # squared distance
            minHeap.append((dist, x, y))

        # turn into a heap in O(n)
        heapq.heapify(minHeap)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)  # extract smallest distance
            res.append([x, y])
            k -= 1

        return res