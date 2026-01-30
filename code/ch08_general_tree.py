from ch08_general_tree_node import GeneralTreeNode
class GeneralTree:
    def __init__(self):
        self._root = None

    def set_root(self, root_data):  
        """Sets the root node of the tree to a new node with `root_data`."""
        self._root = GeneralTreeNode(root_data)    

    def insert_child(self, parent_node, child_node):
        """Inserts a new child node with `child_node` under `parent_node`."""
        parent_node.add_child(child_node)
        return True    

    def delete_child(self, parent_node, child_node):
        """Deletes `child_node` from the children of `parent_node`."""
        parent_node.remove_child(child_node)

    def is_empty(self):
        """Checks if the tree is empty."""
        return self._root is None

    def get_root(self):
        """Returns the root node of the tree."""
        return self._root
    
    def search(self, target_data):
        """Searches for a node with `target_data` in the tree."""
        def _search_recursive(node):
            if node._data == target_data:
                return node
            for child in node._children:
                result = _search_recursive(child)
                if result is not None:
                    return result
            return None

        if self.is_empty():
            return None
        return _search_recursive(self._root)
    
    def height(self):
        """Calculates the height of the tree."""
        def _height_recursive(node):
            if not node._children:
                return 0
            return 1 + max(_height_recursive(child) for child in node._children)

        if self.is_empty():
            return -1
        return _height_recursive(self._root)
    
    def __len__(self):
        """Returns the number of nodes in the tree."""
        def _count_nodes(node):
            count = 1  # Count the current node
            for child in node._children:
                count += _count_nodes(child)
            return count

        if self.is_empty():
            return 0
        return _count_nodes(self._root)
    
    def traverse_preorder(self):
        """Performs a preorder traversal of the tree and returns a list of node data."""
        result = []

        def _preorder_recursive(node):
            result.append(node._data)
            for child in node._children:
                _preorder_recursive(child)

        if not self.is_empty():
            _preorder_recursive(self._root)
        return result   
    
    def traverse_postorder(self):
        """Performs a postorder traversal of the tree and returns a list of node data."""
        result = []

        def _postorder_recursive(node):
            for child in node._children:
                _postorder_recursive(child)
            result.append(node._data)

        if not self.is_empty():
            _postorder_recursive(self._root)
        return result
    
    def traverse_level_order(self):
        """Performs a level-order traversal of the tree and returns a list of node data."""
        result = []
        if self.is_empty():
            return result

        queue = [self._root]
        while queue:
            current_node = queue.pop(0)
            result.append(current_node._data)
            queue.extend(current_node._children)
        return result

    def __str__(self):
        """Returns a string representation of the tree."""
        return str(self._root)
    
if __name__ == "__main__":
    # 1. Create the general tree with root node
    my_tree = GeneralTree()
    my_tree.set_root("CS Program")

    # 2. Get the root and build the hierarchy
    root = my_tree.get_root()
    ds = GeneralTreeNode("Data Structures")
    algo = GeneralTreeNode("Algorithms")
    my_tree.insert_child(root, ds)
    my_tree.insert_child(root, algo)
    my_tree.insert_child(ds, GeneralTreeNode("Arrays"))
    my_tree.insert_child(ds, GeneralTreeNode("Trees"))

    # 3. Print the tree
    print(my_tree)

    # 4. Test other functionalities
    print("The tree is empty?", my_tree.is_empty())
    print("The root node data:", my_tree.get_root()._data)
    print("Searching for 'Trees':", my_tree.search("Trees") is not None)
    print("Tree height:", my_tree.height())
    print("Number of nodes in the tree:", len(my_tree))
    print("Preorder traversal:", my_tree.traverse_preorder())
    print("Postorder traversal:", my_tree.traverse_postorder())
    print("Level-order traversal:", my_tree.traverse_level_order())
    # 5. Remove a child and print the tree again
    my_tree.delete_child(root, algo)
    print("After removing 'Algorithms':")
    print(my_tree)