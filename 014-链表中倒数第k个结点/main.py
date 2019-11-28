# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        
        if not head :
            return None
        slow = fast = head
        
        for _ in range(k):
            if fast:
                fast = fast.next
            else:
                return None
            
        while fast:
            slow = slow.next
            fast = fast.next
            
        return slow


