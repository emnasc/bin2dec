import re
import sys

def validate_binary(input: str):
    if (not re.findall(r'\d{1,8}[0, 1]+', input)) or len(input) > 8:
        if not input.isnumeric():
            specifics = 'Input is not numeric'
        elif (1 > len(input) or len(input) > 8):
            specifics = 'Invalid input length'
        else:
            specifics = 'Input is not binary'
        print(f'Invalid input {input}: {specifics}')
        return False
    return True

def convert_bin_to_dec(input: str):
    if not validate_binary(input):
        return None
    total = 0
    current = 1
    for digit in input[::-1]:
        if digit == '1':
            total += current
        current *= 2
    return total

if __name__ == '__main__':
    for input in sys.argv[1:]:
        result = convert_bin_to_dec(input)
        if result:
            print(result)
