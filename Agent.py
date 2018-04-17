

class Agent():

    def __init__(self, card_game):
        self.card_game = card_game

        # initialize neural networks

        # initialize replay memories a circular buffer and a reservoir
        # get some config files like Eta
        pass

    def play_turn(self, state):

        # decide policy

        # action = policy(state)
        # next_state, reward, done, _ = env.step(action)
        # save [state, action, reward, next_state, done]
        # save [state, action] if DQN is used

        # return next_state for the other player and done in case we need to stop

        pass

    def train(self, episode):
        # train the networks
        # update target network if episode % period == 0
        pass





