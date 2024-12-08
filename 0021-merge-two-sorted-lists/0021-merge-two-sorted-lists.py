class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Step 1: Create a dummy node
        dummy = ListNode(-1)
        current = dummy
        
        # Step 2: Traverse both lists and merge
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1  # Link the smaller node
                list1 = list1.next   # Move to the next node in list1
            else:
                current.next = list2  # Link the smaller node
                list2 = list2.next   # Move to the next node in list2
            current = current.next   # Move the pointer in the merged list
        
        # Step 3: Append the remaining nodes
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Step 4: Return the merged list, skipping the dummy node
        return dummy.next
