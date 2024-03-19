from lark import Lark

with open('grammar.lark') as file:
    sql_parser = Lark(file.read(), start='command', lexer='basic')