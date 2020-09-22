from __future__ import annotations
from numbers import Number
from typing import Callable


class ChurchNumber(Number):
    def __init__(self, church: Callable):
        self.ch = church

    def to_int(self) -> int:
        """チャーチ数を組み込みのint型に変換する"""
        return self.ch(lambda n: n + 1)(0)

    def succ(self) -> ChurchNumber:
        """チャーチ数に+1する"""
        return ChurchNumber(lambda f: lambda x: f(self.ch(f)(x)))

    def __add__(self, other: ChurchNumber) -> ChurchNumber:
        """チャーチ数同士を足し算する

        assert (one + two).to_int() == 3
        """
        return ChurchNumber(lambda f: lambda x: self.ch(f)(other.ch(f)(x)))

    def __mul__(self, other: ChurchNumber) -> ChurchNumber:
        """チャーチ数の掛け算(*)を定義する

        assert (two * two).to_int() == 4
        """
        return ChurchNumber(lambda f: lambda x: other.ch(self.ch(f))(x))

    def __pow__(self, exponent: ChurchNumber) -> ChurchNumber:
        """チャーチ数の累乗(**)を定義する

        assert (two ** three).to_int() == 8
        """
        return ChurchNumber(lambda f: lambda x: exponent.ch(self.ch)(f)(x))
