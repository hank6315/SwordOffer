# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        AxorB = 0
        
        for n in array :
            AxorB ^= n
        
        '''
        the below  is used to find the first value 1 in the AxorB
        -AxorB means 2's, the value xor 2's can find the first value 1 
        for example:
            the number = 1110 , number 2's = (0001)1's + 1 = 0010
            1110 & 0010 = 0010
        
        ''' 
        AxorB &= -AxorB
        # mask = 1
        # while AxorB & mask == 0 :
        #   mask <<= 1
        
        ans = [0,0]
        
        for n in array:
            if AxorB & n:
                ans[0] ^= n
            else :
                ans[1] ^= n
                
                
        return ans