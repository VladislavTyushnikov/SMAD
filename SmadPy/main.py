import numpy as np
import random as rnd


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
    return getU(xVec, tetaVec) + rnd.normalvariate(mu, sigma)


def makeObservations(bordersX, steps, tetaVec, sigma, mu):
    obsTable = []
    for x1 in np.arange(bordersX[0][0], bordersX[0][1] + steps[0], steps[0]):
        for x2 in np.arange(bordersX[1][0], bordersX[1][1] + steps[1], steps[1]):
            yDash = getY([x1, x2], tetaVec, mu, sigma)
            obsTable.append([x1, x2, yDash])
    return obsTable


def avg(listOfFloat):
    avg = 0
    n = listOfFloat.__len__()
    for i in range(n):
        avg += listOfFloat[i]
    avg /= n
    return avg


def calcSignalPower(tetaVec):
    uVec = []
    for x1 in np.arange(-1, 1 + 0.125, 0.125):
        for x2 in np.arange(-1, 1 + 0.125, 0.125):
            y = getU([x1, x2], tetaVec)
            uVec.append(y)

    uAvg = avg(uVec)
    omega2 = 0
    n = uVec.__len__()
    for i in range(n):
        omega2 += (uVec[i] - uAvg) * (uVec[i] - uAvg)
    omega2 /= (n - 1)
    return omega2


def calcTetaDashVec(obsTable, tetaVeclen):

        # Solving system (XT * X) * TetaDash = XT * Y
        # for TetaDash

    m = tetaVeclen
    n = obsTable.__len__()

    X = np.zeros((n, m), dtype=float)
    Y = np.zeros((n, 1), dtype=float)

    for i in range(n):
        x1 = obsTable[i][0]
        x2 = obsTable[i][1]
        y = obsTable[i][2]
        Y[i] = y
        for j in range(m):
            X[i][j] = getFuncIX([x1, x2], j)

    XT = X.transpose()
    XTX = np.dot(XT, X)
    XTY = np.dot(XT, Y)
    TetaDash = np.linalg.solve(XTX, XTY)
    return np.transpose(TetaDash)[0]


def calcSigma2Dash(tetaDashVec, obsTable):
    m = tetaDashVec.__len__()
    n = obsTable.__len__()

    Y = np.zeros((n, 1), dtype=float)
    YDash = np.zeros((n, 1), dtype=float)

    for i in range(n):
        x1 = obsTable[i][0]
        x2 = obsTable[i][1]
        y = obsTable[i][2]

        Y[i] = y
        YDash[i] = getU([x1, x2], tetaDashVec)

    eDash = np.subtract(Y, YDash)

    sigma2 = np.dot(np.transpose(eDash), eDash)
    sigma2 /= (n - m)
    return sigma2[0][0]

def calcQuantile(sigma, sigmaDash):
    print("F: " + str(sigmaDash/sigma))
    if sigmaDash/sigma <= 1.28:
        return "Модель адекватная"
    else:
        return "Модель неадекватная"





sigma = np.sqrt(1.1 * 0.1)
mu = 0
bordersX = [[-1, 1], [-1, 1]]
tetaVec = [1, 3,1, 1 / 100, 1 / 3]
observations = []

observations = makeObservations(bordersX, [0.5, 0.5], tetaVec, sigma, mu)
for i in range(observations.__len__()):
    print(observations[i])
print("Power: ", calcSignalPower(tetaVec))
print("Teta: ", tetaVec)
tetaDashVec = calcTetaDashVec(observations, tetaVec.__len__())
print("TetaDash: ", tetaDashVec)
sigma2Dash = calcSigma2Dash(tetaDashVec, observations)
print("sigma2: ", sigma * sigma)
print("sigma2Dash: ", sigma2Dash)
print(calcQuantile(sigma*sigma, sigma2Dash))