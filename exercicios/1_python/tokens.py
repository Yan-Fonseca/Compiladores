
class Token:
    def __init__(self, lexer, _type):
        self.lexer = lexer
        self.type = _type
        self.next = None
    
    def get_type(self):
        return self.type
    
    def get_lexer(self):
        return self.lexer
    
    def set_next(self, token):
        self.next = next
    
    def get_next(self):
        return self.next