class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = []
        nums = set(nums) #Eliminates Duplicates
        for num in range(1, N+1): 
            if num not in nums:
                res.append(num)

        return res #set of missed numbers
        