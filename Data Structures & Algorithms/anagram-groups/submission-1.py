class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        cnt = dict()
        for i, s in enumerate(strs):

            count = [0]*26
            for j in s:
                count[ord(j)-97] +=1 
            t = tuple(count)

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


