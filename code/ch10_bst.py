# Binary Search Tree (BST) implementation.
from ch10_bst_node import BSTNode
from ch06_stack_sll import Stack


class BinarySearchTree:

    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        # Return the number of values stored in the tree using recursion.
        def _count_nodes(node):
            # Base Case: If the node is None, the size is 0
            if node is None:
                return 0
            # Recursive Step: 1 (current node) + size of children
            return 1 + _count_nodes(node.left) + _count_nodes(node.right)

        return _count_nodes(self._root)

    def _search(self, value):
        """Returns a tuple.
        The first element in the tuple is the node containing the target value,
        or None if not found. If the tree contains duplicates, it returns the first
        node traversed that contains the target value.
        The second element in the tuple is the parent of the node in the first position.
        If the target wasn't found or if it was the root, the parent is set to None.
        """
        parent = None
        node = self._root
        while node is not None:
            node_val = node.data
            if node_val == value:
                return node, parent
            elif value < node_val:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right
        return None, None

    def contains(self, value):
        return self._search(value)[0] is not None

    def insert(self, value):
        node = self._root
        if node is None:  # Empty tree
            self._root = BSTNode(value)
            return None

        while node is not None:
            if value <= node.data:
                if node.left is None:
                    node.left = BSTNode(value)
                    break
                else:
                    node = node.left  # We keep traversing the left branch
            elif node.right is None:
                node.right = BSTNode(value)
                break
            else:
                node = node.right  # We keep traversing the right branch

    def delete(self, value):
        """Delete a value from the tree.
        If the value is not found, raise a ValueError.
        If the tree is empty, raise a ValueError.
        If the tree contains duplicates, delete the first node found.
        """
        if self._root is None:
            raise ValueError("Delete on an empty tree")
        node, parent = self._search(value)
        if node is None:
            raise ValueError("Value not found")

        if node.left is None or node.right is None:
            if node.left is None:
                maybe_child = node.right
            else:
                maybe_child = node.left

            # The node has at most only one child
            if parent is None:
                # The node is the root
                self._root = maybe_child
            elif value <= parent.data:
                parent.left = maybe_child
            else:
                parent.right = maybe_child

        else:  # The node N has two children.
            # Find and remove the node M with the largest value in the left subtree of N.
            max_node, max_node_parent = node.left.find_max_in_subtree()
            if max_node_parent is None:  # M is the left child of N.
                new_node = BSTNode(max_node.data, None, node.right)
            else:
                # Then  replace the node to be deleted with a new node with M.value(),
                new_node = BSTNode(max_node.data, node.left, node.right)
                max_node_parent.set_right(max_node.left)

            if parent is None:
                # The node is the root
                self._root = new_node
            elif value <= parent.data:
                parent.left = new_node
            else:
                parent.right = new_node


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print(bst)  # Should print the BST structure
    print("length:", len(bst))  # Should print the number of nodes in the BST
    print(bst.contains(4))  # Should return True
    print(bst.contains(10))  # Should return False
    bst.delete(4)  # Should delete the node with value 4
    print(bst)  # Should print the BST structure after deletion
    bst.delete(7)  # Should delete the node with value 7
    print(bst)  # Should print the BST structure after deletion
