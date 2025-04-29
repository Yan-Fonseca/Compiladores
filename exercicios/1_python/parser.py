

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.expr = []
        self.current = 0
    
    def parser(self):
        while !self.is_at_end():

    
    def term(self):
        expr = self.factor()
    
    def factor():
        expr = self.primary()

        while self.tokens[self.current].type == "SLASH" or self.tokens[self.current].type == "TIMES":
            
    
    def primary():
        current = self.tokens[self.current]
        if current.type == "NUMBER" or current.type == "IDENTIFIER":
            self.current += 1
            return self.tokens[self.current-1]
        else:
            print("[ERROR]")
            exit(1)

    
    def is_at_end(self):
        return self.tokens[self.current].type == "EOF"
