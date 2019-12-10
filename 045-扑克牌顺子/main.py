# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers : 
          return 0
        
        numbers.sort()
        
        count = 0
        poker_A = 0
        pre_poker  = -1
        
        for i in range(len(numbers)):
          if numbers[i] == 0 :
            poker_A += 1
          else:
            if pre_poker == -1 :
              pre_poker = numbers[i]
            else :
              if pre_poker == numbers[i] :
                return 0
              count += numbers[i] - pre_poker - 1
              pre_poker = numbers[i]
              
        count -= poker_A      
        return count <= 0
              