# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import helper
from helper import ListNode

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_list_head = ListNode()
        great_list_head = ListNode()

        less_list, great_list = None, None
        while head:
            if head.val < x:
                if less_list:
                    less_list.next = ListNode(head.val)
                    less_list = less_list.next
                else:
                    less_list = ListNode(head.val)
                    less_list_head.next = less_list
            else:
                if great_list:
                    great_list.next = ListNode(head.val)
                    great_list = great_list.next
                else:
                    great_list = ListNode(head.val)
                    great_list_head.next = great_list

            head = head.next

        if great_list_head.next and less_list is not None:
            less_list.next = great_list_head.next
        elif great_list_head.next and less_list is None:
            less_list_head.next = great_list_head.next

        return less_list_head.next

# target 보다 뒤쪽의 숫자를 앞에 끼워넣는다.
# 끼워넣는데, 
info = [3,1,2]
x = 2

param = helper.make_node_list(info)
print(Solution().partition(param, x))