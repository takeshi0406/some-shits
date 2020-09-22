from church import ChurchNumber


def test():
    zero = ChurchNumber(lambda f: lambda x: x)
    assert zero.to_int() == 0
    one = zero.succ()
    assert one.to_int() == 1
    two = one.succ()
    assert two.to_int() == 2
    three = two.succ()
    assert three.to_int() == 3

    assert (one + two).to_int() == three.to_int()

    assert (two ** three).to_int() == 8
    assert (two * three).to_int() == 6
    assert (two ** zero).to_int() == 1
