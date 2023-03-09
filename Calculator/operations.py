def sum(num1, num2):
    result = num1 + num2
    if len(str(result)) > 12:
        return "NUM TOO BIG"
    else:
        return f"{str(result):.8}"


def subtraction(num1, num2):
    result = num1 - num2
    if len(str(result)) > 12:
        return "NUM TOO BIG"
    else:
        return f"{str(result):.8}"


def multiplication(num1, num2):
    result = num1 * num2
    if len(str(result)) > 12:
        return "NUM TOO BIG"
    else:
        return f"{str(result):.8}"


def division(num1, num2):
    if num2 == 0:
        return "ERROR"
    result = num1 / num2
    if len(str(result)) > 12:
        return "NUM TOO BIG"
    else:
        return f"{str(result):.8}"
