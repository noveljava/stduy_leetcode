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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_head = ListNode()
        node = result_head

        def put_node(node, val: int):
            node.next = ListNode(val)
            return node.next

        rounds_value = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                while l2 is not None:
                    sum_value = l2.val + rounds_value
                    rounds_value = sum_value // 10
                    sum_value = sum_value % 10
                    node = put_node(node, sum_value)
                    l2 = l2.next

            if l2 is None:
                while l1 is not None:
                    sum_value = l1.val + rounds_value
                    rounds_value = sum_value // 10
                    sum_value = sum_value % 10
                    node = put_node(node, sum_value)
                    l1 = l1.next

            if l1 is not None and l2 is not None:
                sum_value = l1.val + l2.val + rounds_value
                rounds_value = sum_value // 10
                sum_value = sum_value % 10

                node = put_node(node, sum_value)
                l1 = l1.next
                l2 = l2.next

        if rounds_value != 0:
            node = put_node(node, rounds_value)

        return result_head.next

def changeListNode(list_value):
    head = ListNode()
    node = head

    for e in list_value:
        node.next = ListNode(e)
        node = node.next

    return head

print(Solution().addTwoNumbers(changeListNode([2,4,3]).next, changeListNode([5,6,4]).next))
