import gzip
import random
import string
import numpy as np
import pandas as pd


def load_data(path):
    df = []
    for line in gzip.open(path, 'rb'):
        df.append(eval(line))
    return pd.DataFrame.from_dict(df)


# df = load_data('data/qa_Appliances.json.gz')
# df = df['question'] + ' ' + df['answer']
# df.to_csv('data/qa_data.txt', sep='\t', index=False, header=False)

training_data_file = 'data/qa_data.txt'


class MarkovChain:

    def __init__(self):
        self.memory = {}

    def _learn_key(self, key, value):
        if key not in self.memory:
            self.memory[key] = []

        self.memory[key].append(value)

    def learn(self, text):
        tokens = text.split(" ")
        bigrams = [(tokens[i], tokens[i + 1]) for i in range(0, len(tokens) - 1)]
        for bigram in bigrams:
            self._learn_key(bigram[0], bigram[1])

    def _next(self, current_state):
        next_possible = self.memory.get(current_state)

        if not next_possible:
            next_possible = self.memory.keys()

        return random.sample(next_possible, 1)[0]

    def babble(self, amount, state=''):
        if not amount:
            return state

        next_word = self._next(state)
        return state + ' ' + self.babble(amount - 1, next_word)


if __name__ == '__main__':
    m = MarkovChain()
    training_data_file = 'data/qa_data.txt'
    for line in open(training_data_file):
        m.learn(line)
    print(m.babble(20, 'I'))
