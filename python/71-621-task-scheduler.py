class Solution:
    # popping and pushing to a max heap is a log n operation, here it is log 26, meaning the overall time complexity is O(n)
    # from typing import List
    # from collections import Counter, deque
    # import heapq
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]   # use negatives to simulate a max-heap
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)  # do one instance of the most frequent task
                if cnt:                           # if there are more of this task left
                    q.append([cnt, time + n])     # put it in cooldown until time+n

            # if the earliest cooling task is ready, push it back to the heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time