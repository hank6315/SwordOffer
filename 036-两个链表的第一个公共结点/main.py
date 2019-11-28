# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1 = pHead1 
        p2 = pHead2
        
        if not p1 and not p2 : return None
        
        while p1 and p2 and p1 != p2 :
            p1 = p1.next
            p2 = p2.next
            
            if p1 == p2 :
                return p1
            
            # if can't find p1 link, put the p1 to pHead2.
            if not p1 : p1 = pHead2
            if not p2 : p2 = pHead1
                
        
        return p2