class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachableIndex = 0
        for i, num in enumerate(nums):
            if i <= maxReachableIndex:
                # current index is reachable
                maxReachableIndex = max(maxReachableIndex, i+num)
            else:
                return False
        return True