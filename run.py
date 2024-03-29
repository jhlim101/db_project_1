# for testing purposes:
# select ID from students;
# create table test(id int, primary key(id));

from lark import Lark, Visitor, Transformer, UnexpectedToken

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

    def describe_query(self, tree):
        assert tree.data == 'describe_query'
        print(PROMPT + '\'DESCRIBE\' requested')
    
    def desc_query(self, tree):
        assert tree.data == 'desc_query'
        print(PROMPT + '\'DESC\' requested')

    def drop_table_query(self, tree):
        assert tree.data == 'drop_table_query'
        print(PROMPT + '\'DROP TABLE\' requested')
    
    def show_tables_query(self, tree):
        assert tree.data == 'show_tables_query'
        print(PROMPT + '\'SHOW TABLES\' requested')

    def explain_query(self, tree):
        assert tree.data == 'explain_query'
        print(PROMPT + '\'EXPLAIN\' requested')


if __name__ == "__main__":
    while True:
        query = input(PROMPT)
        try:
            output_tree = sql_parser.parse(query)
            ReturnQueryTypeVisitor().visit(output_tree)
        except UnexpectedToken:
            print(PROMPT + 'Syntax Error')

        