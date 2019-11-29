# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        i = 0
        for v in pushV :
            stack.append(v)
            
            while stack and stack[-1] == popV[i]:
                stack.pop(-1)
                i += 1
                
        
        return len(stack) == 0