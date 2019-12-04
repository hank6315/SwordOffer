# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot :
            return []
        
        queue = [pRoot]
        res = []
        while queue :
            n = len(queue)
            temp = []
            for _ in range(n):
                p = queue.pop(0)
                temp.append(p.val)
                if p.left :
                    queue.append(p.left)
                if p.right :
                    queue.append(p.right)
                    
            res.append(temp)
            
            
        return res
        