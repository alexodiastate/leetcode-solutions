class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        myStr = str(x)
        leftPointer = 0
        rightPointer = len(myStr)-1

        while leftPointer < rightPointer:
            if myStr[leftPointer:leftPointer+1] != myStr[rightPointer:rightPointer+1]:
                return False
            leftPointer += 1
            rightPointer -= 1

        return True