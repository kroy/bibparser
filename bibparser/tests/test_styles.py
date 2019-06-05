# pytest tests for the style classes
# run with pytest from the bibparser parent dir

from ..styles import chicago

def test_chicago():
    assert chicago.parse("abcd") == "abcd"