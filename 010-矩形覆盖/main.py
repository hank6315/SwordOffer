# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0: return 0
        f1 = 1
        f2 = 2
        if number == 1 : return f1
        if number == 2 : return f2
        
        for _ in range(number - 2):
            f2 , f1 = f1 + f2 , f2
            
        return f2