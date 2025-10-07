class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if not intervals:
        #     return []

        # Sort by start time
        # O(n * log(n))
        intervals.sort(key=lambda i: i[0])

        output = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = output[-1][1]
            if start <= last_end:                 # overlap → merge
                output[-1][1] = max(last_end, end)
            else:                                 # no overlap → push
                output.append([start, end])

        return output