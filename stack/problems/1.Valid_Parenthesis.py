
"""
===========================================================
VALID PARENTHESES CHECK USING STACK
===========================================================
Given a string containing parentheses:
    (), {}, []

Check whether the parentheses are valid:
- Open brackets must be closed by the same type
- Brackets must be closed in correct order

Time Complexity : O(n)
Space Complexity: O(n)
===========================================================
"""
def isValidParen(s):
    matching = {
       ")" : "(",
       "]" : "[",
       "}" : "{"
    }
    stack = []
    for c in s:
        if c in matching.values():
            stack.append(c)
        elif c in matching:
            if stack and stack[-1] == matching[c]:
                stack.pop()
            else:
                return False
        else:
            return False
    return len(stack) == 0
            
        
    


print("String : (((({})))) Balanced or not?")
print(isValidParen("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(isValidParen("[][]]]"))

print("String : [][] Balanced or not?")
print(isValidParen("[][]"))