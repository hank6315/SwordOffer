class Solution:
    # need to return an arraylist.
    # so we use the stack(list) to store data and return 
    def printListFromTailToHead(self, listNode):
       
        stack = []
        cur = listNode
        
        while cur :
            stack.append(cur.val)
            cur = cur.next
            
        return stack[::-1]


    """
    another similar question is leetcode 206
    the method is used reverse
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        
        while cur :
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            
        
        return pre    
    
        