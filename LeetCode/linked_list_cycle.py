from itertools import count


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detect_cycle(self, head):
        idx = 0
        l_set = set()
        l_tuple = ()
        while head:
            if head not in l_set:
                l_set.add(head)
                l_tuple += (head, idx)
                idx += 1
            else:
                res = (idx for head_check, idx in l_tuple if head_check == head)
        return res[0]

