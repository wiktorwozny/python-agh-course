import string


def check(expr: str) -> bool:  # checking if expression is valid

    state = True  # true -> waiting for variable or opening bracket, false -> waiting for operator or closing bracket

    VAR = string.ascii_lowercase + 'T' + 'F'
    OPR = ['&', '|', '>', '^']

    for sign in expr:
        if state:
            if sign in VAR + '(':
                if sign == '(':
                    continue
                else:
                    state = False
            elif sign == '~':
                continue
            else:
                return False

        else:
            if sign in OPR or sign == ')':
                if sign == ')':
                    continue
                else:
                    state = True
            else:
                return False

    bracket_counter = 0
    for sign in expr:
        if sign == '(':
            bracket_counter += 1
        elif sign == ')':
            bracket_counter -= 1
            if bracket_counter < 0:
                return False

    return bracket_counter == 0 and not state


def bracket(expr: str) -> str:  # removing redundant brackets

    if expr == "":
        return ""
    while expr[0] == '(' and expr[-1] == ')' and check(expr[1:-1]):
        expr = expr[1:-1]

    return expr


def negation(expr: str) -> str:  # removing redundant negations

    new_expr = ''
    i = 0
    while i < len(expr):
        while i < len(expr) - 1 and expr[i] == expr[i + 1] == '~':
            i += 2
        new_expr += expr[i]
        i += 1

    return new_expr


def bal(expr: str, op: str):  # op is an array of operators with the same priority value

    bracket_counter = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ')':
            bracket_counter += 1
        if expr[i] == '(':
            bracket_counter -= 1
        if expr[i] in op and bracket_counter == 0:
            return i

    return None


def onp(expr: str) -> str:  # changing the expression to reverse polish notation

    expr = bracket(expr)
    expr = negation(expr)

    p = bal(expr, '>')
    if p is not None:
        return onp(expr[:p]) + onp(expr[p + 1:]) + expr[p]

    p = bal(expr, '&|')
    if p is not None:
        return onp(expr[:p]) + onp(expr[p + 1:]) + expr[p]

    p = bal(expr, '^')
    if p is not None:
        return onp(expr[:p]) + onp(expr[p + 1:]) + expr[p]

    p = bal(expr, '~')
    if p is not None:
        return onp(expr[:p]) + onp(expr[p + 1:]) + expr[p]

    return expr


def map(expr: str, vec: str) -> str:

    variables = []
    VAR = string.ascii_lowercase

    for char in expr:
        if char in VAR and char not in variables:
            variables.append(char)

    variables.sort()
    for i, var in enumerate(variables):
        expr = expr.replace(var, vec[i])
    expr = expr.replace('T', '1')
    expr = expr.replace('F', '0')

    return expr


def gen(n: int) -> list:

    tab = []
    for num in range(2 ** n):
        binary = str(bin(num)[2:])
        to_append = '0' * (n - len(binary))
        to_append += binary
        tab.append(to_append)

    return tab


def value(expr: str) -> int:

    stack = []
    for char in expr:
        if char in '01':
            stack.append(int(char))
        elif char == '~':
            stack.append(int(1 - stack.pop()))
        elif char == '|':
            stack.append(max(int(stack.pop()), int(stack.pop())))
        elif char == '&':
            stack.append(min(int(stack.pop()), int(stack.pop())))
        elif char == '>':
            stack.append(max(int(stack.pop()), 1 - int(stack.pop())))
        elif char == '^':
            p = stack.pop()
            q = stack.pop()
            stack.append(int((p and (1 - q)) or ((1 - p) and q)))

    return stack.pop()


def tautology(expr: str) -> bool:

    if not check(expr):
        print('ERROR')
        return False

    variables = []
    VAR = string.ascii_lowercase

    for char in expr:
        if char in VAR and char not in variables:
            variables.append(char)

    if len(variables) == 0:
        if value(onp(expr)):
            print('TAK')
            return True
        else:
            print('NIE')
            return False

    bins = gen(len(variables))
    for binary in bins:
        if not value(map(onp(expr), binary)):
            print('NIE')
            return False

    print('TAK')
    return True


if __name__ == '__main__':

    # tautology("(((~~r>(q&s)))&((p|s)>r))>(~q>~p)")
    # print(onp('p>(q>(p&q))'))
    # print(map(onp('p>(q>(p&q))'), '11'))

    tautology('(((~~r>(q&s)))&((p|s)>r))>(~q>~p)')
    tautology('p>(q>(p&q))')

    # print(onp(expr))
    # print(negation(expr))
    # bins = gen(4)
    # for binary in bins:
    #     print(value(map(onp(expr), binary)), binary)

    # print(value(map(onp('p>(q>(p&q))'), '00')))
