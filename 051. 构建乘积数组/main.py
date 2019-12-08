# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        if not A :
            return B

        B.append(1)
        
        for i in range(1,len(A)):
            B.append( B[i - 1] * A[i - 1] )
            
        temp = 1
        
        for i in range(len(A) - 2 , -1, -1):
            temp *= A[i + 1]
            B[i] *= temp
        
        
        return B