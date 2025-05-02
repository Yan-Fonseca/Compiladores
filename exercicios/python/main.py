import scanner
import parser
import interpreter

if __name__ == "__main__":
    nome_arquivo = 'exercicios/samples/sample3.txt'
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        data = arquivo.read()
    scanner = scanner.Scanner(data)
    scanner.scan_tokens()
    tokens = scanner.get_tokens()
    
    parser = parser.Parser(tokens)
    statements = parser.parsing()

    interpreter = interpreter.Interpreter(statements)
    interpreter.interpret()