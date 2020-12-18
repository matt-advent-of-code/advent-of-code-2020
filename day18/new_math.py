global tokens
tokens = []

operators = ['+', '*']


def calculate(expression: str) -> int:
    global tokens
    tokens = list(expression.replace(' ', ''))
    return operate()

def left():
    if tokens[0] == '(':
        return paranthenses()
    else:
        return tokens.pop(0)

def right():
    return left()

def paranthenses():
    tokens.pop(0)
    value = operate()
    tokens.pop(0)
    return value


def operate():
    if len(tokens) == 1:
        return tokens.pop(0)
    l = int(left())
    if len(tokens) == 0:
        return l
    operator = tokens.pop(0)

    if operator == '+':
        total = l + int(right())
    if operator == '*':
        total = l * int(right())

    if len(tokens) > 0 and tokens[0] == ')':
        return total
    tokens.insert(0, total)
    return operate()


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
