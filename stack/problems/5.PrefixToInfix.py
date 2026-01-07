"""
===========================================================
Prefix to Infix Conversion using Stack
===========================================================

Description:
------------
This module converts a prefix (Polish Notation) expression
into its equivalent infix expression using a stack.

Prefix notation places operators before operands and removes
the need for parentheses. During conversion, parentheses are
added to preserve the correct order of evaluation.

This is a classic stack problem and a mirror image of
postfix → infix conversion.

Approach:
---------
1. Traverse the prefix expression from right to left.
2. Push operands directly onto the stack.
3. When an operator is encountered:
   - Pop the top two operands from the stack
   - Combine them as: (operand1 operator operand2)
   - Push the new expression back onto the stack
4. The final stack element is the infix expression.

Time Complexity:
----------------
O(n), where n is the length of the expression.

Space Complexity:
-----------------
O(n), due to stack usage.

Mapped Concepts:
----------------
• Stack traversal
• Expression parsing
• Operator precedence handling
"""

def prefixToInfix(s):
    stack = []
    i = len(s) - 1
    while i >= 0:
        c = s[i]
        if c.isalnum():
            stack.append(c)
        else:
            a = stack.pop()
            b = stack.pop()
            expr = "(" + a + c + b + ")"
            stack.append(expr)
        i -= 1
    return stack[-1] if stack else ""

tests = [
    ("+AB", "(A+B)"),
    ("+A*BC", "(A+(B*C))"),
    ("*+ABC", "((A+B)*C)"),
    ("^A^BC", "(A^(B^C))"),
    ("*+A/BC-A/KL", "((A+(B/C))*(A-(K/L)))")
]

for prefix, expected in tests:
    result = prefixToInfix(prefix)
    print(f"Prefix : {prefix}")
    print(f"Infix  : {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")
