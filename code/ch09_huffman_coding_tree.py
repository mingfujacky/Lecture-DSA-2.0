class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # The character (None for internal nodes)
        self.freq = freq  # The frequency/count
        self.left = None
        self.right = None


class HuffmanTree:
    def __init__(self, frequency_dict):
        self.root = self._build_tree(frequency_dict)
        self.codes = {}
        if self.root:
            self._generate_codes(self.root, "")

    def _build_tree(self, freq_dict):
        # 1. Create a list of leaf nodes
        nodes = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]

        # 2. Loop until only one node (the root) remains
        while len(nodes) > 1:
            # Sort nodes by frequency (Ascending)
            nodes.sort(key=lambda x: x.freq)

            # Pick the two nodes with the lowest frequencies
            left_node = nodes.pop(0)
            right_node = nodes.pop(0)

            # Create a new internal node with their combined frequency
            parent = HuffmanNode(None, left_node.freq + right_node.freq)
            parent.left = left_node
            parent.right = right_node

            # Add the new node back to the list
            nodes.append(parent)

        return nodes[0] if nodes else None

    def _generate_codes(self, node, current_code):
        """Recursively traverses the tree to assign 0s and 1s."""
        if node is None:
            return

        # If it's a leaf node, save its code
        if node.char is not None:
            self.codes[node.char] = current_code

        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def get_codes(self):
        return self.codes

    # Sample data: Character frequencies in a message


data = {"A": 45, "B": 13, "C": 12, "D": 16, "E": 9, "F": 5}

# Build the tree
huffman = HuffmanTree(data)

# Print the resulting binary codes
print("Huffman Codes:")
for char, code in huffman.get_codes().items():
    print(f"{char}: {code}")
