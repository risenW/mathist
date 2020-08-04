import pytest
from mathist import math



def test_add():
    expected = 20
    output = math.add(10, 10)
    assert expected == output


def test_sub():
    expected = 5
    output = math.sub(15, 10)
    assert expected == output


def test_mul():
    expected = 20
    output = math.mul(10, 2)
    assert expected == output


def test_div():
    expected = 3
    output = math.div(30, 10)
    assert expected == output