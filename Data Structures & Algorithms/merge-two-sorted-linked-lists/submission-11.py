# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currentNode1 = list1
        currentNode2 = list2
        dummy = ListNode(0)
        current = dummy

        while (currentNode1 and currentNode2):
            if (currentNode1.val == currentNode2.val):
                current.next = currentNode1
                current = current.next
                currentNode1 = currentNode1.next

                current.next = currentNode2
                current = current.next
                currentNode2 = currentNode2.next
            elif (currentNode1.val < currentNode2.val):
                current.next = currentNode1
                current = current.next
                currentNode1 = currentNode1.next
            elif (currentNode1.val > currentNode2.val):
                current.next = currentNode2
                current = current.next
                currentNode2 = currentNode2.next
        while (currentNode1):
            current.next = currentNode1
            current = current.next
            currentNode1 = currentNode1.next
        while (currentNode2):
            current.next = currentNode2
            current = current.next
            currentNode2 = currentNode2.next
        return dummy.next
