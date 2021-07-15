class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        info: list = []
        info.append(str(self.val))
        head = self.next
        while head is not None:
            info.append(str(head.val))
            head = head.next

        return '->'.join(info)

def make_node_list(info: list) -> ListNode:
    head = ListNode()
    
    value = head
    for i in info:
        value.next = ListNode(i)
        value = value.next

    return head.next