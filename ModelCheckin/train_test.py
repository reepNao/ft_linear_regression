import numpy as np
import matplotlib.pyplot as plt
import json
import sys

def dataset():
    try:
        data = np.genfromtxt("data.csv", delimiter=",", skip_header=1)
    except Exception as e:
        print(f'Warning: Failed to load file! {e}')
        sys.exit(-1)
    
    m = len(data)
    x = data[:, 0].reshape(m, 1)
    Y = data[:, 1].reshape(m, 1)

    xmin = np.min(x)
    xmax = np.max(x)
    normX = (x - xmin) / (xmax - xmin)
    normX = np.hstack((normX, np.ones((m, 1))))  # Add bias term

    return x, normX, Y

def model(X, Theta):
    return X.dot(Theta)

def plot_prediction_curve(x, Y, prediction):
    plt.scatter(x, Y, marker='+', label='Data points')
    plt.plot(x, prediction, c='r', label='Prediction curve')
    plt.legend()
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('Prediction Curve')
    plt.show()

def load_parameters():
    try:
        with open("thetas.json", "r") as json_file:
            data = json.load(json_file)
        return data["theta0"], data["theta1"]
    except Exception as e:
        print(f"Failed to load thetas.json: {e}")
        sys.exit(-1)

def main():
    x, normX, Y = dataset()
    theta0, theta1 = load_parameters()
    prediction = theta0 + theta1 * normX[:, 0]
    
    plot_prediction_curve(x, Y, prediction)

if __name__ == '__main__':
    main()
