import string
OR1 = "|"
OR2 = "+"
ASTERISK = "*"
OPEN_BRACKET = "("
CLOSED_BRACKET = ")"
ALPHABET = list(string.ascii_uppercase)


def validate_and_parse(regular_expression):
    """
    This function validates the input to be a regular expression and returns list of operations to be done on the graph
    :return:    -True if the input is valid
                -False otherwise
    """
    # Case: if closed bracket found before open bracket, or one bracket from 2 found
    if not brackets_check(regular_expression):
        return False, []
    brackets_found = True
    # No brackets
    o = regular_expression.find(OPEN_BRACKET)
    c = regular_expression.find(CLOSED_BRACKET)
    if o == -1 and c == -1:
        brackets_found = False

    number_of_iterations = len(regular_expression)
    finished = False
    reduced_expression = regular_expression
    operations = []
    while not finished:
        print(reduced_expression)
        # Expression needed to be validated
        expression = reduced_expression
        open_bracket = -1
        if brackets_found:
            # All occurrences of brackets in regular expression
            open_bracket_occurrences = [i for i in range(len(reduced_expression))
                                        if reduced_expression.startswith(OPEN_BRACKET, i)]
            closed_bracket_occurrences = [i for i in range(len(reduced_expression))
                                          if reduced_expression.startswith(CLOSED_BRACKET, i)]
            # If there exists brackets
            if len(open_bracket_occurrences) != 0:
                # Find the first nested brackets
                for position in open_bracket_occurrences:
                    if position < closed_bracket_occurrences[0]:
                        open_bracket = position
                    else:
                        break
                expression = reduced_expression[open_bracket + 1: closed_bracket_occurrences[0]]
                # print(open_bracket, closed_bracket_occurrences[0], expression)
                # If one element found in the brackets remove brackets and continue with next iteration.
                if len(expression) == 1:
                    reduced_expression = remove_at(open_bracket, reduced_expression)
                    reduced_expression = remove_at(closed_bracket_occurrences[0] - 1, reduced_expression)
                    # print("One element inside brackets", reduced_expression)
                    continue
            else:
                brackets_found = False
        # Validate expression
        if len(reduced_expression) == 1 or number_of_iterations == 0:
            finished = True
            continue
        try:
            # print("Expression that will be validated: ", expression)
            is_valid, (operations, reduced_expression) = validate_expression(operations, open_bracket+1,
                                                                             expression, reduced_expression)
        except:
            return False, []
        if not is_valid:
            return False, []
        number_of_iterations -= 1
    return True, operations


def validate_expression(operations, start_index, expression, reduced_expression):
    """
    This function takes an expression and validate it
    :param operations: list of operations that is required to be filled
    :param start_index: start index of sub-expression that is required to be validated in the whole string
    :param expression: sub-expression
    :param reduced_expression: string that holds the expression after reduction
    :return: true of its valid and list of operations
    """
    # Case 1: Zero or more.
    asterisk_position = expression.find(ASTERISK)
    if asterisk_position != -1:
        # repeated asterisk
        if len(expression) > 2 and expression[asterisk_position+1] == "*":
            return False, [], []
        else:
            asterisk_position = reduced_expression.find(ASTERISK)
            return True, reduce(operations, asterisk_position-1, asterisk_position+1, reduced_expression)

    # Case 2: move from left to right.
    # if the second char is not or then its a concat
    if reduced_expression[start_index+1] != OR1 and reduced_expression[start_index+1] != OR2:
        return True, reduce(operations, start_index + 0, start_index + 2, reduced_expression)
    # Case 3: Or found
    else:
        # OR not repeated
        if reduced_expression[start_index + 2] == OR1 or reduced_expression[start_index + 2] == OR2:
            return False, [], []
        else:
            return True, reduce(operations, start_index + 0, start_index + 3, reduced_expression)


def reduce(operations, start, end, reduced_expression):
    """
    This function reduces the input to one state and if its an operation it add it to the list of operations
    :param operations: list of operations.
    :param start: start index of sub-expression in which we want to reduce.
    :param end: end index of sub-expression in which we want to reduce.
    :param reduced_expression: new expression after reduction.
    :return: reduced_expression, operations
    """
    expression = reduced_expression[start: end]
    # print(expression, reduced_expression, start, end)
    alphabet_index = len(operations)
    # Case Asterisk:
    if expression.find(ASTERISK) != -1:
        # Add operation
        operations.append([ALPHABET[alphabet_index], "*", expression[0]])
    # Case OR:
    elif expression.find(OR1) != -1 or expression.find(OR2) != -1:
        # Add operation
        operations.append([ALPHABET[alphabet_index], "+", expression[0], expression[2]])
    else:
        # Add operation
        operations.append([ALPHABET[alphabet_index], "CONCAT", expression[0], expression[1]])
    # Reduce
    reduced_expression = reduced_expression[:start] + ALPHABET[alphabet_index] + reduced_expression[end:]
    # print(operations, expression, reduced_expression)
    return operations, reduced_expression


def remove_at(i, s):
    """
    This function removes a char from string
    :param i: index of the char
    :param s: string
    :return: new string after char removal
    """
    return s[:i] + s[i + 1:]


def brackets_check(regular_expression):
    """
    This function checks closed bracket found before open bracket, or one bracket from 2 found
    :param regular_expression: expression needed to be checked
    :return: False if the check failed, True otherwise
    """
    open_bracket_occurrences = [i for i in range(len(regular_expression))
                                if regular_expression.startswith(OPEN_BRACKET, i)]
    closed_bracket_occurrences = [i for i in range(len(regular_expression))
                                  if regular_expression.startswith(CLOSED_BRACKET, i)]
    if len(open_bracket_occurrences) == len(closed_bracket_occurrences):
        if len(open_bracket_occurrences) != 0:
            o = open_bracket_occurrences[0]
            c = closed_bracket_occurrences[0]
            if c < o:
                return False
    else:
        return False
    return True
