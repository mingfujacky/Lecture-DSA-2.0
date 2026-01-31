from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


def parse_n_ary_tree(data):
    if not data:
        return None

    # Step 1: Initialize the root
    root = Node(data[0])
    queue = deque([root])

    # Pointer for the current element in the data list
    # We skip index 0 (root) and index 1 (the first null separator)
    i = 2

    while i < len(data) and queue:
        # Get the current parent node who needs children
        # print([node.val for node in queue])
        current_parent = queue.popleft()

        # Step 2: Process all children until the next 'null'
        while i < len(data) and data[i] is not None:
            child_node = Node(data[i])
            current_parent.children.append(child_node)
            queue.append(child_node)
            i += 1

        # Step 3: Skip the 'null' separator to move to the next parent's children
        i += 1

    return root


def print_preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    for child in root.children:
        print_preorder(child)


if __name__ == "__main__":
    data = [1, None, 3, 2, 4, None, 5, 6]
    root = parse_n_ary_tree(data)
    print_preorder(root)
