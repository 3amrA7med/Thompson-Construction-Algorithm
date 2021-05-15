def preprocess_regular_expression(regular_expression):
    # Convert to small letters
    regular_expression = regular_expression.lower()
    # Remove white spaces
    regular_expression = regular_expression.replace(" ", "")
    return regular_expression
