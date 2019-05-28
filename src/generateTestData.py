import eratosthenes
import math


def transBool(b: bool) -> int:
    if b:
        return 1
    return 0


def transBitList(num, max):

    log2_num = int(math.log2(max))+1

    # 2: is remove 0b from list
    # log2_num and zfill is for 0 padding
    return [int(x) for x in bin(num)[2:].zfill(log2_num)]


def generateTestData(max):
    inp = [i for i in range(2, max)]
    inpbitlist = [transBitList(x, max) for x in inp]
    primelist = eratosthenes.eratosthenes(inp)
    ans = [transBool(i in primelist) for i in inp]
    return [inp, inpbitlist, ans]





