# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import helper
from helper import ListNode

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        result = head

        half_node = head
        count = 0
        while head and head.next:
            half_node = half_node.next
            head = head.next.next
            count += 1

        # reverse
        prev_node = None
        while half_node:
            half_node.next, prev_node, half_node = prev_node, half_node, half_node.next

        half_node = prev_node

        head = result
        for i in range(count):
            if half_node.val == head.next.val and i+1 == count:
                break

            to_insert_node = half_node
            half_node = half_node.next

            to_insert_node.next = head.next
            head.next = to_insert_node
            head = head.next.next

        return result

nums = [1,2,3,4,5,6]
param = helper.make_node_list(nums)
print(Solution().reorderList(param))