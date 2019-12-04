# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if pre == [] :
            return None
        
        root_val = pre[0]
        root = None #TreeNode(root_val)
        cnt = tin.index(root_val)
        root.left = self.reConstructBinaryTree(pre[1: cnt + 1], tin[:cnt])
        root.right = self.reConstructBinaryTree(pre[cnt+ 1 :], tin[cnt + 1 :])
        return root
        