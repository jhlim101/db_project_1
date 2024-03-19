from lark import Lark, Token

PROMPT = 'DB_2022-13616>'

with open('grammar.lark') as file:
    sql_parser = Lark(file.read(), start='command', lexer='basic')

if __name__ == "__main__":
    bool_exit = False
    while not bool_exit:
        query = input(PROMPT)
        print('-----Parsed Result-----')
        output_tree = sql_parser.parse(query)
        print(output_tree.pretty())
        