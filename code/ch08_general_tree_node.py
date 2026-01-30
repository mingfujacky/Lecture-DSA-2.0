class GeneralTreeNode:
    def __init__(self, data):
        self._data = data
        self._children = []

    def add_child(self, child_node):
        """Adds a GeneralTreeNode instance to the children list."""
        self._children.append(child_node)

    def remove_child(self, child_node):
        """Removes a GeneralTreeNode instance from the children list."""
        self._children.remove(child_node)

    def __str__(self, level=0):
        """Helper to visualize the tree structure in the console."""
        ret = "\t" * level + str(self._data) + "\n"
        for child in self._children:
            ret += child.__str__(level + 1)
        return ret

if __name__ == "__main__":
    # 1. Create the nodes
    cs = GeneralTreeNode("CS Program")
    ds = GeneralTreeNode("Data Structures")
    algo = GeneralTreeNode("Algorithms")

    # 2. Build the hierarchy
    cs.add_child(ds)
    cs.add_child(algo)
    ds.add_child(GeneralTreeNode("Arrays"))
    ds.add_child(GeneralTreeNode("Trees"))

    # 3. Print the tree
    print(cs)

    # 4. Remove a child and print the tree again
    cs.remove_child(algo)  # This won't work as expected since it's a different instance
    print("After removing 'Algorithms':")
    print(cs)