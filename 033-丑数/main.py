# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        
        if not index :
            return 0
        res = [1]
        i2 = i3 = i5 = 0
        
        for _ in range(index  - 1):
            m2 = res[i2]*2
            m3 = res[i3]*3
            m5 = res[i5]*5
            
            mm = min(m2,m3,m5)
            
            if mm == m2 :
                i2 += 1
            if mm == m3 :
                i3 += 1  
            if mm == m5 :
                i5 += 1
                
            res.append(mm)
            
         
        
        return res[-1]