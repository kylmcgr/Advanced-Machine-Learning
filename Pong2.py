import gym
import numpy as np

environment = gym.make('Pong-ram-v0')

def determine_action(observation, weights ):
	weighted_sum = np.dot(observation, weights)
	action = 2 if weighted_sum < 0 else 3
	return action

def run_episode(environment, weights):
	observation = environment.reset()
	total_reward = 0
	for step in range(1000):
		action = determine_action(observation, weights)
		observation, reward, done, info = environment.step(action)
		total_reward += reward
		if done:
			break
	return total_reward

best_weights = None
best_reward = 0

# Let's search through 300 different random weights
for step in range(300):
    weights = np.random.rand(128) * 2 - 1
    reward = run_episode(environment, weights)
    if reward > best_reward:
       best_reward = reward
       best_weights = weights

observation = environment.reset()
cumulative_reward = 0

for step in range(0, 200):
    environment.render()
    action = determine_action(observation, best_weights)
    observation, reward, done, info = environment.step(action)
    cumulative_reward += reward
    if done:
        print("Reward when done: {}".format(cumulative_reward))
        if cumulative_reward == 200:
            print("Congrats! You successfully solved Cartpole V-0!")
        else:
            print("Unfortunately, even the best weights weren't enough")
        break
