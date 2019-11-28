# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def maxDepth(self, root):
        if not root : return 0
        res = 1
        
        if root.left:
            res = max(res , self.maxDepth(root.left) + 1)
        if root.right:
            res = max(res , self.maxDepth(root.right) + 1)
            
        return res
    
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot : return True
        
        left = self.maxDepth(pRoot.left)
        right = self.maxDepth(pRoot.right)
        
        
        return (abs(left - right) <= 1 and 
                self.IsBalanced_Solution(pRoot.left) and 
                self.IsBalanced_Solution(pRoot.right))
        
        
    