import numpy as np
import matplotlib.pyplot as plt


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def propagate(w, b, X, Y):
    A = sigmoid(np.dot(w.T, X) + b)
    m = X.shape[1]
    cost = np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A)) * (-1 / m)

    # Backwad stuff
    dw = np.dot(X, (A - Y).T) * (1 / m)  # same diversion as 'w'
    db = (1 / m) * np.sum(A - Y)

    grad = {'dw': dw,
            'db': db}

    cost = np.squeeze(np.array(cost))
    return grad, cost


def optimize(w, b, X, Y, num_tererations=100, learning_rate=0.005, print_cost=False):
    costs = []
    for epoch in range(num_tererations):
        grad, cost = propagate(w, b, X, Y)
        dw = grad['dw']
        db = grad['db']

        w = w - dw * learning_rate
        b = b - db * learning_rate
        if epoch % 10 == 0:
            costs.append(cost)
            if print_cost == True:
                print(f'Cost after iteration {epoch}: {cost:.4f}')

    params = {'w': w,
              'b': b}
    grad = {'dw': dw,
            'db': db}

    return params, grad, costs

def prediction(w, b, X):
    A = sigmoid(np.dot(w.T, X) + b)
    Y_hat = np.where(A > 0.05, 1, 0)
    return  Y_hat


train_set_x_original = np.load(r'C:\Users\Bori\Desktop\train_set_x.npy')
train_set_y = np.load(r'C:\Users\Bori\Desktop\train_set_y.npy')
test_set_x_original = np.load(r'C:\Users\Bori\Desktop\test_set_x.npy')
test_set_y = np.load(r'C:\Users\Bori\Desktop\test_set_y.npy')

print(train_set_x_original.shape)
print(train_set_y.shape)
# index = 2
# plt.imshow(train_set_x_original[index])
# plt.show()

# Flatten the data

train_set_x_flatten = train_set_x_original.reshape(train_set_x_original.shape[0], -1).T
test_set_x_flatten = test_set_x_original.reshape(test_set_x_original.shape[0], -1).T

print(train_set_x_flatten.shape)

# Normalize

train_x = train_set_x_flatten / 255.
test_x = test_set_x_flatten / 255.

# Create model for variables

w = np.zeros((train_x.shape[0], 1))
b = 0.0

learning_rate = 0.005

params, grad, costs = optimize(w, b, train_x, train_set_y, num_tererations=2000, learning_rate = learning_rate, print_cost= True)
Y_hat_test = prediction(params['w'], params['b'], test_x)
Y_hat_train = prediction(params['w'], params['b'], train_x)

print('Train accuracy: {}'.format(100 - np.mean(np.abs(Y_hat_train - train_set_y)) * 100))
print('Train accuracy: {}'.format(100 - np.mean(np.abs(Y_hat_test - test_set_y)) * 100))
# plt.plot(costs)
# plt.show()