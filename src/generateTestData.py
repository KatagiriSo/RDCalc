import eratosthenes


def transBool(b: bool) -> int:
    if b:
        return 1
    return 0


def generateTestData():
    inp = [i for i in range(2, 1000)]
    primelist = eratosthenes.eratosthenes(inp)
    ans = [transBool(i in primelist) for i in inp]
    return [inp, ans]