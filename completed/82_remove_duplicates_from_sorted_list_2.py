# Definition for singly-linked list.
import helper
from helper import ListNode

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        result_head = ListNode()
        current_node = result_head

        prev_value = None
        not_include: list = []

        while head is not None:
            val = head.val
            if val not in not_include and prev_value is None:
                prev_value = val
            elif val == prev_value or val in not_include:
                prev_value = None
                not_include.append(val)
            elif prev_value != val:
                current_node.next = ListNode(prev_value)
                current_node = current_node.next
                prev_value = val

            head = head.next

        if prev_value is not None:
            current_node.next = ListNode(prev_value)

        return result_head.next


node_info = [1,1,1,2,3]
params = helper.make_node_list(node_info)
print(Solution().deleteDuplicates(params))
