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
    def swapPairs(self, head: ListNode) -> ListNode:
        result = head
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next

        return result


def changeListNode(list_value):
    head = ListNode()
    node = head

    for e in list_value:
        node.next = ListNode(e)
        node = node.next

    return head.next

print(Solution().swapPairs(changeListNode([1, 2, 3, 4, 5])))
