# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        visited = [[False]*cols for _ in range(rows)]
        
        def get_sum(x, y):
          return sum(map(int , str(x) + str(y)))
        
        
        def movingCore(threshold, rows, cols, i, j):
          if get_sum(i, j) <= threshold:
              visited[i][j] = True
              for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                  if 0<=x<rows and 0<=y<cols and not visited[x][y]:
                      movingCore(threshold, rows, cols, x, y)

        movingCore(threshold, rows, cols, 0, 0)
        return sum(sum(visited, []))