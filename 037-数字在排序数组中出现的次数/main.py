# -*- coding:utf-8 -*-
class Solution:
    
    def helper(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] < k:
                low = mid + 1
        return high
    
    def GetNumberOfK(self, data, k):
        # write code here
        
        if not data : return 0
        return self.helper(data , k + 0.5) - self.helper(data , k - 0.5)