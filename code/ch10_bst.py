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

        if node.left is None or node.right is None:  # Pattern 1 and Pattern 2
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
            # 1. Find the predecessor m (max node in the left subtree)
            max_node, max_node_parent = node.left.find_max_in_subtree()
            # 2. Create the replacement node. We copy the M's data, but use N's children
            new_node = BSTNode(max_node.data, node.left, node.right)
            # 3. Remove M from its original position. If M has a left child, it must be promoted
            if max_node_parent is None:
                # Special Case: The M is the direct left child of N, that is, M.P is None
                new_node.left = max_node.left
            else:
                # General Case: The M is further down the right-branch of the left subtree
                max_node_parent.right = max_node.left
            # 4. Link the 'new_node' into the tree structure
            if parent is None:
                # The node is the root
                self._root = new_node
            elif value <= parent.data:
                parent.left = new_node
            else:
                parent.right = new_node


if __name__ == "__main__":
    # bst = BinarySearchTree()
    # bst.insert(5)
    # bst.insert(3)
    # bst.insert(7)
    # bst.insert(2)
    # bst.insert(4)
    # bst.insert(6)
    # bst.insert(8)

    # print(bst)  # Should print the BST structure
    # print("length:", len(bst))  # Should print the number of nodes in the BST
    # print(bst.contains(4))  # Should return True
    # print(bst.contains(10))  # Should return False
    # bst.delete(4)  # Should delete the node with value 4
    # print(bst)  # Should print the BST structure after deletion
    # bst.delete(7)  # Should delete the node with value 7
    # print(bst)  # Should print the BST structure after deletion

    # case 1-1
    print("Case 1-1")
    bst = BinarySearchTree()
    bst.insert(0)
    print(bst)  # Should print the BST structure
    bst.delete(0)  # Should delete the node with value 0
    print(bst)  # Should print the BST structure after deletion

    # case 1-2
    print("Case 1-2")
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)
    print(bst)  # Should print the BST structure
    bst.delete(1)  # Should delete the node with value 1
    print(bst)  # Should print the BST structure after deletion

    # case 1-3
    print("Case 1-3")
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(2)
    bst.insert(7)
    bst.insert(3)
    print(bst)  # Should print the BST structure
    bst.delete(3)  # Should delete the node with value 3
    print(bst)  # Should print the BST structure after deletion

    # case 2-1
    print("Case 2-1")
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(1)
    print(bst)  # Should print the BST structure
    bst.delete(3)  # Should delete the node with value 3
    print(bst)  # Should print the BST structure after deletion

    # case 2-2
    print("Case 2-2")
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(1)
    bst.insert(2)
    print(bst)  # Should print the BST structure
    bst.delete(3)  # Should delete the node with value 3
    print(bst)  # Should print the BST structure after deletion

    # case 2-3
    print("Case 2-3")
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(4)
    bst.insert(7)
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    print(bst)  # Should print the BST structure
    bst.delete(4)  # Should delete the node with value 4
    print(bst)  # Should print the BST structure after deletion

    # case 2-4
    print("Case 2-4")
    bst = BinarySearchTree()
    bst.insert(7)
    bst.insert(3)
    bst.insert(9)
    bst.insert(5)
    bst.insert(4)
    bst.insert(6)
    print(bst)  # Should print the BST structure
    bst.delete(3)  # Should delete the node with value 3
    print(bst)  # Should print the BST structure after deletion

    # case 2-5
    print("Case 2-5")
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(1)
    bst.insert(8)
    bst.insert(5)
    bst.insert(4)
    bst.insert(6)
    print(bst)  # Should print the BST structure
    bst.delete(8)  # Should delete the node with value 8
    print(bst)  # Should print the BST structure after deletion

    # case 2-6
    print("Case 2-6")
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(1)
    bst.insert(5)
    bst.insert(8)
    bst.insert(6)
    bst.insert(9)
    print(bst)  # Should print the BST structure
    bst.delete(5)  # Should delete the node with value 5
    print(bst)  # Should print the BST structure after deletion

    # case 3A-1
    print("Case 3A-1")
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    print(bst)  # Should print the BST structure
    bst.delete(3)  # Should delete the node with value 3
    print(bst)  # Should print the BST structure after deletion

    # case 3A-2
    print("Case 3A-2")
    bst2 = BinarySearchTree()
    bst2.insert(5)
    bst2.insert(4)
    bst2.insert(6)
    bst2.insert(2)
    bst2.insert(3)
    print(bst2)  # Should print the BST structure
    bst2.delete(5)  # Should delete the node with value 5
    print(bst2)  # Should print the BST structure after deletion

    # case 3A-3
    print("Case 3A-3")
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(2)
    bst.insert(5)
    bst.insert(3)
    print(bst)  # Should print the BST structure
    bst.delete(4)  # Should delete the node with value 4
    print(bst)  # Should print the BST structure after deletion

    # case 3A-4
    print("Case 3A-4")
    bst = BinarySearchTree()
    bst.insert(8)
    bst.insert(4)
    bst.insert(9)
    bst.insert(3)
    bst.insert(6)
    bst.insert(1)
    bst.insert(5)
    print(bst)  # Should print the BST structure
    bst.delete(8)  # Should delete the node with value 8
    print(bst)  # Should print the BST structure after deletion

    # case 3B-1
    print("Case 3B-1")
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(2)
    bst.insert(5)
    bst.insert(1)
    bst.insert(3)
    print(bst)  # Should print the BST structure
    bst.delete(2)  # Should delete the node with value 2
    print(bst)  # Should print the BST structure after deletion

    # case 3B-2
    print("Case 3B-2")
    bst = BinarySearchTree()
    bst.insert(6)
    bst.insert(4)
    bst.insert(7)
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    print(bst)  # Should print the BST structure
    bst.delete(4)  # Should delete the node with value 4
    print(bst)  # Should print the BST structure after deletion

    # case 3B-3
    print("Case 3B-3")
    bst = BinarySearchTree()
    bst.insert(6)
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(4)
    bst.insert(2)
    bst.insert(5)
    print(bst)  # Should print the BST structure
    bst.delete(3)  # Should delete the node with value 3
    print(bst)  # Should print the BST structure after deletion
    # case 3B-4
    print("Case 3B-4")
    bst = BinarySearchTree()
    bst.insert(8)
    bst.insert(5)
    bst.insert(9)
    bst.insert(2)
    bst.insert(6)
    bst.insert(1)
    bst.insert(4)
    bst.insert(7)
    bst.insert(3)
    print(bst)  # Should print the BST structure
    bst.delete(5)  # Should delete the node with value 5
    print(bst)  # Should print the BST structure after deletion
