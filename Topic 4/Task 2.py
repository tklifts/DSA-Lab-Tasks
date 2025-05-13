# Function to evaluate a postfix expression
def evaluate_postfix(expression):
    stack = []

    # Split the expression into tokens (numbers and operators)
    tokens = expression.split()

    # Loop through each token
    for token in tokens:
        if token.isdigit():  # If it's a number, push it to the stack
            stack.append(int(token))
        else:  # Otherwise, it's an operator, so pop two elements and apply the operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2  # Handle division
            
            # Push the result back to the stack
            stack.append(result)
    
    # The final result will be the only element in the stack
    return stack.pop()

# Test cases for the evaluate_postfix function
def test_postfix():
    # Test case 1
    expression = "5 1 2 + 4 * + 3 -"
    print(f"Expression: {expression}")
    print("Result:", evaluate_postfix(expression))  # Expected Output: 14

    # Test case 2: "3 4 + 2 * 7 /"
    expression = "3 4 + 2 * 7 /"
    print(f"\nExpression: {expression}")
    print("Result:", evaluate_postfix(expression))  # Expected Output: 2.0

    # Test case 3: "10 2 8 * + 3 -"
    expression = "10 2 8 * + 3 -"
    print(f"\nExpression: {expression}")
    print("Result:", evaluate_postfix(expression))  # Expected Output: 23

    # Test case 4: "2 3 + 5 6 + *"
    expression = "2 3 + 5 6 + *"
    print(f"\nExpression: {expression}")
    print("Result:", evaluate_postfix(expression))  # Expected Output: 45

    # Test case 5: "3 4 2 * 1 5 - 2 3 ^ ^ / +"
    expression = "3 4 2 * 1 5 - 2 3 ^ ^ / +"
    print(f"\nExpression: {expression}")
    print("Result:", evaluate_postfix(expression))  # Expected Output: 3.0001220703125

# Run the test cases
if __name__ == "__main__":
    test_postfix()
