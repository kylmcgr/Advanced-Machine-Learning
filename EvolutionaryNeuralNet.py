import random
import numpy as np

class Neuron:

    def __init__(self, numInputs):
        self.value = 0
        self.weights = []
        for i in range(numInputs):
            self.weights.append(random.random()*2-1)


class Layer:

    def __init__(self, numNeurons, numInputs):
        self.neurons = []
        for i in range(numNeurons):
            self.neurons.append(Neuron(numInputs))

class Network:

    def __init__(self, inputs, hiddens, outputs):
        self.layer = []
        self.layer.append(Layer(inputs,0))
        previous = inputs
        for i in hiddens:
            self.layer.append(Layer(i, previous))
            previous = i
        self.layer.append(Layer(outputs,previous))

    def sigmoid(self, value):
        return .5 * (1 + np.tanh(.5 * value))

    def compute(self, inputs):
        for i in range(len(inputs)):
            self.layer[0].neurons[i].value = inputs[i]
        for i in range(1,len(self.layer)):
            previous = self.layer[i-1]
            for j in range(len(self.layer[i].neurons)):
                total = 0
                for k in range(len(previous.neurons)):
                    total += self.layer[i].neurons[j].weights[k]*previous.neurons[k].value
                self.layer[i].neurons[j].value = self.sigmoid(total)
        output = []
        for i in self.layer[-1].neurons:
            output.append(i.value)
        return output

    def setWeights(self, newWeights):
        for i in range(len(self.layer)):
            for j in range(len(self.layer[i].neurons)):
                for k in range(len(self.layer[i].neurons[j].weights)):
                    self.layer[i].neurons[j].weights[k]=newWeights[i][j][k]

    def printWeights(self):
        weights = []
        for i in range(len(self.layer)):
            weights.append([])
            for j in range(len(self.layer[i].neurons)):
                weights[i].append(self.layer[i].neurons[j].weights)
        return weights

class Genome:

    def __init__(self, inputs, hiddens, outputs):
        self.network = Network(inputs, hiddens, outputs)
        self.mutationRate = 0.2
        self.mutationRange = 0.3
        self.score = 0

    def child(self, other):
        for i in range(len(self.network.layer)):
            l = self.network.layer[i]
            for j in range(len(l.neurons)):
                n = l.neurons[j]
                for k in range(len(n.weights)):
                    if (random.random()>0.5):
                        n.weights[k] = other.network.layer[i].neurons[j].weights[k]
                    if (random.random()>self.mutationRate):
                        n.weights[k] = self.mutationRange * (random.random()*2-1)

class Evolution:

    def __init__(self, inp, hid, out):
        self.inputs = inp
        self.hiddens = hid
        self.outputs = out
        self.population = 100
        self.continueRate = 0.2
        self.newRate = 0.2
        self.genomes = []
        for i in range(self.population):
            self.genomes.append(Genome(self.inputs, self.hiddens, self.outputs))

    def evolve(self):
        self.genomes.sort(key=lambda x: x.score, reverse=True)
        nextGen = []
        for i in range((int)(self.continueRate*self.population)):
            nextGen.append(self.genomes[i])
        for i in range((int)(self.newRate*self.population)):
            nextGen.append(Genome(self.inputs, self.hiddens, self.outputs))
        while len(nextGen)<self.population:
            for i in range(len(nextGen)):
                for j in range(i):
                    childGenome = nextGen[i]
                    childGenome.child(nextGen[j])
                    nextGen.append(childGenome)
                    if len(nextGen)>=self.population:
                        self.genomes = nextGen
                        return
