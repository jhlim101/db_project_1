from lark import Lark, Visitor, UnexpectedToken

PROMPT = 'DB_2022-13616>'

with open('grammar.lark') as file:
    sql_parser = Lark(file.read(), start='command', lexer='basic')

# return query type visitor
class ReturnQueryTypeVisitor(Visitor):

    exit_flag = False

    def command(self, tree):
        if tree.children[0] == 'exit':
            self.exit_flag = True

    def select_query(self, tree):
        print(PROMPT + '\'SELECT\' requested')
    
    def create_table_query(self, tree):
        print(PROMPT + '\'CREATE TABLE\' requested')

    def delete_query(self, tree):
        print(PROMPT + '\'DELETE\' requested')

    def describe_query(self, tree):
        print(PROMPT + '\'DESCRIBE\' requested')
    
    def desc_query(self, tree):
        print(PROMPT + '\'DESC\' requested')

    def drop_table_query(self, tree):
        print(PROMPT + '\'DROP TABLE\' requested')
    
    def show_tables_query(self, tree):
        print(PROMPT + '\'SHOW TABLES\' requested')

    def explain_query(self, tree):
        print(PROMPT + '\'EXPLAIN\' requested')

    def insert_query(self, tree):
        print(PROMPT + '\'INSERT\' requested')

    def update_query(self, tree):
        print(PROMPT + '\'UPDATE\' requested')

# parse query function
def parse_query(query, visitor):
    error_flag = False
    try:
        output_tree = sql_parser.parse(query)
        visitor.visit(output_tree)
    except UnexpectedToken:
        print(PROMPT + 'Syntax Error')
        error_flag = True
    return error_flag

if __name__ == "__main__":
    # instantiate visitor class
    visitor = ReturnQueryTypeVisitor()

    # main loop to continue until exit_flag == True
    while not visitor.exit_flag:
        raw_input = input(PROMPT)
        input_list = [raw_input]

        # while loop to continue receiving new lines as input until semicolon is encountered
        while not raw_input.__contains__(";"):
            new_line = input()
            input_list.append(new_line)
            if new_line.__contains__(";"):
                break
        
        # join query sequence together into one line, then split based on semicolon separator to parse queries separately
        query_sequence = " ".join(input_list)
        queries = query_sequence.split(';')

        # iterate through queries and parse each query
        for query in queries:
            query = query.strip()
            if query:
                parsed_query_with_error = parse_query(query + ";", visitor)
                # break from loop if parse_query error_flag returns True
                if parsed_query_with_error:
                    break

