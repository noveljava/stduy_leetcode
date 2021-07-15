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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        result = head
        current_index = 0
        find_start_node = None
        find_end_node = None

        next_node = None
        prev = None
        missing_node = None

        if m == n:
            return head

        for _ in range(m-1):
            find_start_node = head


        for _ in range(m, n+1):
            if current_index == m:
                missing_node = head
            elif current_index == n:
                find_end_node = head

            # 내부에 있는 친구들 Reverse 시키기.
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

            current_index += 1

        missing_node.next = next_node
        if find_start_node:
            find_start_node.next = find_end_node
        else:
            result = find_end_node

        return result

def changeListNode(list_value):
    head = ListNode()
    node = head

    for e in list_value:
        node.next = ListNode(e)
        node = node.next

    return head.next

# print(Solution().reverseBetween(changeListNode([1, 2, 3, 4, 5]), 2, 4))
# print(Solution().reverseBetween(changeListNode([5]), 1, 1))
print(Solution().reverseBetween(changeListNode([5, 4]), 1, 2))
# print(Solution().reverseBetween(changeListNode([1, 2, 3, 4, 5, 6]), 2, 5))
