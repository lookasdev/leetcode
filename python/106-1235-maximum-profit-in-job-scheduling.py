class Solution:
    # T: O(n*log(n)) # log n because of the bisect # better than n^2
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            # dont include
            res = dfs(i + 1)

            # include
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            # finds the first job whose start time is ≥ the current job’s end time
            # j = index of the next non-overlapping job

            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return res

        return dfs(0)

        # insert after duplicates, bisect is alias for bisect_right
        # def bisect(a, x):
        #     lo, hi = 0, len(a)
        #     while lo < hi:
        #         mid = (lo + hi) // 2
        #         if a[mid] <= x:
        #             lo = mid + 1
        #         else:
        #             hi = mid
        #     return lo

        # Any job with start < end_i satisfies a[mid] <= (end_i, -1, -1) → pushed left of j.

        # For jobs with start == end_i, compare second field:
        # (start, end, …) <= (end_i, -1, -1) is False because end >= 0 > -1.

        # So bisect_right stops before these—meaning j is the first index with start >= end_i
        # exactly the next non-overlapping job.

        # !!!
        # it behaves like bisect_left on the start field. We’re just using bisect_right with a specially chosen probe (end_i, -1, -1) to force all start == end_i items to lie to the right of the insertion point. (insertion point being exactly the next non-overlapping job)