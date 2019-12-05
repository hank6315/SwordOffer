# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        res = []
        
        if len(array) <= 0 :
            return res
        
        
        start = 0
        end = len(array) -1
        
        while start < end :
            cursum = array[start] + array[end]
            if cursum == tsum :
                res.append(array[start])
                res.append(array[end])
                break
                
            elif cursum < tsum :
                start += 1
             
            elif cursum > tsum : 
                end -= 1
                
        
        return res
                