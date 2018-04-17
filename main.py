from games.Zsir import Zsir
from Agent import Agent

# dummy values, should come from config
num_episodes = 100
training_interval = 10

if __name__ == "__main__":
    card_game = Zsir()

    player_1 = Agent(card_game)
    player_2 = Agent(card_game)

    state = card_game.reset()

    for e in range(num_episodes):

        state, done = player_1.play_turn(state)
        if done:
            break

        state, done = player_2.play_turn(state)
        if done:
            break

        if e % training_interval == 0:
            player_1.train(e)
            player_2.train(e)
