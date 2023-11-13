class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
            """
            :type list1: Optional[ListNode]
            :type list2: Optional[ListNode]
            :rtype: Optional[ListNode]
            """

            dummy = ListNode()
            current = dummy

            while list1 is not None and list2 is not None:
                #Merge List
                if list1.val<=list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next

            # Attach the remaining elements from either list
            current.next = list1 if list1 is not None else list2
            
            # Return the merged list starting from the next of the dummy node
            return dummy.next
    
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Create an instance of the Solution class
solution = Solution()

# Call the mergeTwoLists function with the linked lists
merged_list = solution.mergeTwoLists(list1, list2)

# Helper function to convert the linked list to a list for printing
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Print the result
print(linked_list_to_list(merged_list))