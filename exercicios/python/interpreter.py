

class Interpreter:
    def __init__(self, stmts):
        self.stmts = stmts
        self.environment = {}
    
    def interpret(self):
        for i in range(0, len(self.stmts)):
            stmt = self.stmts[i]
            if stmt.get_token().type == 'ASSIGN':
                self.run(stmt)
            else:
                value = self.run(stmt)
                print(f'{value}')
    
    def run(self, stmt):
        if stmt.get_token().type == 'ASSIGN':
            return self.run_assign(stmt)
        else:
            return self.run_expr(stmt)
    
    def run_assign(self, stmt):
        identifier = stmt.get_left().get_token().lexer
        result = self.run(stmt.get_right())
        self.environment[identifier] = result
        return result
        
    def run_expr(self, expr):
        if expr.get_left() == None and expr.get_right() == None:
            if expr.get_token().type == 'IDENTIFIER':
                value = self.environment[expr.get_token().lexer]
                return value
            else:
                return int(expr.get_token().lexer)
        
        if expr.get_token().type == 'PLUS':
            return self.run_expr(expr.get_left()) + self.run_expr(expr.get_right())
        elif expr.get_token().type == 'MINUS':
            return self.run_expr(expr.get_left()) - self.run_expr(expr.get_right())
        elif expr.get_token().type == 'TIMES':
            return self.run_expr(expr.get_left()) * self.run_expr(expr.get_right())
        elif expr.get_token().type == 'SLASH':
            return self.run_expr(expr.get_left()) / self.run_expr(expr.get_right())