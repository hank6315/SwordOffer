class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        
        if not matrix :
            return ans
        
        rowBegin = 0 #top
        rowEnd = len(matrix) - 1 #botton
        colBegin = 0 #left
        colEnd = len(matrix[0]) - 1 #right
        
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin , colEnd + 1):
                ans.append(matrix[rowBegin][i])
                
            rowBegin += 1
            
            for i in range(rowBegin  , rowEnd + 1):
                ans.append(matrix[i][colEnd])
            
            colEnd -= 1
            
            if rowBegin <= rowEnd:
                for i in range(colEnd  , colBegin-1 , -1):
                    ans.append(matrix[rowEnd][i])
                    
            rowEnd -= 1
            
            if colBegin <= colEnd :
                for i in range(rowEnd  , rowBegin-1 , -1):
                    ans.append(matrix[i][colBegin])
                    
            colBegin += 1

        return ans