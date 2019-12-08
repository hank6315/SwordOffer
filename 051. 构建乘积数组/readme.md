# 051. 构建乘积数组

给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。


## Solution

ex.{1,2,3,4}

先從左邊往後掃描一次會得到{1,1,2,6}
再從後面掃回來會得到{24,12,4,1}
再把兩個相乘

## LeetCode Link
[238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)