# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = None
        cur = pHead
        
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            
           
        return pre