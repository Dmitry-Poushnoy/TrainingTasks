class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> list[int]:
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node:
            self.res.append(node.val)
            for child in node.children:
                self.dfs(child)


if __name__ == '__main__':
    s = Solution()
    tree_l = Node(1, [Node(None, Node(3, Node(2, Node(4, Node(None, Node(5, Node(6))))))))
    print(s.preorder(tree_l))

# [1, null, 3, 2, 4, null, 5, 6]
