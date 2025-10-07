class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # newInterval goes before current interval (no overlap)
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # newInterval goes after current interval (no overlap)
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # overlap case -> merge intervals
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # add the last merged interval
        res.append(newInterval)
        return res