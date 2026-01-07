"""
===========================================================
Infix to Prefix Conversion using Stack
===========================================================

Description:
------------
This module converts an infix expression into its equivalent
prefix (Polish Notation) expression using a stack-based method.

Prefix notation places the operator before its operands and
eliminates the need for parentheses. This conversion is a
standard stack problem and frequently appears in interviews
as a variation of infix-to-postfix.

Approach Used (Reverse Method):
-------------------------------
1. Reverse the infix expression.
2. Swap '(' with ')'.
3. Convert the modified expression to postfix.
4. Reverse the postfix result to obtain prefix.

This approach is preferred in interviews because it reuses
the infix → postfix logic and avoids complex direct parsing.

Time Complexity:
----------------
O(n), where n is the length of the expression.

Space Complexity:
-----------------
O(n), due to stack and output storage.

Mapped Concepts:
----------------
• Stack usage
• Operator precedence and associativity
• Expression parsing

Related Interview Problems:
---------------------------
• LeetCode 150 – Evaluate Reverse Polish Notation
• LeetCode 224 – Basic Calculator
• LeetCode 227 – Basic Calculator II
"""
def infixToPrefix(s):
    stack= []
    output = []
    precedence ={
        "^" : 3,
        "/" : 2,
        "*" : 2,
        "-" : 1,
        "+" : 1
    }
    i = len(s) - 1
    while i >= 0:
        c = s[i]
        if c.isalnum():
            output.append(c)
        elif c == ")":
            stack.append(c)
        elif c == "(":
            while stack and stack[-1] != ")":
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != ")" and (precedence[stack[-1]] > precedence[c] 
                                              or (precedence[stack[-1]] == precedence[c] and c != "^"))):
                output.append(stack.pop())
            stack.append(c)   
        i -= 1
    
    while stack:
        output.append(stack.pop())
    return "".join(output[::-1])

tests = [
    ("A+B", "+AB"),
    ("A+B*C", "+A*BC"),
    ("(A+B)*C", "*+ABC"),
    ("A+(B*C)", "+A*BC"),
    ("A^B^C", "^^ABC"),
    ("(A+B/C)*(A-K/L)", "*+A/BC-A/KL")
]

for infix, expected in tests:
    result = infixToPrefix(infix)
    print(f"Infix  : {infix}")
    print(f"Prefix : {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")

    