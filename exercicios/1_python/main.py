import scanner
import parser
import interpreter

if __name__ == "__main__":
    data = "a = 1 + 2; a;"
    scanner = scanner.Scanner(data)
    scanner.scan_tokens()
    tokens = scanner.get_tokens()
    
    parser = parser.Parser(tokens)
    statements = parser.parsing()

    interpreter = interpreter.Interpreter(statements)
    interpreter.interpret()