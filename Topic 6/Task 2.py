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
    
    # Find the Lowest Common Ancestor (LCA) of two nodes
    def find_LCA(self, n1, n2):
        return self._find_LCA_recursive(self.root, n1, n2)
    
    def _find_LCA_recursive(self, node, n1, n2):
        # If the tree is empty, return None
        if node is None:
            return None
        
        # If both nodes are smaller than the root, then LCA lies in the left subtree
        if n1 < node.value and n2 < node.value:
            return self._find_LCA_recursive(node.left, n1, n2)
        
        # If both nodes are greater than the root, then LCA lies in the right subtree
        if n1 > node.value and n2 > node.value:
            return self._find_LCA_recursive(node.right, n1, n2)
        
        # If one node is on the left and the other is on the right, then root is the LCA
        return node
    
    # Inorder traversal to print elements in ascending order
    def inorder_traversal(self):
        self._inorder_recursive(self.root)
        print()  # For new line after traversal
    
    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.value, end=" ")
            self._inorder_recursive(node.right)

# Test the BST and LCA function
bst = BinarySearchTree()

# Insert values
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(5)
bst.insert(15)
bst.insert(25)
bst.insert(35)

# Inorder traversal (should print values in ascending order)
print("Inorder Traversal:")
bst.inorder_traversal()  # Expected Output: 5 10 15 20 25 30 35

# Test LCA for different pairs of nodes
print("\nLCA of 5 and 15:")
lca = bst.find_LCA(5, 15)
print(f"LCA: {lca.value}")  # Expected Output: 10

print("\nLCA of 5 and 25:")
lca = bst.find_LCA(5, 25)
print(f"LCA: {lca.value}")  # Expected Output: 20

print("\nLCA of 25 and 35:")
lca = bst.find_LCA(25, 35)
print(f"LCA: {lca.value}")  # Expected Output: 30
