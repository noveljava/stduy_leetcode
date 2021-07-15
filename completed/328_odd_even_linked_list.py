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
    # 개선이 필요.... 너무 느린대
    def oddEvenList(self, head: ListNode) -> ListNode:
        index = 1
        result = head
        while head:
            prev_next_odd_group_member = head
            for _ in range(index):
                prev_next_odd_group_member = prev_next_odd_group_member.next
            
            if prev_next_odd_group_member is None or prev_next_odd_group_member.next is None:
                break

            group_member = prev_next_odd_group_member.next

            prev_next_odd_group_member.next = group_member.next
            group_member.next = head.next
            head.next = group_member

            head = head.next
            index += 1

        return result


def changeListNode(list_value):
    head = ListNode()
    node = head

    for e in list_value:
        node.next = ListNode(e)
        node = node.next

    return head.next

print(Solution().oddEvenList(changeListNode([1, 2, 3, 4, 5, 6])))
