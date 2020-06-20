import re
import sys
from typing import Union


def validate_binary(input: str) -> bool:
    if not re.findall(r'[0, 1]+', input):
        if not input.isnumeric():
            specifics = 'Input is not numeric'
        else:
            specifics = 'Input is not binary'
        print(f'Invalid input {input}: {specifics}')
        return False
    return True


def convert_bin_to_dec(input: str) -> Union[None, int]:
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
    for item in sys.argv[1:]:
        result = convert_bin_to_dec(item)
        if result:
            print(result)
