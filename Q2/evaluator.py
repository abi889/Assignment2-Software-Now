
def tokenize(expr):
    tokens = []
    i = 0

    while i < len(expr):
        c = expr[i]

        if c.isdigit():
            num = c
            i += 1
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1

            tokens.append(("NUM", num))

            #Checking for implicit multiplication
            if i < len(expr) and expr[i] == "(":
                tokens.append(("OP", "*"))

            continue

        elif c in "+-*/":
            tokens.append(("OP", c))

        elif c == "(":
            if tokens and (tokens[-1][0] == "NUM" or tokens[-1][0] == "RPAREN"):
                tokens.append(("OP", "*"))

            tokens.append(("LPAREN", c))

        elif c == ")":
            tokens.append(("RPAREN", c))

            if i + 1 < len(expr):
                next_c = expr[i + 1]
                if next_c.isdigit() or next_c == "(":
                    tokens.append(("OP", "*"))

        elif c == " ":
            i += 1
            continue

        else:
            return "ERROR"

        i += 1

    tokens.append(("END", ""))
    return tokens


#Parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos]

    def eat(self):
        self.pos += 1

    def parse(self):
        node = self.expr()
        return node

    def expr(self):
        node = self.term()

        while self.peek()[1] in ["+", "-"]:
            op = self.peek()[1]
            self.eat()
            node = (op, node, self.term())

        return node

    def term(self):
        node = self.factor()

        while self.peek()[1] in ["*", "/"]:
            op = self.peek()[1]
            self.eat()
            node = (op, node, self.factor())

        return node

    def factor(self):
        token = self.peek()

        if token[0] == "OP" and token[1] == "-":
            self.eat()
            return ("neg", self.factor())

        elif token[0] == "NUM":
            self.eat()
            return int(token[1])

        elif token[0] == "LPAREN":
            self.eat()
            node = self.expr()
            if self.peek()[0] != "RPAREN":
                raise Exception("Missing )")
            self.eat()
            return node

        else:
            raise Exception("Invalid")


#Tree String
def tree_to_str(node):
    if isinstance(node, int):
        return str(node)

    if node[0] == "neg":
        return f"(neg {tree_to_str(node[1])})"

    return f"({node[0]} {tree_to_str(node[1])} {tree_to_str(node[2])})"



#Evaluator
def evaluate(node):
    if isinstance(node, int):
        return node

    if node[0] == "neg":
        return -evaluate(node[1])

    left = evaluate(node[1])
    right = evaluate(node[2])

    if node[0] == "+":
        return left + right
    if node[0] == "-":
        return left - right
    if node[0] == "*":
        return left * right
    if node[0] == "/":
        if right == 0:
            raise Exception("Divide by zero")
        return left / right


#main evaluation function
def evaluate_file(input_path: str):
    results = []

    with open(input_path, "r") as f:
        lines = f.readlines()

    output_lines = []

    for line in lines:
        expr = line.strip()

        try:
            tokens = tokenize(expr)
            if tokens == "ERROR":
                raise Exception()
            
            parser = Parser(tokens)
            tree = parser.parse()
            
            tree_str = tree_to_str(tree)
            
            token_parts = []
            for t in tokens:
                if t[0] == "END":
                    token_parts.append("[END]")
                else:
                    token_parts.append(f"[{t[0]}:{t[1]}]")
            token_str = " ".join(token_parts)

        except:
            tree_str = "ERROR"
            token_str = "ERROR"
            result = "ERROR"
        else:
            try:
                result = evaluate(tree)
                
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 4)
                    
            except:
                result = "ERROR"

        output_lines.append(f"Input: {expr}")
        output_lines.append(f"Tree: {tree_str}")
        output_lines.append(f"Tokens: {token_str}")
        output_lines.append(f"Result: {result}")
        output_lines.append("")

        results.append({
            "input": expr,
            "tree": tree_str,
            "tokens": token_str,
            "result": result
        })

    with open("output.txt", "w") as f:
        f.write("\n".join(output_lines))

    return results