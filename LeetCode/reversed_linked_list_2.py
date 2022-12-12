class ListNode:
    def __init__(self, val, next_nd=None):
        self.val = val
        self.next_nd = next_nd

    def print_list(self) -> None:
        """ Вывести в консоль последовательность значений связного списка """
        if self is None:
            print("None list")
        while self:
            if self.next_nd is not None:
                print(f"{self.val}, ", end='')
            else:
                print(f"{self.val}")
            self = self.next_nd

    def reverse_list(self):
        """ Развернуть лист в обратную сторону """
        previous_node = None
        current_node = self
        while current_node:
            next_node = current_node.next_nd
            current_node.next_nd = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node


if __name__ == '__main__':
    initial_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    initial_list.print_list()
    initial_list.reverse_list().print_list()
