import bin_to_dec

def test_false_on_non_binary_input():
    assert bin_to_dec.validate_binary('9957') == False

def test_false_on_too_long_input():
    assert bin_to_dec.validate_binary('8437520845606') == False

def test_false_on_non_numeric_input():
    assert bin_to_dec.validate_binary('djafhisd') == False

def test_true_on_short_binary():
    assert bin_to_dec.validate_binary('0010')

def test_true_success_on_complete_binary():
    assert bin_to_dec.validate_binary('11000000')

def test_8_on_short_input():
    assert bin_to_dec.convert_bin_to_dec('1000') == 8

def test_5_on_full_input():
    assert bin_to_dec.convert_bin_to_dec('00000101') == 5