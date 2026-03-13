class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        for i in range(N): #DAY 1
            num = target - nums[i]
            for j in range(i+1, N):
                if num == nums[j]:
                    return [i,j]