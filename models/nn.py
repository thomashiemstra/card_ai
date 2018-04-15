from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
import numpy as np


class NeuralNetwork:
    def __init__(self, state_size, action_size, config):
        self.state_size = state_size
        self.action_size = action_size
        self.config = config
        self.model = self.build_model()

    def build_model(self):
        # standard neural network model
        mc = self.config
        model = Sequential()

        model.add(Dense(mc.layer_config[0], input_dim=self.state_size, activation='linear'))

        for x in mc.layer_config[1:]:
            model.add(Dense(x, activation='relu'))
            model.add(Dropout(mc.dropout_rate))

        model.add(Dense(self.action_size, activation='linear'))

        model.compile(loss='mean_squared_error',
                      optimizer=SGD())
        return model

    def act(self, state):
        state = np.array([state])
        return self.model.predict(state)

    def train(self, states, actions):
        mc = self.config
        self.model.fit(states, actions, batch_size=mc.batch_size)

