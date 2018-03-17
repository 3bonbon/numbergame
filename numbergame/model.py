from collections import namedtuple

Score = namedtuple('Score', 'maru sankaku')


class Player:
    def __init__(self, number):
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