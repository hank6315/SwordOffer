# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(0 , n + 1):
            temp = i
            while temp :
                if temp % 10 == 1:
                    count +=1
                temp /= 10
                
        return count