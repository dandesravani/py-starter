from hello.main import add, findPair


def test_add():
    assert add(1, 1) == 2


def test_findpair():
    assert findPair([97, 7, 3, 2, 19, 98, 4, 96]) == [(3, 97), (98, 2), (96, 4)]
