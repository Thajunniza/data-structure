"""
# Determine whether or not a set of brackets are balanced
A balanced set of brackets is one where the number and type of opening and closing brackets match and that is also properly nested within the string of brackets.

Examples of Balanced Brackets
{ }
{ } { }
( ( { [ ] } ) )
Examples of Unbalanced Brackets
( ( )
{ { { ) } ]
[ ] [ ] ] ]
"""


class Stack:
    def __init__(self):
        self.items = []

    # inserts an item
    def push(self, item):
        self.items.append(item)

    # gives the last item
    def pop(self):
        return self.items.pop()

    # returns all item
    def getStack(self):
        return self.items

    # check if the arrayis empty
    def isEmpty(self):
        return self.items == []

    # Returns the last element of the list
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]


def is_match(open, close):
    if open == "(" and close == ")":
        return True
    if open == "{" and close == "}":
        return True
    if open == "[" and close == "]":
        return True
    else:
        return False


def isParenBalanced(parenString):
    s = Stack()
    isBalance = True
    i = 0
    openParen = "({["
    while i < len(parenString) and isBalance:
        c = parenString[i]
        if c in openParen:
            s.push(c)
        else:
            if s.isEmpty():
                isBalance = False
                break
            else:
                if not is_match(s.pop(), c):
                    isBalance = False

        i += 1

    if isBalance and s.isEmpty():
        return True
    else:
        return False


print("String : (((({})))) Balanced or not?")
print(isParenBalanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(isParenBalanced("[][]]]"))

print("String : [][] Balanced or not?")
print(isParenBalanced("[][]"))
