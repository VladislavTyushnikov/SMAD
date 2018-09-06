import numpy as np
import NormalDistributionGenerator as NormRnd


def getFuncIX(xVec, i):
    switcher = {
        0: abs(xVec[0]),
        1: xVec[1] * xVec[1],
        2: abs(xVec[0] * xVec[1]),
        3: np.sin(xVec[0] * 50),
        4: np.sin(xVec[1] * 10)
    }
    return switcher[i]


def getU(xVec, tetaVec):
    summ = 0
    for i in range(tetaVec.__len__()):
        summ += getFuncIX(xVec, i) * tetaVec[i]
    return summ


def getY(xVec, tetaVec, mu, sigma):
    return getU(xVec, tetaVec) + NormRnd.rnd(mu, sigma)


sigma = 1
mu = 0
tetaVec = [1, 3, 1 / 100, 1 / 3]

for i in np.arange(-1, 1 + 0.25, 0.25):
    for j in np.arange(-1, 1 + 0.25, 0.25):
        print(getY([j, i], tetaVec, sigma, mu))
