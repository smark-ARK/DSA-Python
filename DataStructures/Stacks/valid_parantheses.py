from Stack import Stack


def valid_parentheses(s: str):
    stack = Stack()
    for i in s:
        if i in ["{", "[", "("]:
            stack.push(i)
        else:
            c = stack.peek()
            if i == "}" and c == "{":
                stack.pop()
            elif i == "]" and c == "[":
                stack.pop()
            elif i == ")" and c == "(":
                stack.pop()
            else:
                return False
    return True if stack.is_empty() else False


s = "{[()]}"
print(valid_parentheses(s))
