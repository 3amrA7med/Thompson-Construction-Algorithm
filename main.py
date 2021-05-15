import click
from utils import validate_and_parse, construct_nfa, preprocess_regular_expression, draw_graph

# Assumptions made:
# 1- No capital letters used in the regular expression and if used it is converted to lower case.
# 2- White spaces are removed.
# 3- regular expression will be with limited length. (26 operation maximum).
@click.command()
@click.option('-re', '--regular_expression', type=click.STRING,
              help='input regular expression.', required=True, default='A|B')
def run(regular_expression):
    regular_expression = preprocess_regular_expression(regular_expression)
    is_valid, operations = validate_and_parse(regular_expression)
    print(operations)
    if is_valid:
        # Convert to corresponding NFA
        json = construct_nfa(operations)
        print(json)
        draw_graph(json)
    else:
        # The regular expression is invalid
        print("The regular expression is invalid.")


if __name__ == '__main__':
    run()
