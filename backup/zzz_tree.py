class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(values):
    """Helper to build a binary tree from a list of values (level order)."""
    if not values:
        return None
    root = BTNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)
        if i < len(values) and values[i] is not None:
            current.left = BTNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = BTNode(values[i])
            queue.append(current.right)
        i += 1
    return root


def traverse_tree(root):
    """Helper to traverse the tree in level order and return a list of values."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        result.append(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


def invertTree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.left)
    return root


if __name__ == "__main__":
    root = [4, 2, 7, 1, 3, 6, 9]
    root_node = build_tree(root)
    print(traverse_tree(root_node))
    inverted_root = invertTree(root_node)
    print(traverse_tree(inverted_root))
