import gym
import numpy as np

environment = gym.make('SpaceInvaders-ram-v0')

def determine_action(observation, weights ):
    weighted_sum = np.dot(observation, weights)
    action = 0
    if weighted_sum > 1:
        if weighted_sum > 2:
            if weighted_sum > 3:
                if weighted_sum > 4:
                    action = 4
                else:
                    action = 3
            else:
                action = 2
        else:
            action = 1
    return action

def run_episode(environment, weights):
	observation = environment.reset()
	total_reward = 0
	for step in range(100000):
		action = determine_action(observation, weights)
		observation, reward, done, info = environment.step(action)
		total_reward += reward
		if done:
			break
	return total_reward

best_weights = None
best_reward = 0

# Let's search through 300 different random weights
for step in range(1000):
    weights = np.random.rand(128) * 2 - 1
    reward = run_episode(environment, weights)
    if reward > best_reward:
       best_reward = reward
       best_weights = weights
    print(step)

observation = environment.reset()
cumulative_reward = 0

for step in range(0, 100000):
    environment.render()
    action = determine_action(observation, best_weights)
    observation, reward, done, info = environment.step(action)
    cumulative_reward += reward
    if done:
        print("Reward when done: {}".format(cumulative_reward))
        break
