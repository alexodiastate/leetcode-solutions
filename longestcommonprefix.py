#Problem: https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == None or len(strs) == 1:
            return strs[0]

        #find the shortest word in the list to trav
        shortest = min(strs)

        #start from the first elem
        if len(shortest) == 0:
            return ""
        curr = shortest[0]
