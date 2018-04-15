from models.nn import NeuralNetwork
from config import NNConfig


if __name__ == "__main__":

    config = NNConfig()
    nn = NeuralNetwork(4, 1, config)

