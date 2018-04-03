# this is my old thing from last semester

import gym
import time
from random import randint
from random import random
# env = gym.make('CartPole-v0')
env = gym.make('CartPole-v1')
b = [1,1,1,1,1,1,1,1]
bestReward = 0
ave = []
p = True
bestLast100 = 0
for k in range(10000):
    observation = env.reset()
    a = [0,0,0,0,0,0,0,0]
    for i in range(len(a)):
        a[i] = b[i]
    score = 0
    rand = randint(0,7)
    r2 = random()*2-1
    if i<9900:
        a[rand] = a[rand] + r2
    if k % 1000 == 0:
        print (k)
    for t in range(1000):
        # print observation
        action1 = a[0]*observation[0] + a[1]*observation[1] + a[2]*observation[2] + a[3]*observation[3]
        action2 = a[4]*observation[0] + a[5]*observation[1] + a[6]*observation[2] + a[7]*observation[3]
        action = 0
        if action1>action2:
            action = 0
        else:
            action = 1
        observation, reward, done, info = env.step(action)
        score += reward
        if done:
            if score > bestReward:
                bestReward = score
                for i in range(len(b)):
                    b[i] = a[i]
            ave.append(score)
            if len(ave)>=100 and p:
                last100ave = 0
                for i in range(100):
                    last100ave += ave[-(i+1)]
                last100ave /= 100
                if last100ave>475:
                    for i in range(100):
                        print (ave[-(i+1)])
                    p = False
                    print (k)
                if last100ave>bestLast100:
                    bestLast100 = last100ave
            break
print (bestLast100)
observation = env.reset()
totalScore = 0
for t in range(1000):
    env.render()
    action1 = b[0]*observation[0] + b[1]*observation[1] + b[2]*observation[2] + b[3]*observation[3]
    action2 = b[4]*observation[0] + b[5]*observation[1] + b[6]*observation[2] + b[7]*observation[3]
    action = 0
    if action1>action2:
        action = 0
    else:
        action = 1
    observation, reward, done, info = env.step(action)
    totalScore += reward
    if done:
        break
print (totalScore, b)
