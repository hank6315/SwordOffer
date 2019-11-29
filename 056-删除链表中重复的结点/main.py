# -*- coding:utf-8 -*-
    #class ListNode:
    # def __init__(self, x):
    #     self.val = x
    #     self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here

        # dummy to pointer to first node , beacuse maybe the first node will duplicate
        head = None # ListNode(0)
        head.next = pHead
        pre = head
        cur = pHead
        
        while cur and cur.next:
            if cur.val == cur.next.val:
                # if cur.val equal cur.next.val, change cur location
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                #pre.next pointer to cur.next, cur = cur.next    
                pre.next = cur.next
                cur = cur.next
            else :

                # if cur.val != cur.next.val, move the pre and cur loaction.
                pre = cur
                cur = cur.next
                
        return head.next
                    