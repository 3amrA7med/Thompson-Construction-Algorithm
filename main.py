import click
from utils import validate_and_parse
from utils.constructor import construct_nfa

@click.command()
@click.option('-re', '--regular_expression', type=click.STRING,
              help='input regular expression.', required=True, default='A|B')
def run(regular_expression):
    is_valid, operations = validate_and_parse(regular_expression)
    print(operations)
    if is_valid:
        # Convert to corresponding NFA
        json = construct_nfa(operations)
        print(json)
    else:
        # The regular expression is invalid
        print("The regular expression is invalid.")


if __name__ == '__main__':
    run()
