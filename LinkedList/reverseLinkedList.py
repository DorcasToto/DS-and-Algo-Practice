# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None  # keep track of the previous node
        current = head  # head of the original linked list
        nextNode = None  # keep track of the next node
    
        # Traverse the linked list
        while current is not None:
            nextNode = current.next  # Save the reference to the next node
            current.next = prev  # Reverse the link by pointing the     current node to the previous node
            prev = current  # Move the 'prev' pointer one step forward
            current = nextNode  # Move the 'current' pointer one step forward
        
        return prev  # 'prev' now points to the head of the reversed linked list