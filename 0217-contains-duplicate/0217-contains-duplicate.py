class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        init_len = len(nums)
        uniq_len = len(set(nums))
        if init_len == uniq_len:
            return False
        return True