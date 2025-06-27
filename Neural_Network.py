import random
#import topological_sorting # if you are somebody else, don't mind this, it's not that important

class Bot:
    def __init__(self, neurons):
        self.neurons = neurons
        self.outputs = {}

    # def topologically_sort(self): WIP
    #     unsorted_nodes = []
    #     for node in self.neurons:
    #         unsorted_nodes.append(node[:2])
    #     sorted_nodes = topological_sorting.topologically_sort(unsorted_nodes)
    #
    #     new_neurons = [None] * len(sorted_nodes)
    #     for neuron in self.neurons:
    #         id = neuron[0]
    #         index = sorted_nodes.index(id)
    #         new_neurons[index] = neuron
    #     self.neurons = new_neurons

    def calculate(self, inputs): # inputs -> {neuron_id: input, ...}
        self.outputs = self.neurons

        for input in inputs.items():
            self.outputs[input[0]] = input[1]

        # print(self.outputs)

        for neuron in self.neurons.items():
            if neuron[0] not in inputs.keys():
                neuron_id = neuron[0]
                parent_weights = neuron[1][0]
                neuron_bias = neuron[1][1]

                # print(tuple(parent_weights.items()))

                total = 0
                for parent in tuple(parent_weights.items()):
                    parent_id = parent[0]
                    parent_weight = parent[1]

                    # print(parent_weight)

                    total += parent_weight * self.outputs[parent_id]

                total += neuron_bias

                if total < 0:
                    total = 0

                self.outputs[neuron_id] = total

                print(f"{neuron_id}: {total}")

                # print("-")

if __name__ == "__main__":

    test_neurons = {

        0: "input",
        1: "input",
        2: [{0: -100, 1: 1}, 0],
        3: [{0: 1, 1: 1}, 0],
        4: [{0: 1, 1: 1}, 0],
        5: [{2: 1, 3: 1, 4: 1}, 0],
        6: [{2: 1, 3: 1, 4: 1}, 0],

    }

    random_neurons = {

        0: "input",
        1: "input",
        2: [{0: random.random(), 1: random.random()}, random.random()],
        3: [{0: random.random(), 1: random.random()}, random.random()],
        4: [{0: random.random(), 1: random.random()}, random.random()],
        5: [{2: random.random(), 3: random.random(), 4: random.random()}, random.random()],
        6: [{2: random.random(), 3: random.random(), 4: random.random()}, random.random()],

    }

    # neuron_id: [{parent_id: parent_weight, ... }, bias]

    bot = Bot(test_neurons)

    bot.calculate({0: 37, 1: 73})
