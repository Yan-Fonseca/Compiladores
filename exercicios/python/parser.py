class Node:
    def __init__(self, left=None, right=None, token=None):
        self.left = left
        self.right = right
        self.token = token
    
    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_token(self):
        return self.token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.stmts = []
        self.current_token = 0
    
    def parsing(self):
        while not self.is_at_end():
            self.create_statement()
        return self.stmts
    
    def is_at_end(self):
        return self.tokens[self.current_token].type == "EOF"
    
    def create_statement(self):
        self.stmts.append(self.expr())
        self.end_stmt()
    
    def expr(self):
        if self.tokens[self.current_token + 1].type == "ASSIGN":
            return self.assign()
        else:
            return self.term()
    
    def assign(self):
        identifier = self.consume_token('IDENTIFIER')
        node_id = Node(token=identifier)

        assign = self.consume_token('ASSIGN')
        node = Node(token=assign)

        node.set_left(node_id)
        node.set_right(self.expr())

        return node

    def term(self):
        left = self.factor()
        type = self.get_type(['PLUS', 'MINUS'])

        if type == ' ':
            return left
        else:
            node = Node(token=self.consume_token(type))
            node.set_left(left)
            node.set_right(self.term())
            return node

    
    def factor(self):
        token_type = self.get_type(['IDENTIFIER', 'NUMBER'])
        if token_type == ' ':
            print('[ERROR] Fator esperado')
            exit(1)

        left = Node(token=self.consume_token(token_type))

        type = self.get_type(['TIMES', 'SLASH'])

        if type == ' ':
            return left
        else:
            node = Node(token=self.consume_token(type))
            node.set_left(left)
            node.set_right(self.factor())
            return node

    
    def end_stmt(self):
        aux = self.tokens[self.current_token]
        if aux.type == "SEMICOLON":
            self.current_token += 1
        else:
            print(f'[ERROR] {aux.lexeme} is not a Semicolon (;)')
            exit(1)

    def get_type(self, types):
        for i in range(0,len(types)):
            if self.tokens[self.current_token].type == types[i]:
                return types[i]
        return ' '

    def consume_token(self, type):
        aux = self.tokens[self.current_token]
        if aux.type == type:
            self.current_token += 1
            return self.tokens[self.current_token - 1]
        else:
            print(f'[ERROR] {aux.lexer} is invalid')
            exit(1)
    
    def print_tree(self, node, level=0):
        if node is None:
            return
        print('    ' * level + f'[{node.token.type}] {node.token.lexer}')
        self.print_tree(node.get_left(), level + 1)
        self.print_tree(node.get_right(), level + 1)

