import numpy as np
import matplotlib.pyplot as plt
import json
import sys

def thetas_values(theta0, theta1):
    thetas = {
        "theta0": theta0,
        "theta1": theta1,
    }
    try:
        with open("thetas.json", "w") as json_file:
            json.dump(thetas, json_file, indent=4)
    except:
        sys.exit(-1)

def pred_curve(x, Y, prediction):
    plt.scatter(x, Y, marker='*')
    plt.plot(x, prediction, c='r')
    plt.legend(['prediction curve: f(x)=θ1x+θ0'])
    plt.show()

def coef_determ(y, pred):
    a = ((y - pred)**2).sum()
    b = ((y - y.mean())**2).sum()
    coef = (1 - a / b) * 100
    print("The determination coefficient (R²) is : {:.{prec}f}%".format(coef, prec=2))
    return

def dataset():
    try:
        liste = np.genfromtxt("data.csv", delimiter=",", skip_header=1)
    except:
        print('Failed to load .csv file')
        sys.exit(-1)
    m = len(liste)
    x = np.array(liste[:, 0], float).reshape(m, 1)
    Y = np.array(liste[:, 1], float).reshape(m, 1)
    xmin = np.min(x)
    xmax = np.max(x)
    normX = (x - xmin) / (xmax - xmin)
    normX = np.hstack((normX, np.ones((m, 1))))  # Add bias term
    Theta = np.random.randn(2, 1)  # Ensure Theta has shape (2, 1)
    return x, normX, Y, Theta

def model(X, Theta):
    return X.dot(Theta)

def cost_function(m, X, Y, Theta):
    return (1 / (2 * m)) * np.sum((model(X, Theta) - Y)**2)

def gradient_descent(X, Y, Theta, learning_rate, n_iterations):
    m = len(Y)
    for i in range(n_iterations):
        Theta -= learning_rate * (1 / m) * X.T.dot(model(X, Theta) - Y)
    return Theta

def ft_linear_regression():
    learning_rate = 0.10
    n_iterations = 2000
    x, normX, Y, Theta = dataset()
    final_Theta = gradient_descent(normX, Y, Theta, learning_rate, n_iterations)
    prediction = model(normX, final_Theta)
    return x, Y, prediction, final_Theta

def argument_parser():
    x, Y, prediction, final_Theta = ft_linear_regression()
    pred_curve(x, Y, prediction)
    coef_determ(Y, prediction)
    thetas_values(final_Theta[1].item(), final_Theta[0].item())

if __name__ == '__main__':
    argument_parser()
