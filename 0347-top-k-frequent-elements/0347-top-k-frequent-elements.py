class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        
        # sorted(freq.items(), key = lambda x : x[1], reverse = True) this sorts the items based on the frequency
        # and reverses it means arranges in descending order
        for key,cnt in sorted(freq.items(), key = lambda x : x[1], reverse = True)[:k]:
            res.append(key)

        return res