from abc import ABC, abstractmethod

class Context:
    def __init__(self):
        self._variables = {}

    def set_variable(self, name, value):
        self._variables[name] = value

    def get_variable(self, name):
        if name not in self._variables:
            raise KeyError(f"Variable with name {name} not found")

        return self._variables[name]

class Expression(ABC):
    @abstractmethod
    def interpret(self, context: Context) -> int:
        pass

class Number(Expression):
    def __init__(self, value):
        self._value = value

    def interpret(self, context: Context) -> int:
        return int(self._value)

class Variable(Expression):
    def __init__(self, name):
        self._name = name

    def interpret(self, context: Context) -> int:
        return context.get_variable(self._name)

class Add(Expression):
    def __init__(self, left, right):
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> int:
        return self._left.interpret(context) + self._right.interpret(context)

class Sub(Expression):
    def __init__(self, left, right):
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> int:
        return self._left.interpret(context) - self._right.interpret(context)

def infix_to_postfix(expression: str) -> str:
    """Konwertuje wyrażenie z notacji infiksowej na postfiksową (RPN)
    używając algorytmu Shunting Yard (Dijkstry)"""
    tokens = expression.split()
    output = []
    operator_stack = []

    precedence = {'+': 1, '-': 1}

    for token in tokens:
        if token.isdigit() or token.isalpha():
            output.append(token)
        elif token in precedence:
            while (operator_stack and
                   operator_stack[-1] in precedence and
                   precedence[operator_stack[-1]] >= precedence[token]):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()  # usuń '('

    while operator_stack:
        output.append(operator_stack.pop())

    return ' '.join(output)


def parse_expression(expression: str) -> Expression:
    """Parsuje wyrażenie w notacji infiksowej"""
    # Konwertuj na notację postfiksową (RPN)
    postfix = infix_to_postfix(expression)
    tokens = postfix.split()
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(Number(token))
        elif token.isalpha():
            stack.append(Variable(token))
        elif token in ['+', '-']:
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(Add(left, right))
            else:
                stack.append(Sub(left, right))

    return stack[0]

if __name__ == "__main__":
    context = Context()
    context.set_variable("x", 10)
    context.set_variable("y", 20)

    expression = parse_expression("x + y + 5 - 2 + x")
    print(expression.interpret(context))
