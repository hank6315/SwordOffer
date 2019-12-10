# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, head):
        # write code here
        dic = dict()
        m = n = head
        while m:
          dic[m] = None #RandomListNode(m.label)
          m = m.next
        while n:
          dic[n].next = dic.get(n.next)
          dic[n].random = dic.get(n.random)
          n = n.next
        return dic.get(head)