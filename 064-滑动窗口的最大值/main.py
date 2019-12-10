# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size == 0 : return []
        windows = []
        res = []
        for i in range(len(num)):
          while windows and windows[0] <= i - size :
            windows.pop(0)
            
          while windows and num[windows[-1]] < num[i] :
            windows.pop(-1)
            
          windows.append(i)
          
          if i < size - 1:
            continue
            
          res.append(num[windows[0]])
          
          
        return res