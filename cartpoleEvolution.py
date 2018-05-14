import gym
from EvolutionaryNeuralNet import Evolution, Genome
env = gym.make('CartPole-v1')
# env = gym.make('FrozenLake-v0')
evo = Evolution(4,[6],2)
def train():
    best = 0
    training = True
    numSolved = 0
    i = 0
    while(training):
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
        if evo.genomes[0].score >= 500:
            numSolved += 1
        else:
            numSolved = 0
        if numSolved == 10:
            training = False
        if evo.genomes[0].score >= best:
            print (evo.genomes[0].score)
            best = evo.genomes[0].score
        i += 1

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
    print("average score for trained network over 1000 simulations", sum(trained_rewards)/1000)
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
    print("average score for untrained network over 1000 simulations", sum(untrained_rewards)/1000)


train()
# show()
validate()
