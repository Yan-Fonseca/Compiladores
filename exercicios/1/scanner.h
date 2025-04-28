#ifndef SCANNER_H
#define SCANNER_H

#include <tokens.h>
#include <string>

class Scanner {
private:
    Token *tokens;
    Token *last;
public:
    Scanner() {
        this->tokens = nullptr;
        this->last = nullptr;
    }
    ~Scanner() {}

    Token *scan(std::string data) {
        char character;
        char next_character;
        std::string aux = "";

        for(int i=0; i<data.length()-1; i++) {
            character = data[i];
            next_character = next(data, i);

            if(next_character == ' ') {
                this->create_token(aux);
            }
        }
    }

    char next(std::string data, int index) {
        return data[index+1];
    }

    void create_token(std::string lexer) {
        TokenType type = this->verify_type(lexer);
        
    }

    TokenType verify_type(std::string lexer) {
        try
        {
            int _ = stoi(lexer);
            return TokenType::NUMBER;
        }
        catch(const std::exception& e)
        {
            if (lexer == "=")
                return TokenType::ASSIGN;
            else if (lexer == "+" || lexer == "-" || lexer == "*" || lexer == "/" || lexer == "%")
                return TokenType::OPERATOR;
            else if (lexer == ";")
                return TokenType::SEMICOLON;
            else
                return TokenType::IDENTIFIER;
        }
    }
};

#endif