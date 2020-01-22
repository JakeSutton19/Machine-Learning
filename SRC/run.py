import numpy as np
from dqn_keras import Agent
from utils import make_env


if __name__ == '__main__':
    # env = make_env('PongNoFrameskip-v4')
    env = make_env('ChromeDinoNoBrowser-v0')
    # env = make_env('ChromeDino-v0')

    num_games = 1000
    load_checkpoint = False
    best_score = 0
    agent = Agent(gamma=0.99, epsilon=1.0, alpha=0.001,
                  input_dims=(4,84,84), n_actions=3, mem_size=25000,
                  eps_min=0.02, batch_size=64, replace=1000, eps_dec=1e-5)

    if load_checkpoint:
        agent.load_models()

    scores, eps_history = [], []
    n_steps = 0

    for i in range(num_games):
        done = False
        observation = env.reset()
        score = 0
        n_steps = 0
        while not done:
            action = agent.choose_action(observation)
            observation_, reward, done, info = env.step(action)
            n_steps += 1
            score += reward
            if not load_checkpoint:
                agent.store_transition(observation, action,
                                     reward, observation_, int(done))
                agent.learn()
            # else:
            #     env.render()
            observation = observation_

        scores.append(score)

        avg_score = np.mean(scores[-100:])
        print('episode: ', i,'score: %.1f' % score, ' average score %.1f' % avg_score, ' best score %.1f' % best_score, 'epsilon %.3f' % agent.epsilon, 'steps', n_steps)
        if score > best_score:
            agent.save_models()
            print('####  Model Saved. ###')
            best_score = score

        eps_history.append(agent.epsilon)

    agent.save_models()
    print('\nFinal Model Saved.\n')

