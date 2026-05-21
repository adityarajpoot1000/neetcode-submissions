class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = dict()
        for i, num in enumerate(nums):
            if num in index.keys():
                index[num].append(i)
            else:
                index[num] = [i]

        for i, num in enumerate(nums):
            if target - num in index.keys():
                if num == target-num and len(index[num])>=2:
                    return index[num][:2]
                elif i != index[target-num][0]:
                    return [i, index[target-num][0]]
