import numpy as np
import copy
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))
def init_paran():
    w1 = np.random.randn(n_h, n_X) * 0.01
    b1 = np.zeros((n_h, 1))
    w2 = np.random.randn(n_Y, n_h) * 0.01
    b2 = np.zeros((n_Y, 1))

    prams = {
        'w1': w1,
        'b1': b1,
        'w2': w2,
        'b2': b2
    }

    return prams


def forward_prop(x, parameters):
    w1 = parameters['w1']
    w2 = parameters['w2']
    b1 = parameters['b1']
    b2 = parameters['b2']

    z1 = np.dot(w1, x) + b1
    A1 = np.tanh(z1)
    z2 = np.dot(w2, A1) + b2
    A2 = sigmoid(z2)

    cache = {
        'z1': z1,
        'z2': z2,
        'A1': A1,
        'A2': A2
    }

    return A2, cache


def compute_cost(A2, Y):
    loss = (Y * np.log(A2) + (1-Y) * np.log(1 - A2)) * -1
    cost = np.sum(loss)/ Y.shape[1]

    return cost


def back_prop(parameters, cash, X, Y):
    m = X.shape[1]
    w1 = parameters['w1']
    w2 = parameters['w2']

    A1 = cash['A1']
    A2 = cash['A2']

    dz2 = A2 - Y
    dw2 = np.dot(dz2, A1.T) * (1/m)
    db2 = np.sum(dz2, axis= 1, keepdims=True) * (1 / m)
    dz1 = np.dot(w2.T, dz2) * (1 - np.power(A1, 2))
    dw1 = (1/m) * np.dot(dz1, X.T)
    db1 = (1/m) * np.sum(dz1, axis=1, keepdims=True)

    grad = {
        'dw1': dw1,
        'dw2': dw2,
        'db1': db1,
        'db2': db2
    }

    return grad

def update_parametes(parameters, grads, learnin_rate):
    w1 = copy.deepcopy(parameters['w1'])
    w2 = copy.deepcopy(parameters['w2'])
    b1 = copy.deepcopy(parameters['b1'])
    b2 = copy.deepcopy(parameters['b2'])

    dw1 = grads['dw1']
    dw2 = grads['dw2']
    db1 = grads['db1']
    db2 = grads['db2']

    w1 = w1 - dw1 * learnin_rate
    w2 = w2 - dw2 * learnin_rate
    b1 = b1 - db1 * learnin_rate
    b2 = b2 - db2 * learnin_rate

    prams = {
        'w1': w1,
        'w2': w2,
        'b1': b1,
        'b2': b2
    }

    return prams


def nn_mode(X, Y, num_iteration = 1000, print_soct=False):
    np.random.seed(42)
    parametes = init_paran()

    for epoch in range(num_iteration):
        A2, cache = forward_prop(X, parametes)

        cost = compute_cost(A2, Y)
        grads = back_prop(parametes, cache, X, Y)

        parametes = update_parametes(parametes, grads, 0.005)

        if print_soct and epoch % 100 == 0:
            print(f"Cost after {epoch} iteration: {cost: 4f}")

    return parametes

def prediction(paramteres, X):
    A2, _ = forward_prop(X, paramteres)
    prediction = np.where(A2>0.5, 1, 0)
    return prediction



X = np.loadtxt(r'C:\Users\Bori\Desktop\planar_X.dat', dtype=float)
Y = np.loadtxt(r'C:\Users\Bori\Desktop\planar_Y.dat', dtype=float)

Y = Y.reshape(1, -1)
X = X.T

n_X = X.shape[0]
n_h = 4
n_Y = Y.shape[0]


trained_paramaters = nn_mode(X, Y, num_iteration=10000, print_soct=True)
