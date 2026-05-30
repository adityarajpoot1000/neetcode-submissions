class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = nums.copy()
        back = nums.copy()
        n = len(nums)
        for i in range(1,n):
            front[i] *= front[i-1]
        for i in range(n-2,-1,-1):
            back[i] *= back[i+1]
        res = [1]*n
        res[0] = back[1]
        res[-1] = front[-2]
        for i in range(1, n-1):
            res[i] = front[i-1]*back[i+1]
        return res