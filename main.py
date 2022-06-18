import numpy 
import matplotlib

# goal of practice, have less than 50 precent error rate of MNIST 
# Specs of neural network, fully connected, sigmoid 

# What does a model need?
# 1) Input space size
# 2) Output space size
# 3) How many layers and their sizes 
class Model():
    def __init__(self, inputSpace, outputSpace, layerCount, neuronType):
        self.inputSpace = inputSpace
        self.outputSpace = outputSpace
        self.createLayers(layerCount, neuronType)

    def createLayers(layerCount):
        for layer in layerCount:
            return 0 

#neuron type, sigmoid or RELU 
class Layer():
    def __init__(self, neuronCount, neuronType):
        self.generateNeurons = neuronCount
        self.neuronType = neuronType
        self.neuronList = []

    def generateNeurons(neuronCount):
        for neuron in neuronCount:
            neuronList.append(Neuron(self.neuronType))
        return 0 

# What does a neuron need to do?
# 1) Connection to other neurons, input or output
# 2) These connections need to contain a weight 
class Neuron(neuronType):
    def __init__(self):
        self.neuronType = neuronType 

