# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot :
            return None
        
        stack = []
        
        while pRoot or stack :
            while pRoot :
                stack.append(pRoot)
                pRoot = pRoot.left
                
            pRoot = stack.pop()
            
            k -= 1
            
            if k == 0 :
                return pRoot
            
            pRoot = pRoot.right