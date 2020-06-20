import re

def __validate(input: str):
    if (not re.findall(r'\d{1,8}[0, 1]+', input)) or len(input) > 8:
        if 1 > len(input) > 8:
            specifics = 'Invalid input length'
        elif not input.isnumeric():
            specifics = 'Input is not numeric'
        else:
            specifics = 'Input is not binary'
        print(f'Invalid input {input}: {specifics}')
        return False
    return True

def convert(input: str):
    if not __validate():
        return None
    total = 0
    current = 1
    for digit in input[::-1]:
        if digit == '1':
            total += current
        current *= 2
    return total
