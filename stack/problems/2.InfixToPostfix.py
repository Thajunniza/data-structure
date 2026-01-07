"""
===========================================================
Infix to Postfix Conversion using Stack
===========================================================

Description:
------------
This module converts an infix expression into its equivalent
postfix (Reverse Polish Notation) expression using a stack.

The algorithm correctly handles:
- Operator precedence
- Operator associativity (including right-associative '^')
- Parentheses
- Alphanumeric operands

This conversion is a foundational step in expression evaluation
and is widely used in compilers, interpreters, and calculator
implementations.

Approach:
---------
1. Traverse the infix expression from left to right.
2. Append operands directly to the output.
3. Push '(' onto the stack.
4. On ')', pop operators until '(' is encountered.
5. For operators:
   - Pop from stack based on precedence and associativity rules.
   - Push the current operator onto the stack.
6. After traversal, pop all remaining operators from the stack.

Key Rule:
---------
- Left-associative operators (+, -, *, /):
  pop while precedence(stack_top) >= precedence(current)
- Right-associative operator (^):
  pop while precedence(stack_top) > precedence(current)

Time Complexity:
----------------
O(n), where n is the length of the expression.

Space Complexity:
-----------------
O(n) for the stack and output list.

Test Coverage:
--------------
Includes test cases for:
- Basic expressions
- Operator precedence
- Parentheses
- Nested expressions
- Right-associative exponent operator (^)

Mapped Interview Problems:
--------------------------
- LeetCode 150: Evaluate Reverse Polish Notation
- LeetCode 224: Basic Calculator
- LeetCode 227: Basic Calculator II

Author Notes:
-------------
Designed for repeated revision, interview preparation,
and clean demonstration of stack-based expression parsing.
"""

def infixToPostfix(s):
    if not s :
        return ""
    output = []
    stack = []
    precedence = {
        "^" : 3,
        "/" : 2,
        "*" : 2,
        "-" : 1,
        "+" : 1
    }
    for c in s:
        if c.isalnum():
            output.append(c)
        elif c == "(":
            stack.append(c)
        elif c == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != "(" and (precedence[stack[-1]] > precedence[c] or
                    (precedence[stack[-1]] == precedence[c] and c != "^")):
                output.append(stack.pop())
            stack.append(c)
    
    while stack:
        output.append(stack.pop())
    return "".join(output)

def test_infix_to_postfix():
    tests = [
        ("A+B", "AB+"),
        ("A+B*C", "ABC*+"),
        ("(A+B)*C", "AB+C*"),
        ("A+(B*C)", "ABC*+"),
        ("A+B+C", "AB+C+"),
        ("A*B+C*D", "AB*CD*+"),
        ("(A+B)*(C+D)", "AB+CD+*"),
        ("A+(B+C*(D+E))", "ABCDE+*++"),
        ("A^B^C", "ABC^^"),          # right associative
        ("(A+B/C)*(A/K-L)", "ABC/+AK/L-*")
    ]

    for infix, expected in tests:
        result = infixToPostfix(infix)
        print(f"Infix   : {infix}")
        print(f"Postfix : {result}")
        print(f"Expected: {expected}")
        print("PASS\n" if result == expected else "FAIL\n")

test_infix_to_postfix()