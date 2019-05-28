import numpy as np
import generateTestData as generateTestData


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


def testPrime():

    data = generateTestData.generateTestData(10)

    xlist = np.matrix(data[1])
    tlist = np.matrix(data[2]).T
    w = np.matrix(np.zeros(xlist.shape[1]))
    e = 0.5

    print("data:"+str(data))
    print("xlist:"+str(xlist))
    print("tlist:"+str(tlist))
    print("w:"+str(w))
    print("e:"+str(e))


    epoch = 10
    for i in range(0, epoch):
        w = learning(w, xlist, tlist, e)
    
    all = tlist.shape[0]
    p = 0
    for i in range(0, tlist.shape[0]):
        ans = forward(w, xlist[i])        
        print(str(data[0][i]) + " ans " + str(ans) + "---" + str(tlist[i]))
        if ans == tlist[i]:
            p = p + 1

    print("all:" + str(all) + " true:" + str(p) + " percent:" + str(float(p/all*100))+"%")




testPrime()