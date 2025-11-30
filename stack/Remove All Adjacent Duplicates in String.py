""" 
===========================================================
Remove All Adjacent Duplicates in String  (Stack Pattern)
===========================================================

🧩 Problem:
Given a string `s`, repeatedly remove all pairs of **adjacent duplicate characters**.
Return the final string after all such deletions are done.

Example:
---------
Input:  "abbaca"
Process:
    "abbaca"
     ⬆⬆  -> remove "bb"
    "aaca"
      ⬆⬆ -> remove "aa"
    "ca"

Output: "ca"

-----------------------------------------------------------
🧠 Pattern: Stack (String + Adjacent Removal)
-----------------------------------------------------------

Idea:
- Use a stack to track characters.
- For each character:
  - If the stack is not empty and the top equals the current character,
    we found a duplicate → pop the top (remove pair).
  - Otherwise, push the current character.
- In the end, the stack contains the string with all adjacent duplicates removed.

-----------------------------------------------------------
✅ Python Solution
-----------------------------------------------------------

```python
"""
def remove_duplicates(s: str) -> str:
    """
    Remove all adjacent duplicates in a string using a stack.

    Args:
        s (str): Input string

    Returns:
        str: String after removing all adjacent duplicates

    Example:
        >>> remove_duplicates("abbaca")
        'ca'
    """
    stack = []

    for c in s:
        # If stack not empty and top is same as current char, pop it
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    # Stack holds characters in order
    return "".join(stack)


if __name__ == "__main__":
    print(remove_duplicates("abbaca"))  # ca
