# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        str_info = f"[{self.val}]"
        next_node = self.next

        while next_node is not None:
            str_info += f" -> [{next_node.val}]"
            next_node = next_node.next
        
        return str_info

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 1 -> 2 -> 3 -> 4
        # first. [2 -> 1] -> 3 -> 4
        # second. 3 -> [2 -> 1] -> 4

        result_head = ListNode()
        while head:
            current_node = ListNode(head.val)
            if result_head.next is not None:
                current_node.next = result_head.next

            result_head.next = current_node
            head = head.next

        return result_head.next


def changeListNode(list_value):
    head = ListNode()
    node = head

    for e in list_value:
        node.next = ListNode(e)
        node = node.next

    return head

print(Solution().reverseList(changeListNode([1,2,3,4]).next))
