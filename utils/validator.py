OR1 = "|"
OR2 = "+"
REPETITION = "*"
OPEN_BRACKET = "("
CLOSED_BRACKET = ")"


def validate(regular_expression):
    """
    This function validates the input to be a regular expression.
    :return:    -True if the input is valid
                -False otherwise
    """
    # Case: if closed bracket found before open bracket, or one bracket from 2 found
    o = regular_expression.find(OPEN_BRACKET)
    c = regular_expression.find(CLOSED_BRACKET)
    if o != -1 and c == -1:
        return False
    if o == -1 and c != -1:
        return False
    if (o != -1 and c != -1) and c < o:
        return False

    finished = False
    reduced_expression = regular_expression
    while not finished:
        # All occurrences of substring in string
        open_bracket_occurrences = [i for i in range(len(reduced_expression))
                                    if reduced_expression.startswith(OPEN_BRACKET, i)]
        closed_bracket_occurrences = [i for i in range(len(reduced_expression))
                                      if reduced_expression.startswith(CLOSED_BRACKET, i)]
        # Find the first nested brackets
        open_bracket = -1
        for position in open_bracket_occurrences:
            if position < closed_bracket_occurrences[0]:
                open_bracket = position
            else:
                break
        print(open_bracket, closed_bracket_occurrences[0])
        # Validate expression
        is_valid = validate_expression(reduced_expression)
        if not is_valid:
            return False
        finished = True


def validate_expression(expression):
    # Case1: OR.
    if expression.find(OR1) != -1 or expression.find(OR2) != -1:
        # OR not repeated
        pass

    # Case2: Zero or more.
    if expression.find(REPETITION) != -1:
        pass
    return False
    # Case3: Concat.
