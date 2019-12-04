# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        stack = [n for n in s.split(' ')]
        stack.reverse()
        
        return ' '.join(stack)

    # leetcode 
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))

  