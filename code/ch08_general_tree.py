class TreeNode:
    def __init__(self, data):
        self._data = data
        self._children = []

    def add_child(self, child_node):
        """Adds a TreeNode instance to the children list."""
        self._children.append(child_node)

    def __repr__(self, level=0):
        """Helper to visualize the tree structure in the console."""
        ret = "\t" * level + repr(self._data) + "\n"
        for child in self._children:
            ret += child.__repr__(level + 1)
        return ret
    
    def get_height(self):
        # Base Case: If the node has no children (it's a leaf)
        if not self._children:
            return 0
        # Recursive Step: 
        # 1. Get the height of every child
        # 2. Find the maximum height among them
        # 3. Add 1 for the current level (the edge connecting to children)
        return 1 + max(child.get_height() for child in self._children)
    
    def traverse(self, level=0):
        # Create indentation based on the current depth
        indent = "  " * level
        print(f"{indent}{self._data}")
        
        # Recurse for each child, increasing the level
        for child in self._children:
            child.traverse(level + 1)

    @staticmethod
    def save_to_file(node, filename, level=0):
        # 'a' for append or 'w' for write
        mode = 'w' if level == 0 else 'a'
        with open(filename, mode, encoding='utf-8') as f:
        # Save depth and data separated by a comma
            f.write(f"{level},{node._data}\n")
    
        for child in node._children:
            TreeNode.save_to_file(child, filename, level + 1)        
    @staticmethod
    def load_from_file(filename):
        stack = []  # Stores (node, level)
        root = None

        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                # Parse the level and data
                level, data = line.strip().split(',', 1)
                level = int(level)
                new_node = TreeNode(data)

                if level == 0:
                    root = new_node
                    stack = [(root, 0)]
                else:
                    # Find the parent: pop from stack until we find the node 
                    # whose level is exactly (current level - 1)
                    while stack and stack[-1][1] >= level:
                        stack.pop()
                
                    parent_node = stack[-1][0]
                    parent_node.add_child(new_node)
                    stack.append((new_node, level))
    
        return root



if __name__ == "__main__":

    # # 1. Create the nodes
    # root = TreeNode("CS Program")
    # ds = TreeNode("Data Structures")
    # algo = TreeNode("Algorithms")

    # # 2. Build the hierarchy
    # root.add_child(ds)
    # root.add_child(algo)
    # ds.add_child(TreeNode("Arrays"))
    # ds.add_child(TreeNode("Trees"))

    # # 3. Print the tree
    # print(root)

    root = TreeNode.load_from_file("tree.txt")
    print(root)

    # 4. Get and print the height of the tree
    # print("Height of the tree:", root.get_height())  # Output should be 2
    # print("Height of the node ds:", ds.get_height())  # Output should be 0

    # 5. Traverse and print the tree
    print("Tree Traversal:")
    root.traverse() 

    # 6. Save the tree structure to a file
    TreeNode.save_to_file(root, "tree.txt")
