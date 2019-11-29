# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, node):
        # write code here
        self.s1.append(node)
        if not self.s2 or node <= self.s2[-1]:
            self.s2.append(node)
    def pop(self):
        # write code here
        if self.s1[-1] == self.s2[-1] :
            self.s2.pop()
            
        self.s1.pop()
    def top(self):
        # write code here
        return self.s1[-1]
    def min(self):
        # write code here
        
        return self.s2[-1]