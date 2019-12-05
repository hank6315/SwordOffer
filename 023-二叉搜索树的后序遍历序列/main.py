# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence: return False
        return self.helper(sequence)
    
    def helper(self,sequence):
        if len(sequence) <= 1: return True
        
        root = sequence[-1]
        
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        for j in range(i, len(sequence)-1):
            if sequence[j] < root:
                return False
        return self.helper(sequence[:i]) and self.helper(sequence[i:-1])