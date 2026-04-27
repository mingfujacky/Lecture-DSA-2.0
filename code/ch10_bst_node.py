"""A class modeling the nodes of the binary search tree."""


class BSTNode:

    def __init__(self, data, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def __str__(self, level=0):
        """Helper to visualize the tree structure in the console."""
        ret = "\t" * level + str(self._data) + "\n"
        if self._left is not None:
            ret += self._left.__str__(level + 1)
        if self._right is not None:
            ret += self._right.__str__(level + 1)
        return ret

    def __repr__(self):
        left_node_id = id(self._left) if self._left is not None else None
        right_node_id = id(self._right) if self._right is not None else None
        left_node_data = self._left._data if self._left is not None else None
        right_node_data = self._right._data if self._right is not None else None

        return f"BTNode: {id(self)} data: {self._data} (left: {left_node_id}, data: {left_node_data})(right: {right_node_id}, data: {right_node_data})"

    @property
    def data(self):
        return self._data

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @left.setter
    def left(self, node):
        self._left = node

    @right.setter
    def right(self, node):
        self._right = node

    def find_min_in_subtree(self):
        # Return the node with the smallest value in the subtree rooted at the node, and its parent
        parent = None
        node = self
        while node.left is not None:
            parent = node
            node = node.left
        return node, parent

    def find_max_in_subtree(self):
        # Return the node with the largest value in the subtree rooted at the node, and its parent.
        parent = None
        node = self
        while node.right is not None:
            parent = node
            node = node.right
        return node, parent


if __name__ == "__main__":
    # Test the Node class
    node10 = BSTNode(10)
    node5 = BSTNode(5)
    node15 = BSTNode(15)
    node2 = BSTNode(2)
    node8 = BSTNode(8)
    node10.left = node5
    node10.right = node15
    node5.left = node2
    node5.right = node8
    print(node10)
    print(repr(node10))
    print("-" * 100)
    min_node, min_parent = node10.find_min_in_subtree()
    print("min_node:", min_node)
    print("min_node_parent:", repr(min_parent))
    print("-" * 100)
    max_node, max_parent = node10.find_max_in_subtree()
    print("max_node:", max_node)
    print("max_node_parent:", repr(max_parent))
