"""
===========================================================
Postfix to Infix Conversion using Stack
===========================================================

Description:
------------
This module converts a postfix (Reverse Polish Notation)
expression into its equivalent infix expression using a stack.

The algorithm reconstructs the infix expression by preserving
the correct order of operations using parentheses.

This conversion is commonly used to:
- Understand expression parsing
- Visualize postfix expressions
- Prepare for stack-based interview problems

Approach:
---------
1. Traverse the postfix expression from left to right.
2. Push operands directly onto the stack.
3. When an operator is encountered:
   - Pop the top two operands from the stack
   - Form a new infix sub-expression: (operand1 operator operand2)
   - Push the new expression back onto the stack
4. After traversal, the stack contains one element:
   the complete infix expression.

Time Complexity:
----------------
O(n), where n is the length of the postfix expression.

Space Complexity:
-----------------
O(n) due to stack usage.

Notes:
------
• Parentheses are added aggressively to ensure correctness.
• Multiple valid infix expressions may exist for the same
  postfix expression.
• String comparison in tests should expect parentheses.

Mapped Concepts:
----------------
• Stack usage
• Expression parsing
• Operator precedence handling
"""

def postfixToInfix(s):
    stack = []
    for c in s:
        if c.isalnum():
            stack.append(c)
        else:
            b = stack.pop()
            a = stack.pop()
            expr = "(" + a + c + b + ")"
            stack.append(expr)
    return stack[-1] if stack else ""



def test_postfix_to_infix():
    tests = [
        ("(A+B)", "AB+"),
        ("(A+(B*C))", "ABC*+"),
        ("((A+B)*C)", "AB+C*"),
        ("((A+B)+C)", "AB+C+"),
        ("((A*B)+(C*D))", "AB*CD*+"),
        ("((A+B)*(C+D))", "AB+CD+*"),
        ("(A+(B+(C*(D+E))))", "ABCDE+*++"),
        ("(A^(B^C))", "ABC^^")
    ]

    for expected_infix, postfix in tests:
        result = postfixToInfix(postfix)
        print(f"Postfix : {postfix}")
        print(f"Infix   : {result}")
        print(f"Expected: {expected_infix}")
        print("PASS\n" if result == expected_infix else "FAIL\n")

test_postfix_to_infix()
