# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        import heapq as hq
        
        if k > len(tinput) or k <= 0 :
            return []
        
        heap = [-x for x in tinput[:k]]
        hq.heapify(heap)
        for num in tinput[k:]:
            if -heap[0] > num:
                hq.heapreplace(heap, -num)
        return sorted(-x for x in heap)
        