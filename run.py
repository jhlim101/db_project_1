# for testing purposes:
# select ID from students;
# create table test(id int, primary key(id));

from lark import Lark, Visitor

PROMPT = 'DB_2022-13616>'

with open('grammar.lark') as file:
    sql_parser = Lark(file.read(), start='command', lexer='basic')

class ReturnQueryTypeVisitor(Visitor):
    def select_query(self, tree):
        assert tree.data == 'select_query'
        print(PROMPT + '\'SELECT\' requested')
    
    def create_table_query(self, tree):
        assert tree.data == 'create_table_query'
        print(PROMPT + '\'CREATE TABLE\' requested')

    def delete_query(self, tree):
        assert tree.data == 'delete_query'
        print(PROMPT + '\'DELETE\' requested')

if __name__ == "__main__":
    bool_exit = False
    while not bool_exit:
        query = input(PROMPT)
        output_tree = sql_parser.parse(query)
        ReturnQueryTypeVisitor().visit(output_tree)
        