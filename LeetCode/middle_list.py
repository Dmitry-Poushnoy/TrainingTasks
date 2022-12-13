# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middle_node(self, head):
        head_node = head
        counter = 0
        while head:
            counter += 1
            head = head.next
        middle_index = counter // 2
        for _ in range(middle_index):
            head_node = head_node.next
        return head_node


if __name__ == '__main__':
    l_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    s = Solution()
    print(s.middle_node(l_list).val)
