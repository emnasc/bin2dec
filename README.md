# bin2dec

A simple implementation of a binary to decimal converter.

This is and implementation of the Bin2Dec app idea on [Florin Pop's](https://github.com/florinpop17) [App ideas](https://github.com/florinpop17/app-ideas) repository.

Following the description in the user histories, which can be found [here](https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/Bin2Dec-App.md), this implementation comply to the following constraints:
+ User can enter up to 8 binary digits in one input field
+ User must be notified if anything other than a 0 or 1 was entered
+ User views the results in a single output field containing the decimal (base 10) equivalent of the binary number that was entered

And as an extra increment:
+ User can enter a variable number of binary digits

## Environment and depenencies
This implementation uses Pipenv as an virtual environment manager. The environment was created from a Python 3.6.0 base interpreter. Pipenv can be installed via pip using:

``` shell script
pip install pipenv
```

The only other dependency of the project is pytest, used to run the unit tests of the project. Once pipenv is installed, it can initialized and have pytest installed using:

``` shell script
pipenv shell
pip install pytest
```

## Executing the project
The project can be execute as a standard Python script, taking one or more binary strings as command line arguments.
```` shell script
python bin_to_dec.py 000101 11101 111001
````

The line above should output the following

````
5
29
57
````