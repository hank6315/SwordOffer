# 004-重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。


## Solution
preorder[0]的第一個是root
preorder[0] == inorder[k]
由於inorder是中序排序所以k的左邊是左子樹，k的右邊是右子樹
另外我們也知道節點左子樹的節點數(跟中序的左子樹相同)，我們設為L，所以我們可以知道preorder從1~L+1就是根結點左子樹的前序排序

## LeetCode Link
[105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)