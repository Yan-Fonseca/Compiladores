#ifndef TOKENS_H
#define TOKENS_H

#include <string>

enum TokenType {
    NUMBER,
    SEMICOLON,
    OPERATOR,
    ASSIGN,
    IDENTIFIER,
    TEOF // token EOF
};

class Token {
private:
    std::string lexer;
    TokenType type;
    Token *next;
public:
    Token(std::string lexer, TokenType type) {
        this->lexer = lexer;
        this->type = type;
        this->next = nullptr;
    }
    ~Token() {}

    TokenType getType() {return this->type;}
    std::string getLexer() {return this->lexer;}

    void setNext(Token *next) {this->next = next;}
    Token *getNext() {return this->next;}
};

#endif