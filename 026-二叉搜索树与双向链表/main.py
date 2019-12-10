# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, root):
        # write code here
        cur = root
        pre = ans = None
        while cur:
            while cur.left:
                q = cur.left
                while q.right:
                    q = q.right
                q.right = cur
                cur.left, cur = None, cur.left 
            cur.left = pre
            if pre is None:
                ans = cur
            else:
                pre.right = cur
            pre, cur = cur, cur.right
        return ans