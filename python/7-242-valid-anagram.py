class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1: Using sorting
        # return sorted(s) == sorted(t)

        # Solution 2: Using Counter
        # return Counter(s) == Counter(t)

        # Solution 3: Using Hash Maps
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True