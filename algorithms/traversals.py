class Node:
    """
    Binary Search Tree node
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
            Insert Node
        """
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)


def inorder_traversal(root, lvl=0):
    """
    LEFT - NODE - RIGHT
    """
    vals = []
    if root:
        vals = inorder_traversal(root.left, lvl + 1)
        vals.append([root.data, lvl])
        vals += inorder_traversal(root.right, lvl + 1)
    return vals


def preorder_traversal(root, lvl=0):
    """
    NODE - LEFT - RIGHT
    """
    vals = []
    if root:
        vals.append([root.data, lvl])
        vals += preorder_traversal(root.left, lvl + 1)
        vals += preorder_traversal(root.right, lvl + 1)
    return vals


def postorder_traversal(root, lvl=0):
    """
    LEFT - RIGHT - NODE
    """
    vals = []
    if root:
        vals = postorder_traversal(root.left, lvl + 1)
        vals += postorder_traversal(root.right, lvl + 1)
        vals.append([root.data, lvl])
    return vals


if __name__ == '__main__':
    # create Binary Tree
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)

    print(inorder_traversal(root))
    print(preorder_traversal(root))
    print(postorder_traversal(root))
