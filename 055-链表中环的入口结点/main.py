# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead and pHead.next : return None 
        slow = fast = pHead
        
        while fast:
            slow = slow.next
            fast = fast.next
            
            if fast:
                fast =fast.next
            if slow == fast:
                break
                
        if not fast : return None
        
        slow = pHead
        
        while slow != fast :
            slow = slow.next
            fast = fast.next
            
        return fast
        