# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count = 0
        length = len(numbers) 
        target = numbers[0]
        
        for i in range(length):
            if count == 0 or target == numbers[i]:
                target = numbers[i]
                count += 1
            else :
                count -= 1
        
        
        # need to recount the target number, if it over the half of length.
        count = 0
        for i in numbers:
            if i == target :
                count += 1
                
        if count > len(numbers) / 2 :
            return target 
        else :
            return 0
        