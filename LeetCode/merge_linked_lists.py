# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, list1: ListNode, list2: ListNode) -> ListNode | None:
        list_of_values = self.make_list_of_sorted_values(list1, list2)
        if list_of_values:
            head_node = res_list_of_nodes = ListNode(list_of_values[0])
            for ind, val in enumerate(list_of_values[1:]):
                res_list_of_nodes.next = ListNode(val)
                res_list_of_nodes = res_list_of_nodes.next
            return head_node
        else:
            return None

    def print_list_of_nodes(self, head_node):
        while head_node is not None:
            print(head_node.val)
            head_node = head_node.next

    def make_list_of_sorted_values(self, list1, list2):
        list_of_values = []
        if list1 is None and list2 is None:
            return []
        for _node in (list1, list2):
            while _node is not None:
                list_of_values.append(_node.val)
                _node = _node.next
        list_of_values.sort()
        return list_of_values


if __name__ == '__main__':
    list_a = ListNode(1, ListNode(2, ListNode(4)))
    list_b = ListNode(1, ListNode(3, ListNode(4)))
    s = Solution()
    print(s.merge_two_lists(list_a, list_b))

# TypeError: 'NoneType' object is not subscriptable
#     head_node = res_list_of_nodes = ListNode(list_of_values[0])
# Line 9 in mergeTwoLists (Solution.py)
#     ret = Solution().mergeTwoLists(param_1, param_2)
# Line 55 in _driver (Solution.py)
#     _driver()
# Line 66 in <module> (Solution.py)
