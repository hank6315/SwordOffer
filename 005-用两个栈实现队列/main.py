
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, node):
        # write code here
        self.s1.append(node)
    def pop(self):
        # return xx
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop(-1))
        return self.s2.pop(-1)


# LeetCode
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        top = self.peek()
        self.stack2.pop()
        
        return top
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stack2 :
            while self.stack1 :
                self.stack2.append(self.stack1[-1])
                self.stack1.pop()
        
        return self.stack2[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack1 == [] and self.stack2 == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()