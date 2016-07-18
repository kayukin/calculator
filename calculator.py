from stack import Stack


def get_operation_priority(operation):
    priority = 0
    if operation == '(':
        priority = 0
    elif operation == ')':
        priority = 1
    elif operation == '+' or operation == '-':
        priority = 2
    elif operation == '*' or operation == '/':
        priority = 3
    elif operation == '^':
        priority = 4
    return priority


def build_rpn(expression):
    stack = Stack()
    rpn_expression = ''
    num = False
    for c in expression:
        if c.isdigit():
            rpn_expression += c
            num = True
        else:
            if num:
                rpn_expression += ' '
                num = False
            if c == '(':
                stack.push(c)
            elif c == ')':
                while stack.peek() != '(':
                    rpn_expression += stack.pop()
                stack.pop()
            elif c in ['+', '-', '*', '/', '^']:
                while not stack.isEmpty() and get_operation_priority(c) <= get_operation_priority(stack.peek()):
                    rpn_expression += stack.pop()
                stack.push(c)
    while not stack.isEmpty():
        rpn_expression += stack.pop()
    return rpn_expression


def calc(left_operand, right_operand, operation):
    left_operand = float(left_operand)
    right_operand = float(right_operand)
    if operation == '^':
        print("br")
    if operation == '+':
        return left_operand + right_operand
    elif operation == '-':
        return left_operand - right_operand
    elif operation == '*':
        return left_operand * right_operand
    elif operation == '/':
        return left_operand / right_operand
    elif operation == '^':
        return left_operand ** right_operand


def calculate(expression):
    rpn_expression = build_rpn(expression)
    stack = Stack()
    i = 0
    while i < len(rpn_expression):
        if rpn_expression[i].isdigit():
            number = rpn_expression[i]
            while rpn_expression[i + 1].isdigit():
                i += 1
                number += rpn_expression[i]
            stack.push(number)
        elif rpn_expression[i] in ['+', '-', '*', '/', '^']:
            right_operand = stack.pop()
            left_operand = stack.pop()
            stack.push(calc(left_operand, right_operand, rpn_expression[i]))
        i += 1
    return float(stack.pop())


def main():
    print(calculate("34 + 4 * 2 / (1 - 5)^2"))


if __name__ == '__main__':
    main()
