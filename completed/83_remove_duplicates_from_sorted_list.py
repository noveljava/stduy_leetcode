# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import helper
from helper import ListNode

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        result = head
        while head is not None:
            if head.next is not None and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return result

node_info = [1,1,1,2,3]
params = helper.make_node_list(node_info)
print(Solution().deleteDuplicates(params))
