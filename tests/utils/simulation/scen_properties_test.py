#import src.pyssem.pyssem as pyssem
import pytest

# Create a pytest fixture to load the species.json file
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4


if __name__ == '__main__':
    test_answer()

