class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        cnt = dict()
        for num in nums:
            if num not in cnt.keys():
                cnt[num] = False

        ans = 1
        for start in cnt.keys():
            if cnt[start]:
                continue
            temp = 1
            cnt[start] = True
            while start+1 in cnt.keys():
                temp+=1
                cnt[start+1] = True
                start+=1

            ans = max(ans, temp)
        return ans
