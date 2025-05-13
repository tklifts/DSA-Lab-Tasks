class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Insert a new node with the given value
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_recursive(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert_recursive(node.right, value)
            else:
                node.right = Node(value)
    
    # Search for a value in the tree
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node is not None
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    # Delete a node from the tree
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node to be deleted found
            # Case 1: Node has no child (leaf node)
            if node.left is None and node.right is None:
                node = None
            # Case 2: Node has one child
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            # Case 3: Node has two children
            else:
                # Get the in-order successor (smallest in the right subtree)
                min_node = self._min_value_node(node.right)
                node.value = min_node.value
                node.right = self._delete_recursive(node.right, min_node.value)
        return node
    
    # Find the node with the minimum value in the subtree
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    # Inorder traversal to print elements in ascending order
    def inorder_traversal(self):
        self._inorder_recursive(self.root)
        print()  # For new line after traversal
    
    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.value, end=" ")
            self._inorder_recursive(node.right)

# Test the BST implementation
bst = BinarySearchTree()

# Insert values
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# Inorder traversal (should print values in ascending order)
print("Inorder Traversal:")
bst.inorder_traversal()  # Expected Output: 20 30 40 50 60 70 80

# Search for a value
print("\nSearch for 40:")
print(bst.search(40))  # Expected Output: True
print("\nSearch for 100:")
print(bst.search(100))  # Expected Output: False

# Delete a node
print("\nDelete 20:")
bst.delete(20)
bst.inorder_traversal()  # Expected Output: 30 40 50 60 70 80

# Delete a node with one child (40 has no left child)
print("\nDelete 40:")
bst.delete(40)
bst.inorder_traversal()  # Expected Output: 30 50 60 70 80

# Delete a node with two children (50 has two children)
print("\nDelete 50:")
bst.delete(50)
bst.inorder_traversal()  # Expected Output: 30 60 70 80
