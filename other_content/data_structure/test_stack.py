from stack import Stack

def checkBalance(s):
    myStack = Stack(len(s))
    for ch in s:
        if ch == '(' or ch == '{':
            myStack.push(ch)
        else:
            if myStack.is_empty():
                return False
            elif ch==')' and myStack.peek() !='(':
                return False
            elif ch=='}' and myStack.peek() !='{':
                return False
            myStack.pop()
    if myStack.is_empty():
        return True
    return False


print(checkBalance("()()(())"))
print(checkBalance("({{(){}}})"))
print(checkBalance("({{({}))}}"))
