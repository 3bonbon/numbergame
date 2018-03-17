import pytest
from numbergame import Player
from numbergame.model import is_valid_number


def test_valid_numbers():
    assert is_valid_number('0123')
    assert is_valid_number('9876')
    assert is_valid_number('4739')
    assert is_valid_number('1029')


def test_invalid_numbers():
    assert not is_valid_number('0122')
    assert not is_valid_number('0000')
    assert not is_valid_number('123')
    assert not is_valid_number('12345')
    assert not is_valid_number('a')
    assert not is_valid_number('123o')
    assert not is_valid_number('atoz')
    assert not is_valid_number('%^$@')
    assert not is_valid_number('')


def test_valid_player_creation():
    p = Player('0123')


def test_invalid_player_creation():
    with pytest.raises(ValueError) as e:
        p = Player('')
