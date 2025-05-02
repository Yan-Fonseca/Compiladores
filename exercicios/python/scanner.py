from tokens import Token

class Scanner:
    def __init__(self, data):
        self.tokens = []
        self.data = data
        self.current = 0
    
    def scan_tokens(self):
        while not self.is_at_end():
            self.scan_token()
        
        self.tokens.append(Token("EOF", "EOF"))
    
    def scan_token(self):
        character = self.advance()

        if character == '=':
            self.tokens.append(Token(character, "ASSIGN"))
        elif character == ';':
            self.tokens.append(Token(character, "SEMICOLON"))
        elif character == '+':
            self.tokens.append(Token(character, "PLUS"))
        elif character == '-':
            self.tokens.append(Token(character, "MINUS"))
        elif character == '*':
            self.tokens.append(Token(character, "TIMES"))
        elif character == '/':
            self.tokens.append(Token(character, "SLASH"))
        elif character.isdigit():
            self.number()
        elif character.isalpha():
            self.identifier()
        elif character == ' ' or character == '\n' or character == '\t':
            pass
        else:
            print(f'[ERROR] caractere Inválido: {character}')
    
    def number(self):
        num = ""
        num += self.data[self.current - 1]
        while not self.is_at_end() and self.data[self.current].isdigit():
            num += self.advance()
        
        self.tokens.append(Token(num, "NUMBER"))
    
    def identifier(self):
        ident = ""
        ident += self.data[self.current - 1]
        while not self.is_at_end() and self.data[self.current].isalnum():
            ident += self.advance()
        
        self.tokens.append(Token(ident, "IDENTIFIER"))

    def advance(self):
        self.current += 1
        return self.data[self.current-1]
    
    def is_at_end(self):
        return self.current == len(self.data)

    def get_tokens(self):
        return self.tokens