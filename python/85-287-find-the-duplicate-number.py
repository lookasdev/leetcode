class Solution:
    # floyd algorithm explanation in video: https://www.youtube.com/watch?v=wjYnzkAhcNk
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        
        # Phase 1: Detect intersection point inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle (duplicate number)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow