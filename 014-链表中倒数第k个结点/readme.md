# 014-链表中倒数第k个结点

题目描述
输入一个链表，输出该链表中倒数第k个结点。

## Solution

slow and fast pointer.
first, let fast go k - 1 steps and the slow and fast go together.
if fast end tail , the slow pointer is on the last k node.

## LeetCode Link
i think that is very similar  
[141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)