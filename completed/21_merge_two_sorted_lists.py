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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # When l1 = [] and l2 = [] is inputted, It must be return None.
        head_merged_list = ListNode()
        node = head_merged_list

        def put_node(node, val: int):
            node.next = ListNode(val)
            return node.next

        while l1 is not None or l2 is not None:
            if l1 is None:
                while l2 is not None:
                    node = put_node(node, l2.val)
                    l2 = l2.next

            if l2 is None:
                while l1 is not None:
                    node = put_node(node, l1.val)
                    l1 = l1.next

            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    node = put_node(node, l1.val)
                    l1 = l1.next
                else:
                    node = put_node(node, l2.val)
                    l2 = l2.next

        return head_merged_list.next


def changeListNode(list_value):
    head = ListNode()
    node = head

    for e in list_value:
        node.next = ListNode(e)
        node = node.next

    return head

print(Solution().mergeTwoLists(changeListNode([1,2,4]).next, changeListNode([1,3,4]).next))