import bin_to_dec

def test_failure_on_non_binary_input():
    assert bin_to_dec.convert('9957') == None

def test_none_on_too_long_input():
    assert bin_to_dec.convert('8437520845606') == None

def test_failure_on_non_numeric_input():
    assert bin_to_dec.convert('djafhisd') == None

def test_success_on_short_binary():
    assert bin_to_dec.convert('1000') == 8

def test_success_on_complete_binary():
    assert bin_to_dec.convert('00000101') == 5