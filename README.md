# perceptron
This project represents a single-layer neural network with 3 inputs and 1 output.

## What is a Perceptron?
In a very simple way we can see a Perceptron as a neural network that has no hidden layers, it only has output and input layers.
It is used to represent the most basic case scenarios of neural networks.

<p align="center">
  <img src="https://github.com/ryzenboi98/perceptron/blob/main/structure.png">
</p>

In the diagram above it is designed the structure of the Perceptron implemented. 

The provided data for the training is ruled by the first input that is exacly the result of the expected output.

It means that for the following example we would expect the following results:
```
[inputs] -> output
[1, 0, 1] -> 1
[0, 0, 1] -> 0
[1, 1, 1] -> 1
[0, 1, 0] -> 0
```

As we can see, it doesn't matter the value of the two second inputs the result is always the same value as the first input.




