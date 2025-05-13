class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Helper function to check if the tree is balanced
    def is_balanced(self, node):
        # Recursive function to check height and balance of tree
        def check_balance(node):
            if node is None:
                return 0  # Base case: height of an empty subtree is 0

            # Recursively check the height of the left and right subtrees
            left_height = check_balance(node.left)
            if left_height == -1:  # If the left subtree is unbalanced, propagate -1
                return -1

            right_height = check_balance(node.right)
            if right_height == -1:  # If the right subtree is unbalanced, propagate -1
                return -1

            # If the current node is unbalanced, return -1
            if abs(left_height - right_height) > 1:
                return -1

            # Return the height of the current node's subtree
            return max(left_height, right_height) + 1

        # Start the check from the root
        return check_balance(node) != -1

# Test Cases

# Balanced Tree
bt1 = BinaryTree()
bt1.root = Node(10)
bt1.root.left = Node(5)
bt1.root.right = Node(15)
bt1.root.left.left = Node(2)
bt1.root.left.right = Node(7)
bt1.root.right.left = Node(12)
bt1.root.right.right = Node(20)

# Unbalanced Tree
bt2 = BinaryTree()
bt2.root = Node(10)
bt2.root.left = Node(5)
bt2.root.left.left = Node(2)

# Testing the balanced check function
print("Tree 1 is balanced:", bt1.is_balanced(bt1.root))  # Expected Output: True
print("Tree 2 is balanced:", bt2.is_balanced(bt2.root))  # Expected Output: False
