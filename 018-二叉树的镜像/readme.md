# 018-二叉树的镜像
题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
输入描述:
二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5


## Solution

use stack to store left and right value.
and using `swap` to swap the value.
meaning left = righ right = left

## LeetCode Link
[226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)