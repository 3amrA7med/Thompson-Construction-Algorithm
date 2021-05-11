import click
from utils import validate


@click.command()
@click.option('-re', '--regular_expression', type=click.STRING,
              help='input regular expression.', required=True, default='A|B')
def run(regular_expression):
    is_valid = validate(regular_expression)
    print(is_valid, regular_expression)
    if is_valid:
        # Convert to corresponding NFA
        pass
    else:
        # The regular expression is invalid
        print("The regular expression is invalid.")


if __name__ == '__main__':
    run()
