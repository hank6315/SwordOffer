# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        deepth = 1
        
        if pRoot.left :
            deepth = max(deepth ,self.TreeDepth(pRoot.left) + 1 )
        if pRoot.right :
            deepth = max(deepth ,self.TreeDepth(pRoot.right) + 1)
            
        return deepth
            