# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        cnt = 0
        res = [0] * len(array)
        
        for n in array :
            if n % 2 != 0:
                cnt += 1
                
        odd_pos = 0
        even_pos = cnt
        
        for i in range(len(array)):
            if array[i] % 2 != 0:
                res[odd_pos] = array[i]
                odd_pos += 1
            else : 
                res[even_pos] = array[i]
                even_pos += 1
                
        return res