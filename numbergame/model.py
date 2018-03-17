import string
from collections import namedtuple

Score = namedtuple('Score', 'maru sankaku')


def is_valid_number(number):
    if len(number) != 4:
        return False
    if len(set(number)) < 4:
        return False
    for digit in number:
        if digit not in string.digits:
            return False
    return True


class Player:
    def __init__(self, number):
        if not is_valid_number(number):
            raise ValueError(f'{number} is not a valid number')
        self._number = number

    def calc_score(self, guess):
        maru = 0
        sankaku = 0
        for ans, gss in zip(self._number, guess):
            if ans == gss:
                maru += 1
            elif gss in self._number:
                sankaku += 1
        return Score(maru=maru, sankaku=sankaku)

