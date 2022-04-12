def parentheses_checker(s):
    stack = []

    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char)

        else:

            if not stack:
                return False

            popped_char = stack.pop()

            if popped_char == '(':
                if char != ')':
                    return False

            if popped_char == '{':
                if char != '}':
                    return False

            if popped_char == '[':
                if char != ']':
                    return False
    if stack:
        return False
    else:
        return True


s = "(({[]})})"
res = parentheses_checker(s)
if res:
    print('Balanced')
else:
    print('not balanced')
