class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(start_node: ListNode) -> None:
    while start_node:
        print(start_node.val)
        start_node = start_node.next
    return start_node


class Solution:
    def reverse_list(self, head: [ListNode | None]) -> [ListNode | None]:
        values = list()
        while head:
            values.append(head.val)
            head = head.next
        values = values[::-1]

        if not values:
            return None
        if len(values) == 1:
            return ListNode(values[0])

        new_head = ListNode(values[0])
        flag_start = True
        start_node = ListNode()
        for item in values[1:]:
            new_head.next = ListNode(item)
            if flag_start:
                flag_start = False
                start_node = new_head
            new_head = new_head.next

        return start_node


if __name__ == '__main__':
    s = Solution()
    head_inputed = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(s.reverse_list(head_inputed))

# IndexError: list index out of range
#     new_head = ListNode(values[0])
# Line 14 in reverseList (Solution.py)
#     ret = Solution().reverseList(param_1)
# Line 48 in _driver (Solution.py)
#     _driver()
# Line 59 in <module> (Solution.py)
