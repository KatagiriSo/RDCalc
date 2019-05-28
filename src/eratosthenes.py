

def modfilter(l: list, modnum: int) -> list:
    return list(filter(lambda x: x == modnum or x % modnum != 0, l))


def eratosthenes(l: list) -> list:
    ret = l.copy()
    max = l[-1]
    for i in l:
        if i*i > max:
            return ret
        ret = modfilter(ret, i)
    return ret


def test():
    tryval = [i for i in range(2, 1000)]
    res = eratosthenes(tryval)
    print(res)
