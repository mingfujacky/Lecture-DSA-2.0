# Binary Search Tree (BST) implementation.
import sys
sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/my_package"
)
from stacks.stack_sll import Stack
from trees.bst_node import Node

class BinarySearchTree:

    def __init__(self):
        self._root = None

    def __repr__(self):
        return f'BinarySearchTree({str(self)})'

    def __str__(self):
        return str(self._root)

    def __len__(self) -> bool:
        """Return the number of values stored in the tree."""
        # This version of the traversal algorithm uses an explicit stack, instead of recursion.
        stack = Stack()
        stack.push(self._root)
        size = 0
        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                size += 1
                stack.push(node.right())
                stack.push(node.left())
        return size


#     def __iter__(self):
#         """
#         Iterate over the values in the BST.

#         Parameters:
#             None

#         Functionality:
#             Iterates over the values in the BST. The iteration starts at the root of the BST and
#             traverses the tree using inorder traversal.
#         """
#         current = self._root
#         stack = Stack()
#         while current is not None or len(stack) > 0:
#             if current is None:
#                 current = stack.pop()
#                 yield current.value()
#                 current = current.right()
#             else:
#                 while current.left() is not None:
#                     stack.push(current)
#                     current = current.left()
#                 yield current.value()
#                 current = current.right()


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
            node_val = node.value()
            if node_val == value:
                return node, parent
            elif value < node_val:
                parent = node
                node = node.left()
            else:
                parent = node
                node = node.right()
        return None, None


    def contains(self, value):
        return self._search(value)[0] is not None


    def insert(self, value):       
        node = self._root
        if node is None: # Empty tree
            self._root = Node(value)
            return None
        
        while node is not None:
            if value <= node.value():
                if node.left() is None:
                    node.set_left(Node(value))
                    break
                else:
                    node = node.left() # We keep traversing the left branch
            elif node.right() is None:
                    node.set_right(Node(value))
                    break
            else:
                node = node.right()  # We keep traversing the right branch

    def delete(self, value):
        """ Delete a value from the tree.
            If the value is not found, raise a ValueError.
            If the tree is empty, raise a ValueError.
            If the tree contains duplicates, delete the first node found.
        """
        if self._root is None:
            raise ValueError('Delete on an empty tree')
        node, parent = self._search(value)
        if node is None:
            raise ValueError('Value not found')

        if node.left() is None or node.right() is None:
            if node.left() is None:
                maybe_child = node.right() 
            else:
                maybe_child = node.left()

            # The node has at most only one child
            if parent is None:
                # The node is the root
                self._root = maybe_child
            elif value <= parent.value():
                parent.set_left(maybe_child)
            else:
                parent.set_right(maybe_child)
        
        else: # The node N has two children.
            # Find and remove the node M with the largest value in the left subtree of N.
            max_node, max_node_parent = node.left().find_max_in_subtree()
            if max_node_parent is None: # M is the left child of N.
                new_node = Node(max_node.value(), None, node.right())
            else:
            # Then  replace the node to be deleted with a new node with M.value(),
                new_node = Node(max_node.value(), node.left(), node.right())
                max_node_parent.set_right(max_node.left())
            
            if parent is None:
                # The node is the root
                self._root = new_node
            elif value <= parent.value():
                parent.set_left(new_node)
            else:
                parent.set_right(new_node)

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print(bst)  # Should print the BST structure
    print('length:', len(bst))  # Should print the number of nodes in the BST
    print(bst.contains(4))  # Should return True
    print(bst.contains(10))  # Should return False
    bst.delete(4)  # Should delete the node with value 4
    print(bst)  # Should print the BST structure after deletion
    bst.delete(7)   # Should delete the node with value 7  
    print(bst)  # Should print the BST structure after deletion