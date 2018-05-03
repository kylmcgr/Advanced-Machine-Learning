import gym
from EvolutionaryNeuralNet import Evolution
env = gym.make('CartPole-v1')
# env = gym.make('FrozenLake-v0')
evo = Evolution(4,[6],2)
def train():
    best = 0
    for i in range(100):
        print (i)
        for genome in evo.genomes:
            observation = env.reset()
            score = 0
            for t in range(500):
                actions = genome.network.compute(observation)
                action = 0
                if actions[0]>actions[1]:
                    action = 0
                else:
                    action = 1
                observation, reward, done, info = env.step(action)
                score += reward
                if done:
                    break
            genome.score = score
        evo.evolve()
        if evo.genomes[0].score > best:
            print (evo.genomes[0].score)
            best = evo.genomes[0].score

def show():
    observation = env.reset()
    score = 0
    for t in range(1000):
        env.render()
        actions = evo.genomes[0].network.compute(observation)
        action = 0
        if actions[0]>actions[1]:
            action = 0
        else:
            action = 1
        observation, reward, done, info = env.step(action)
        score += reward
        if done:
            break
    print (score)
train()
show()
