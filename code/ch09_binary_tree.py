from ch09_binary_tree_node import BTNode


class BinaryTree:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def set_root(self, root_data):
        """Sets the root node of the tree to `node`."""
        self._root = BTNode(root_data)

    def __str__(self, level=0):
        """Helper to visualize the tree structure in the console."""
        if self.root is None:
            return "<empty tree>"
        return self.root.__str__(level)

    def __len__(self):
        """Returns the number of nodes in the tree."""

        def _count_nodes(node):
            if node is None:
                return 0
            return 1 + _count_nodes(node.left) + _count_nodes(node.right)

        return _count_nodes(self._root)

    def get_height(self, node):
        """Calculates how many steps to the furthest leaf."""
        if node is None:
            return -1
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def search(self, target):
        """Checks if the tree contains a node with `target` data."""

        def _contains_recursive(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return _contains_recursive(node.left) or _contains_recursive(node.right)

        return _contains_recursive(self._root)

    def is_empty(self):
        return self._root is None

    def traverse_in_order(self, node):
        result = []

        def _in_order_recursive(cur):
            if cur is not None:
                _in_order_recursive(cur.left)
                result.append(cur.data)
                _in_order_recursive(cur.right)

        _in_order_recursive(node)
        return result

    def traverse_preorder(self, node):
        result = []

        def _preorder_recursive(cur):
            if cur is not None:
                result.append(cur.data)
                _preorder_recursive(cur.left)
                _preorder_recursive(cur.right)

        _preorder_recursive(node)
        return result

    def traverse_postorder(self, node):
        result = []

        def _postorder_recursive(cur):
            if cur is not None:
                _postorder_recursive(cur.left)
                _postorder_recursive(cur.right)
                result.append(cur.data)

        _postorder_recursive(node)
        return result

    def traverse_level_order(self):
        """Performs a level-order traversal of the tree and returns a list of node data."""
        result = []
        if self.is_empty():
            return result

        queue = [self._root]

        while queue:
            current = queue.pop(0)
            result.append(current.data)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        return result


if __name__ == "__main__":

    # 1. Create the Tree
    my_tree = BinaryTree()
    my_tree.set_root(10)

    # 2. Add children manually to the root
    my_tree.root.left = BTNode(5)
    my_tree.root.right = BTNode(15)

    # 3. Add a grandchild
    node2 = BTNode(2)
    node20 = BTNode(20)
    node21 = BTNode(21)

    my_tree.root.left.left = node2
    node2.left = node20
    node2.right = node21

    # 4. Visualize
    print(my_tree)
    print("Height of tree:", my_tree.get_height(my_tree.root))
    print("Number of nodes in tree:", len(my_tree))
    print("Tree search 15:", my_tree.search(15))
    print("Tree search 99:", my_tree.search(99))

    # 5. In-order Traversal
    print("In-order Traversal:", end=" ")
    traversal_result = my_tree.traverse_in_order(my_tree.root)
    print(traversal_result)

    # 6. Pre-order Traversal
    print("Pre-order Traversal:", end=" ")
    traversal_result = my_tree.traverse_preorder(my_tree.root)
    print(traversal_result)

    # 7. Post-order Traversal
    print("Post-order Traversal:", end=" ")
    traversal_result = my_tree.traverse_postorder(my_tree.root)
    print(traversal_result)

    # 8. Level-order Traversal
    print("Level-order Traversal:", end=" ")
    traversal_result = my_tree.traverse_level_order()
    print(traversal_result)
