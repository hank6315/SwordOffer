# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2: 
            return False
        if self.isSame(pRoot1 , pRoot2) : 
            return True
        
        return self.HasSubtree(pRoot1.left , pRoot2) or self.HasSubtree(pRoot1.right , pRoot2)
    
    def isSame(self, s , t):
        
        if not t :
            return True
        
        elif not s:
            return False
        
        if s.val == t.val : 
            return self.isSame(s.left , t.left) and self.isSame(s.right , t.right)
        else :
            return False
        