def is_valid_parentheses(s):
    stack=[]
    brackets={')':'(',
              '}': '{',
              ']':'[' 
              }
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
    return len(stack)==0
print("=== Valid Parenthesis Checker ===")
print("Examples:")
print("()")
print("({[]})")
s=input("Enter the parenthesis string: ")
if is_valid_parentheses(s):
    print("Output: True")
    print("The string is balanced.")
else:
    print("Output: False")
    print("The string is not balanced")