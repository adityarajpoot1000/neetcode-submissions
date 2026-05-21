class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = list(Counter(nums).items())
        count = sorted(count, key = lambda x: x[1])
        print(count)
        return [x[0] for x in count[-k:]]