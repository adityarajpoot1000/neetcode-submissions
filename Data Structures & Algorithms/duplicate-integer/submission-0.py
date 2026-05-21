class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = dict()
        for i in nums:
            if i in count.keys():
                return True
            else:
                count[i] = None
        return False
            