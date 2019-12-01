# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        f = 1
        if number == 1 : return f
        
        for _ in range(number - 1):
            f = 2 *f
            
        return f