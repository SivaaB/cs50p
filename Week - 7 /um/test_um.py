import pytest
from um import count

def test_input():
    assert count ("Um, thanks lol") == 1
    assert count ("um okay") == 1
    assert count ("um um um um um wtf") == 5
    assert count("um") == 1