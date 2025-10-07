class Solution:
    # O(m*n*26) # 26 is length of count array # n is average word length # m is number of words in strs
    # better than O(m*n*log(n)) if we were to sort the strings
    # in python lists cannot be keys, so we change it to a tuple instead since they are non mutable
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)  # key = char count tuple, value = list of words
        res = {}  # normal dictionary

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)

            if key not in res:
                res[key] = []
            res[key].append(s)

        return list(res.values())