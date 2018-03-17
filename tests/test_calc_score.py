from numbergame import Player
from numbergame import Score

p = Player('0123')


def test_0_maru():
    assert p.calc_score('4567') == Score(0, 0)


def test_1_maru():
    assert p.calc_score('4527') == Score(1, 0)


def test_4_maru():
    assert p.calc_score('0123') == Score(4, 0)


def test_1_sankaku():
    assert p.calc_score('4560') == Score(0, 1)


def test_2_sankaku():
    assert p.calc_score('4501') == Score(0, 2)


def test_4_sankaku():
    assert p.calc_score('1230') == Score(0, 4)


def test_1_maru_1_sankaku():
    assert p.calc_score('0451') == Score(1, 1)


def test_2_maru_2_sankaku():
    assert p.calc_score('0321') == Score(2, 2)


def test_1_maru_3_sankaku():
    assert p.calc_score('0312') == Score(1, 3)

