"""
===========================================================
PREFIX TO POSTFIX CONVERSION USING STACK
===========================================================

Description:
------------
This module converts a Prefix expression into a Postfix
expression using a stack-based approach.

Prefix notation places operators before operands,
while Postfix notation places operators after operands.

The algorithm processes the Prefix expression from
right to left and uses a stack to build the Postfix
expression.

Key Concepts Used:
------------------
- Stack (LIFO)
- Expression parsing
- Operand vs Operator handling

Time Complexity:
----------------
O(n), where n is the length of the expression

Space Complexity:
-----------------
O(n) for stack storage

Use Case:
---------
Commonly asked in:
- Data Structures & Algorithms interviews
- Stack-based expression problems
- Compiler design basics
- LeetCode / Coding interviews
"""

def prefixToPostfix(s):
    stack =[]
    for c in s:
        if c.isalnum():
            stack.append(c)
        else:
            a = stack.pop()
            b = stack.pop()
            expr = a + b + c
            stack.append(expr)
    return stack[-1] if stack else ""

tests = [
    ("+AB", "AB+"),
    ("+A*BC", "ABC*+"),
    ("*+ABC", "AB+C*"),
    ("^A^BC", "ABC^^")
]

for prefix, expected in tests:
    result = prefixToPostfix(prefix)
    print(f"Prefix  : {prefix}")
    print(f"Postfix : {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")
