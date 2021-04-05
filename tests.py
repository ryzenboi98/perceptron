import numpy as np

from perceptron import Perceptron

X_train = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1],
])

y_train = np.array([0, 0, 1, 1, 0])

X_test = np.array([
    [0, 0, 1],
    [1, 1, 1],
    [0, 1, 1],
    [1, 1, 0],
    [1, 0, 0],
])

y_test = np.array([0, 1, 0, 1, 1])

def accuracy(y, y_pred):
    accuracy = np.sum(y == y_pred) / len(y)
    return accuracy

p = Perceptron(learning_rate=0.01, epochs=10000)
p.train(X_train, y_train)
print("Trained weights")
print(p.weights)

predictions = p.predict(X_test)
print('Predictions')
print(predictions)

print("Accuracy -> ", accuracy(y_test, predictions))