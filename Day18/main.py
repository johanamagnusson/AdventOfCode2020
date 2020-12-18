import queue

with open("data", "r") as fh:
    lines = fh.read().splitlines()


def compute_RPN(seq):
    i = 0
    news = seq
    while len(news) > 1:
        if news[i] == "*":
            num = news[i-1] * news[i-2]
            news[i] = num
            news.pop(i-1)
            news.pop(i-2)
            i = 0
        elif news[i] == "+":
            num = news[i-1] + news[i-2]
            news[i] = num
            news.pop(i-1)
            news.pop(i-2)
            i = 0
        i+=1
    return news[0]

def greater(operation, token):
    if operation == "+" and token == "*":
        return True
    return False

s = 0
p = 2
for line in lines:
    tokens = []
    output = []
    operator = []
    for c in line.split(" "):
        if c in ["*", "+"]:
            tokens.append(c)
        elif "(" in c:
            for cc in c[:c.count("(")]:
                tokens.append(cc)
            tokens.append(int(c.replace("(","")))
        elif ")" in c:
            tokens.append(int(c.replace(")","")))
            for cc in c[len(c)-c.count(")"):]:
                tokens.append(cc)
        else:
            tokens.append(int(c))

    if p == 1:
        while tokens:
            token = tokens.pop(0)
            try:
                num = int(token)
                output.append(num)
            except ValueError:
                if token in ["*", "+"]:
                    while operator and operator[0] != "(":
                        output.append(operator.pop(0))
                    operator.insert(0, token)
                elif token == "(":
                    operator.insert(0, token)
                elif token == ")":
                    while True:
                        if operator[0] == "(":
                            operator.pop(0)
                            break
                        output.append(operator.pop(0))
        while operator:
            output.append(operator.pop(0))

    elif p == 2:
        while tokens:
            token = tokens.pop(0)
            try:
                num = int(token)
                output.append(num)
            except ValueError:
                if token in ["*", "+"]:
                    while operator and operator[0] != "(" and greater(operator[0], token):
                        output.append(operator.pop(0))
                    operator.insert(0, token)
                elif token == "(":
                    operator.insert(0, token)
                elif token == ")":
                    while True:
                        if operator[0] == "(":
                            operator.pop(0)
                            break
                        output.append(operator.pop(0))
        while operator:
            output.append(operator.pop(0))

    s += compute_RPN(output)
print("Part {}: ".format(p), s)
