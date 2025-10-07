class Solution:
    # monotonic decreasing stack
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index] — strictly decreasing temps

        for i, t in enumerate(temperatures):
            # pop all cooler/equal days; fill their answer with the distance to today
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])  # current day waits for a warmer future day

        return res
    
    # only need the index on the stack
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     n = len(temperatures)
    #     res = [0] * n
    #     stack = []  # indices of days with temps in strictly decreasing order

    #     for i, t in enumerate(temperatures):
    #         while stack and t > temperatures[stack[-1]]:
    #             j = stack.pop()          # j is an earlier, cooler day
    #             res[j] = i - j           # wait until today
    #         stack.append(i)              # store only the index

    #     return res