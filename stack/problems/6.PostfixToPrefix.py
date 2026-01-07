"""
===========================================================
Postfix to Prefix Conversion using Stack
===========================================================

Description:
------------
This module converts a postfix (Reverse Polish Notation)
expression into its equivalent prefix (Polish Notation)
expression using a stack.

Postfix notation places operators after operands, while
prefix notation places operators before operands. The
conversion reconstructs the expression tree structure
using stack operations.

Approach:
---------
1. Traverse the postfix expression from left to right.
2. Push operands directly onto the stack.
3. When an operator is encountered:
   - Pop the top two operands from the stack
   - Form a new prefix expression: operator + operand1 + operand2
   - Push the new expression back onto the stack
4. After traversal, the stack contains one element:
   the complete prefix expression.

Time Complexity:
----------------
O(n), where n is the length of the postfix expression.

Space Complexity:
-----------------
O(n), due to stack usage.

Mapped Concepts:
----------------
• Stack-based expression reconstruction
• Operand ordering
• Expression tree traversal
"""

def postfixToPrefix(s):
    stack = []
    for c in s:
        if c.isalnum():
            stack.append(c)
        else:
            b = stack.pop()
            a = stack.pop()
            expr = c+a+b
            stack.append(expr)
    return stack[-1] if stack else ""

tests = [
    ("AB+", "+AB"),
    ("ABC*+", "+A*BC"),
    ("AB+C*", "*+ABC"),
    ("ABC*+", "+A*BC"),
    ("ABC^^", "^A^BC")
]

for postfix, expected in tests:
    result = postfixToPrefix(postfix)
    print(f"Postfix : {postfix}")
    print(f"Prefix  : {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")
