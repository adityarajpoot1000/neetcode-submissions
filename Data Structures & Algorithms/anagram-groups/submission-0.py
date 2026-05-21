class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        cnt = dict()
        for i, s in enumerate(strs):

            count = dict()
            for k in range(26):
                count[chr(97+k)] = 0
            for j in s:
                count[j] +=1 
            t = tuple(count.items())

            if t in cnt.keys():
                cnt[t].append(i)
            else:
                cnt[t] = [i]
        ans = []
        for i in cnt.keys():
            t = []
            for j in cnt[i]:
                t.append(strs[j])
            ans.append(t)


            
        return ans


