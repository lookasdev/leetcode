class Solution:
    # greedy approach
    # If you fail at some station i, any start before i also fails (because you already went negative).
    # If starting at start fails at i, then every start between start and i also fails.
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1

        return start