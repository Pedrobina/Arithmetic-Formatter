import sys

def verify_exceptions(number1, number2, operator):
    # The operator is + or - ?
    try:
        if operator != '+' and operator != '-':
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."

    # The numbers contain only digits?
    try:
        int(number1)
    except:
        return "Error: Numbers must only contain digits."
    try:
        int(number2)
    except:
        return "Error: Numbers must only contain digits."


    try:
        if len(number1) > 4 or len(number2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."

    return ""


def arithmetic_arranger(expressions, showResult=False):
    count_expressions = len(expressions)
    message = " "
    find_error = False
    line1 = line2 = line3 = line4 = ''

    # verify if there is more than 5 problems in expressions
    try:
        if len(expressions) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."

    for exp in expressions:
        count_expressions = count_expressions - 1
        line = "-"
        space_number1 = space_number2 = space_result = ' '
        space_line = size_number1 = size_number2 = 0

        # Verify exceptions
        spare_problem = exp.split()
        valid_expression = verify_exceptions(spare_problem[0], spare_problem[2], spare_problem[1])
        if valid_expression != "":
            return valid_expression

        # Get the split values of expression
        number1 = int(spare_problem[0])
        operator = spare_problem[1]
        number2 = int(spare_problem[2])

        # Get the size of numbers
        size_number1 = len(spare_problem[0])
        size_number2 = len(spare_problem[2])


        # Get the result of operation
        if operator == '+':
            result = str(number1 + number2)
        else:
            result = str(number1 - number2)

        # Verify the large number to calculate the size of line
        if size_number1 > size_number2:
            space_line = size_number1
        elif size_number1 < size_number2:
            space_line = size_number2
        else:
            space_line = size_number1

        space_line = space_line + 1
        for size in range(space_line):
            line = line + "-"


        # Calculating the space for the lines
        for space in range(space_line - size_number1):
            space_number1 = space_number1 + ' '
        for space in range(space_line - size_number2 - 1):
            space_number2 = space_number2 + ' '
        for space in range(space_line - len(result)):
            space_result = space_result + ' '

        if count_expressions > 0:
            line1 = line1 + space_number1 + spare_problem[0] + '    '
            line2 = line2 + operator + space_number2 + spare_problem[2] + '    '
            line3 = line3 + line + '    '
            line4 = line4 + space_result + result + '    '
        else:
            line1 = line1 + space_number1 + spare_problem[0]
            line2 = line2 + operator + space_number2 + spare_problem[2]
            line3 = line3 + line
            line4 = line4 + space_result + result



    if showResult == True:
        #print( line1 + '\n' + line2 + '\n' + line3 + '\n' + line4)
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3
