class BTNode:
    def __init__(self, data, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

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

    def __str__(self, level=0):
        """Helper to visualize the tree structure in the console."""
        ret = "\t" * level + str(self._data) + "\n"
        for child in (self._left, self._right):
            if child is not None:
                ret += child.__str__(level + 1)
            else:
                ret += "\t" * (level + 1) + "None\n"
        return ret

    def __repr__(self):
        left_node_id = id(self._left) if self._left is not None else None
        right_node_id = id(self._right) if self._right is not None else None
        left_node_data = self._left._data if self._left is not None else None
        right_node_data = self._right._data if self._right is not None else None

        return f"BTNode: {id(self)} data: {self._data} (left: {left_node_id}, data: {left_node_data})(right: {right_node_id}, data: {right_node_data})"


if __name__ == "__main__":
    # Test the Node class
    node10 = BTNode(10)
    node5 = BTNode(5)
    node15 = BTNode(15)
    node2 = BTNode(2)
    node8 = BTNode(8)
    node10.left = node5
    node10.right = node15
    node5.left = node2
    node5.right = node8

    print(node10)
    print(repr(node10))
    print(repr(node15))
