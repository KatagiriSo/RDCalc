import numpy as np


# vec1, vec2 np -> num
def prod(vec1, vec2):
    return vec1*vec2.T


# step function
def step(x):
    if x > 0:
        return 1
    return 0


def forward(w, x):
    u = prod(w, x)
    return step(u)


# e 学習率 t 正解
def train(w, x, t, e):
    z = forward(w, x)
    w = w + (t - z) * x * e
    return w


# e 学習率 anslist 正解列
def learning(w, xlist, anslist, e):
    zipedPair = zip(xlist, anslist)
    for x, t in zipedPair:
        w = train(w, x, t, e)
    return w


def test():
    xlist = np.matrix([[1, 0, 0], [1, 0, 0], [1, 1, 1], [1, 0, 1]])
    tlist = np.matrix([1, 1, 0, 1]).T
    w = np.matrix([0, 0, 0])
    e = 0.01

    epoch = 10
    for i in range(0, epoch):
        w = learning(w, xlist, tlist, e)
    
    for i in range(0, 4):
        ans = forward(w, xlist[i])
        print("ans " + str(ans) + "---" + str(tlist[i])+"\n")


test()