def calculate(expression: str) -> int:
    expression = eval_paren(expression.replace(' ', ''))
    expression = eval_plus(expression)
    return int(eval_multiply(expression))


def eval_plus(expression: str) -> str:
    while '+' in expression:
        i = expression.index('+')
        left_start_index = i - 1
        while expression[left_start_index -1].isnumeric() and left_start_index - 1 >= 0:
            left_start_index = left_start_index - 1
        left = int(expression[left_start_index:i])

        right_end_index = i + 1
        while right_end_index + 1 < len(expression) and expression[right_end_index + 1].isnumeric():
            right_end_index += 1
        right = int(expression[i:right_end_index +1])

        total = int(left) + int(right)
        expression = ''.join(list(expression[: left_start_index])) + str(total) + ''.join(list(expression[right_end_index + 1:]))
    return expression

def eval_multiply(expression: str) -> str:
    while '*' in expression:
        i = expression.index('*')
        left_start_index = i - 1
        while expression[left_start_index -1].isnumeric() and left_start_index - 1 >= 0:
            left_start_index = left_start_index - 1
        left = int(expression[left_start_index:i])

        right_end_index = i + 1
        while right_end_index + 1 < len(expression) and expression[right_end_index + 1].isnumeric():
            right_end_index += 1
        right = int(expression[i + 1:right_end_index +1])

        total = int(left) * int(right)
        expression = ''.join(list(expression[: left_start_index])) + str(total) + ''.join(list(expression[right_end_index + 1:]))
    return expression

def eval_paren(expression: str) -> str:
    paren_stack = []
    while '(' in expression:
        i = expression.index('(')
        paren_stack.append('(')
        for j in range(i + 1, len(list(expression))):
            if expression[j] == '(':
                paren_stack.append('(')
            if expression[j] == ')':
                paren_stack.pop()
                if len(paren_stack) == 0:
                    sub_expression = expression[i+1:j]
                    sub_expression = calculate(sub_expression)
                    expression = ''.join(expression[:i]) + str(sub_expression) + ''.join(expression[j+1:])
                    break
    return expression


if __name__ == '__main__':
    with open('input.txt') as data:
        total = 0
        for line in data.readlines():
            total += calculate(line.strip('\n'))

        print(total)

## parse -> num
## parse -> (
## num -> left + parse
## num -> left * parse
## num -> number
## ( -> parse )
