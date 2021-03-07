# Forth

def calculate_back():
    stack = []
    operator = ['+', '-', '*', '/']
    for i in string_list:

        if i in operator:
            if len(stack) >= 2:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if i == '+':
                    stack.append(num1 + num2)
                elif i == '-':
                    stack.append(num1 - num2)
                elif i == '*':
                    stack.append(num1 * num2)
                elif i == '/':
                    stack.append(num1 // num2)
            else:
                return 'error'
        else:
            stack.append(i)

    if stack[-1] == '.' and len(stack) == 2:
        return stack[0]

    return 'error'

T = int(input())

for tc in range(1, T + 1):
    string_list = input().split()
    a = calculate_back()
    print('#%d ' % (tc) + str(a))
