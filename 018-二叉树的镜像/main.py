# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root : return None
        
        stack = []
        stack.append(root)
        
        while stack:
            p = stack[-1]
            stack.pop()
            
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
                
            p.left , p.right = p.right , p.left
            
        return root