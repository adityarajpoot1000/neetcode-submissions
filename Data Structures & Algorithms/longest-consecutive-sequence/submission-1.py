class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        cnt = dict()
        i = 1
        for num in nums:
            if num not in cnt.keys():
                cnt[num] = [i,0]
                i+=1

        ans = 1
        for start in cnt.keys():
            temp = 1
            while start+1 in cnt.keys():
                temp+=1
                start+=1
            ans = max(ans, temp)
        return ans
