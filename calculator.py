import operator

import sys

from stack import Stack


def build_rpn(expression):
    priority = {
        '(': 0, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4
    }
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
                while not stack.is_empty() and priority[c] <= priority[stack.peek()]:
                    rpn_expression += stack.pop()
                stack.push(c)
    while not stack.is_empty():
        rpn_expression += stack.pop()
    return rpn_expression


def calculate(expression):
    operators = {
        '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow
    }

    rpn_expression = build_rpn(expression)
    stack = Stack()
    i = 0
    while i < len(rpn_expression):
        if rpn_expression[i].isdigit():
            number = rpn_expression[i]
            while rpn_expression[i + 1].isdigit():
                i += 1
                number += rpn_expression[i]
            stack.push(float(number))
        elif rpn_expression[i] in operators:
            right_operand = stack.pop()
            left_operand = stack.pop()
            operation = rpn_expression[i]
            stack.push(operators[operation](left_operand, right_operand))
        i += 1
    return float(stack.pop())


def main():
    if len(sys.argv) == 2:
        print(calculate(sys.argv[1]))
    else:
        print('Usage: calculator.py "expression"')


if __name__ == '__main__':
    main()
