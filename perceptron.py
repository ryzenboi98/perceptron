import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, epochs=10000):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def train(self, X, y):
        n_samples, n_features = X.shape

        # init weights
        self.weights = np.zeros(n_features)
        self.bias = 0

        y_ = np.array([1 if i > 0 else 0 for i in y])

        for _ in range(self.epochs):
            for i, x_i in enumerate(X):
                sum = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_function(sum)

                adjustments = self.lr * (y_[i] - y_predicted)


                self.weights += adjustments * x_i
                self.bias += adjustments

    def predict(self, X):
        sum = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_function(sum)

        return y_predicted

    def activation_function(self, x):
        return np.where(x >= 0, 1, 0)
