# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot :
            return True
        
        return self.ismirror(pRoot.left , pRoot.right)
    
    def ismirror(self , n , p):
        if not n and not p : return True
        if not n or not p : return False
        
        return n.val == p.val and  self.ismirror(n.left , p.right) and self.ismirror(n.right , p.left)