# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode : return None
        
        # right tree
        if pNode.right :
            p = pNode.right 
            while p.left :
                p = p.left
            return p
            
        #no right tree but have parent
        while pNode.next and  pNode != pNode.next.left:
            pNode = pNode.next
        
        #return parent node
        return pNode.next
            
            