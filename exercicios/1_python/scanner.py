from token import Token

class Scanner:
    def __init__(self, data):
        self.tokens = []
        self.data = data
        self.current = 0
    
    def scan_tokens(self):
        while !self.is_at_end():
            self.scan_token()
        
        self.tokens.push(Token("EOF", "EOF"))
    
    def scan_token():
        character = self.advance()

        if character == '=':
            self.tokens.push(Token(character, "ASSIGN"))
        elif character == ';':
            self.tokens.push(Token(character, "SEMICOLON"))
        elif character == '+':
            self.tokens.push(Token(character, "PLUS"))
        elif character == '-':
            self.tokens.push(Token(character, "MINUS"))
        elif character == '*':
            self.tokens.push(Token(character, "TIMES"))
        elif character == '/':
            self.tokens.push(Token(character, "SLASH"))
        elif character.isdigit():
            self.number()
        elif character.isalpha():
            self.identifier()
        else:
            print("[ERROR] caractere Inválido")
    
    def number(self):
        num = ""
        num += self.data[self.current - 1]
        while self.data[self.current].isdigit():
            num += self.advance()
        
        self.tokens.push(Token(num, "NUMBER"))
    
    def identifier(self):
        ident = ""
        ident += self.data[self.current - 1]
        while self.data[self.current].isdigit():
            ident += self.advance()
        
        self.tokens.push(Token(ident, "IDENTIFIER"))

    def advance(self):
        self.current += 1
        return self.data[self.current-1]
    
    def is_at_end(self):
        return self.current == len(self.data) - 1

    def get_tokens(self):
        return self.tokens