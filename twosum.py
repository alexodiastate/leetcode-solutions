from collections import defaultdict

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        my_list = defaultdict(int)

        for i in range(len(nums)):
            if my_list.__contains__(target-nums[i]):
                return [i,my_list.get(target-nums[i])]
            my_list[nums[i]] = i
        return 0