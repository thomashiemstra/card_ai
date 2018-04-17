from abc import ABC, abstractmethod


class AbstractCardGame(ABC):

    @abstractmethod
    def reset(self):
        # reset the game and return an observation of the game like observe()
        pass

    @abstractmethod
    def play(self, action):
        # play an action, must be an int or a numpy int array
        # also return the new state of the game (numpy array of ints), reward (int) and done (boolean)
        # returns np.array(state), reward, done
        pass

    @abstractmethod
    def check_legality_actions(self, actions):
        # input: array of proposed scores per action
        # put all the scores of illegal moves to zero
        # example move 0 illegal [0.5, 0.3, 0.2] -> [0, 0.3, 0.2]
        pass
