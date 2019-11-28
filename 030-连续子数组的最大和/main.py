# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        ans = array[0]
        sumans = 0

        for i in range(len(array)):
            sumans += array[i]
            ans = max(sumans , ans)
            sumans = max(sumans , 0)
        
        
        return ans