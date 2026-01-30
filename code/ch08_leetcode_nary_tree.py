from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def parse_n_ary_tree(data):
    if not data:
        return None

    # Step 1: Initialize the root
    root = Node(data[0])
    queue = deque([root])
    
    # Pointer for the current element in the data list
    # We skip index 0 (root) and index 1 (the first null separator)
    i = 2
    
    while i < len(data) and queue:
        # Get the current parent node who needs children
        current_parent = queue.popleft()
        
        # Step 2: Process all children until the next 'null'
        while i < len(data) and data[i] is not None:
            child_node = Node(data[i])
            current_parent.children.append(child_node)
            queue.append(child_node)
            i += 1
        
        # Step 3: Skip the 'null' separator to move to the next parent's children
        i += 1
        
    return root

def serialize_n_ary_tree(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        current_node = queue.popleft()
        result.append(current_node.val)
        
        for child in current_node.children:
            queue.append(child)
        
        # Append 'null' to indicate the end of children for the current node
        result.append(None)
    
    # Remove the last 'null' if it exists
    if result and result[-1] is None:
        result.pop()
    
    return result

def print_preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    for child in root.children:
        print_preorder(child)

if __name__ == "__main__":
    # Example usage:
    data = [1, None, 3, 2, 4, None, 5, 6]
    root = parse_n_ary_tree(data)
    print_preorder(root)  # Output: 1 3 5 6 2 4
    print()
    data = [1, None, 2, 3, 4, None, 5, 6, None, None, 7]
    root = parse_n_ary_tree(data)
    serialized = serialize_n_ary_tree(root)
    print("Serialized N-ary Tree:", serialized)
    print("Preorder Traversal:", end=" ")
    print_preorder(root)
    print()