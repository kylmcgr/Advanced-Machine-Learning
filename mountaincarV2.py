import gym
from EvolutionaryNeuralNet import Evolution, Genome
env = gym.make('MountainCar-v0')
# env = gym.make('FrozenLake-v0')
evo = Evolution(2,[6],3)
def train():
    best = -1
    for i in range(200):
        print (i)
        for genome in evo.genomes:
            observation = env.reset()
            score = 0
            right = -1
            for t in range(200):
                actions = genome.network.compute(observation)
                action = 0
                if actions[0]>actions[1]:
                    if actions[0]>actions[2]:
                        action = 0
                    else:
                        action = 2
                else:
                    action = 1
                observation, reward, done, info = env.step(action)
                score += reward
                if observation[0]>right:
                    right = observation[0]
                if done:
                    score = score + 300
                    break
            if score == -200:
                genome.score = right
            else:
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
            if actions[0]>actions[2]:
                action = 0
            else:
                action = 2
        else:
            action = 1
        observation, reward, done, info = env.step(action)
        score += reward
        if done:
            score = 1000-score
            break
    print (score)

def validate():
    trained_rewards = []
    trained_genome = evo.genomes[0]
    for i in range(1000):
        observation = env.reset()
        score = 0
        for t in range(1000):
            # env.render()
            actions = trained_genome.network.compute(observation)
            action = 0
            if actions[0]>actions[1]:
                action = 0
            else:
                action = 1
            observation, reward, done, info = env.step(action)
            score += reward
            if done:
                break
        trained_rewards.append(score)
    print(sum(trained_rewards)/1000)
    untrained_rewards = []
    untrained_genome = Genome(4,[6],2)
    for i in range(1000):
        observation = env.reset()
        score = 0
        for t in range(1000):
            # env.render()
            actions = untrained_genome.network.compute(observation)
            action = 0
            if actions[0]>actions[1]:
                action = 0
            else:
                action = 1
            observation, reward, done, info = env.step(action)
            score += reward
            if done:
                break
        untrained_rewards.append(score)
    print(sum(untrained_rewards)/1000)

train()
# show()
validate()
