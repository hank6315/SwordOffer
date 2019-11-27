# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        left = 0
        right = len(rotateArray) - 1
        
        while left < right:
            if rotateArray[left] < rotateArray[right]:
                return rotateArray[left]
            
            mid = (left + right )/ 2
            
            if rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            else :
                right = mid
        return rotateArray[left]
        