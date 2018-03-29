# this is my old thing from last semester, I copied the weights after training so I wouldn't have to train each time

import gym
import time
from random import randint
from random import random
env = gym.make('MountainCar-v0')
b = [1.810671322762644, 0.43274226815281325, 3.2998817305126655, 0.836420592861991, 1.7865698513342276, 2.539112519087211]
ave = []
bestReward = -10
bestLast100 = -100000
for i in range(1000):
    observation = env.reset()
    a = [0,0,0,0,0,0]
    for i in range(len(a)):
        a[i] = b[i]
    cur = -10
    actualScore = 0
    score = 0
    rand = randint(0,5)
    r2 = random()*2-1
    if i<9900:
        a[rand] = a[rand] + r2
    for t in range(1000):
        action1 = a[0]*observation[0] + a[1]*observation[1]
        action2 = a[2]*observation[0] + a[3]*observation[1]
        action3 = a[4]*observation[0] + a[5]*observation[1]
        action = 0
        if action1>action2:
            if action1>action3:
                action = 0
            else:
                action = 2
        else:
            action = 1
        observation, reward, done, info = env.step(action)
        score -= reward
        actualScore += reward
        if observation[0]>cur:
            cur = observation[0]
        if done:
            # print("Episode finished after {} timesteps".format(t+1))
            score = 1000-score
            if score>cur:
                cur = score
                # print("On Finish")
                # print(a)
            break
    if cur > bestReward:
        bestReward = cur
        print(bestReward)
        for i in range(len(b)):
            b[i] = a[i]
        # print("On Change")
        # print(b)
        # print(a)
    ave.append(actualScore)
    if len(ave)>=100:
        last100ave = 0
        for i in range(100):
            last100ave += ave[-(i+1)]
        last100ave /= 100
        if last100ave>bestLast100:
            # print(last100ave)
            bestLast100 = last100ave


observation = env.reset()
# final = -10
# print("Before Final")
print(b)
observation = env.reset()
totalScore = 0
for t in range(10000):
    env.render()
    action1 = b[0]*observation[0] + b[1]*observation[1]
    action2 = b[2]*observation[0] + b[3]*observation[1]
    action3 = b[4]*observation[0] + b[5]*observation[1]
    action = 0
    if action1>action2:
        if action1>action3:
            action = 0
        else:
            action = 2
    else:
        action = 1
    observation, reward, done, info = env.step(action)
    # if observation[0]>final:
    #     final = observation[0]
    totalScore += reward
    if done:
        # print("Episode finished after {} timesteps".format(t+1))
        break
print (totalScore)
# print bestLast100
