# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.index = -1
        
    def Serialize(self, root):
            # write code here
        if root:
            return str(root.val) + ' ' + self.Serialize(root.left) + self.Serialize(root.right)
        else:
            return '# '
        
    def Deserialize(self, s):
        # write code here
        l = s.split()
        self.index += 1
        if self.index >= len(s):
            return None
        
        node = None
        
        if l[self.index] != '#' :
            node = None #TreeNode(int(l[self.index]))
            node.left = self.Deserialize(s)
            node.right = self.Deserialize(s)
            
        return node
         