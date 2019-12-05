# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, nums):
        # write code here
        
        if not nums : return []
        res = []
        #list(sorted(nums))
        self.dfs(nums, "", res)
        return sorted(list(set(res)))
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+ nums[i], res)


##
# -*- coding:utf-8 -*-
class Solution1:
    def Permutation(self, nums):
        # write code here
        
        if not nums : return []
        res = []
        list(sorted(nums))
        self.dfs(nums, "", res)
        return list(res)
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            self.dfs(nums[:i]+nums[i+1:], path+ nums[i], res)