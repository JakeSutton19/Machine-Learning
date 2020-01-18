
from Agent.__init__ import Agent
from functions import *
import sys

if len(sys.argv) != 4:
	print("Usage: python train.py [stock] [window] [episodes]")
	exit()

stock_name, window_size, episode_count = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

agent = Agent(window_size)
data = getNCAADataVec(stock_name)
l = len(data) - 1
batch_size = 32

for e in range(episode_count + 1):
	print("Episode " + str(e) + "/" + str(episode_count))
	state = getState(data, 0, window_size + 1)

	total_profit = 0
	agent.inventory = []
	win_count = 0
	loss_count = 0

	for t in range(l):
		action = agent.act(state)

		# sit
		next_state = getState(data, t + 1, window_size + 1)
		reward = 0

		if action == 1: # buy
			agent.inventory.append(data[t])
			print("Win: {}".format(win_count))
			win_count += 1

		elif action == 2 and len(agent.inventory) > 0: # sell
			bought_price = agent.inventory.pop(0)
			reward = max(data[t] - bought_price, 0)
			total_profit += data[t] - bought_price
			print("Loss: {}".format(loss_count))
			loss_count += 1

		done = True if t == l - 1 else False
		agent.memory.append((state, action, reward, next_state, done))
		state = next_state

		if done:
			print( "--------------------------------")
			print( "Wins: {}, Losses: {}".format(win_count, loss_count))
			print( "--------------------------------")

		if len(agent.memory) > batch_size:
			agent.expReplay(batch_size)

	if e % 10 == 0:
		agent.model.save("/home/human/NCAA/SRC/Models/model_ep" + str(e))
