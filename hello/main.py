import turtle


def add(x: int, y: int) -> int:
    return x + y


def findPair(arr: list[int]) -> list[tuple[int, int]]:
    res: list[tuple[int, int]] = []

    first = arr[0]
    rest = arr[1:]

    while len(rest) >= 1:
        for val in rest:
            if val + first == 100:
                res.append((val, first))
                break

        first = rest[0]
        rest = rest[1:]

    return res


bob = turtle.Turtle()
