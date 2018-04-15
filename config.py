class NNConfig:
    def __init__(self):
        self.layers = 5
        self.layer_config = [32, 64, 32]
        self.dropout_rate = 0.5
        self.batch_size = 32