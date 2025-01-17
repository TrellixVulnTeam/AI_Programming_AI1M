import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_points(X, y):
    admitted = X[np.argwhere(y == 1)]
    rejected = X[np.argwhere(y == 0)]
    plt.scatter([s[0][0] for s in rejected],
                [s[0][1] for s in rejected],
                s=25, color='blue', edgecolor='k')
    plt.scatter([s[0][0] for s in admitted],
                [s[0][1] for s in admitted],
                s=25, color='red', edgecolor='k')


def display(m, b, color='g--'):
    plt.xlim(-0.05, 1.05)
    plt.ylim(-0.05, 1.05)
    x = np.arange(-10, 10, 0.1)
    plt.plot(x, m*x+b, color)


# Reading and plotting the data
data = pd.read_csv('data/data.csv', header=None)
X = np.array(data[[0, 1]])
y = np.array(data[2])
plot_points(X, y)
plt.show()


# Implementing the basics functions
# Softmax
def softmax(x):
    return (1/(1 + np.exp(-x)))


# prediction function
def prediction(features, weights, bias):
    return softmax(np.dot(features, weights) + bias)


# error
def error_formula(y, y_hat):
    return -y * np.log(y_hat) - (1 - y) * np.log(1 - y_hat)


# update weights
def update_weights(x, y, weights, bias, learning_rate):
    y_hat = prediction(x, weights, bias)
    error = y - y_hat
    weights += learning_rate * error * x
    bias += learning_rate * bias
    return weights, bias


# Training function
np.random.seed(44)

epochs = 100
learning_rate = 0.01


def train(features, targets, epochs, learnrate, graph_lines=False):

    errors = []
    n_records, n_features = features.shape
    last_loss = None
    weights = np.random.normal(scale=1 / n_features**.5, size=n_features)
    bias = 0
    for e in range(epochs):
        del_w = np.zeros(weights.shape)
        for x, y in zip(features, targets):
            output = prediction(x, weights, bias)
            error = error_formula(y, output)
            weights, bias = update_weights(x, y, weights, bias, learnrate)

        # Printing out the log-loss error on the training set
        out = prediction(features, weights, bias)
        loss = np.mean(error_formula(targets, out))
        errors.append(loss)
        if e % (epochs / 10) == 0:
            print("\n========== Epoch", e, "==========")
            if last_loss and last_loss < loss:
                print("Train loss: ", loss, "  WARNING - Loss Increasing")
            else:
                print("Train loss: ", loss)
            last_loss = loss
            predictions = out > 0.5
            accuracy = np.mean(predictions == targets)
            print("Accuracy: ", accuracy)
        if graph_lines and e % (epochs / 100) == 0:
            display(-weights[0]/weights[1], -bias/weights[1])

    # Plotting the solution boundary
    plt.title("Solution boundary")
    display(-weights[0]/weights[1], -bias/weights[1], 'black')
    plt.show()
    
    # Plotting the data
    plot_points(features, targets)
    plt.show()

    # Plotting the error
    plt.title("Error Plot")
    plt.xlabel('Number of epochs')
    plt.ylabel('Error')
    plt.plot(errors)
    plt.show()


# Time to train the algorithm!
train(X, y, epochs, learning_rate)
