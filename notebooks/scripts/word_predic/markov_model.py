import numpy as np
import pandas as pd
import string
import gzip
import pickle

initial_word = {}
second_word = {}
transitions = {}


def load_data(path):
    df = []
    for line in gzip.open(path, 'rb'):
        df.append(eval(line))
    return pd.DataFrame.from_dict(df)


def remove_punctuation(sentence):
    return sentence.translate(str.maketrans('', '', string.punctuation))


def add2dict(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)


def list2probabilities(given_list):
    probability_dict = {}
    given_list_length = len(given_list)
    for item in given_list:
        probability_dict[item] = probability_dict.get(item, 0) + 1
    for key, value in probability_dict.items():
        probability_dict[key] = value / given_list_length
    return probability_dict


def train_markov_model(training_file):
    for line in open(training_file):
        tokens = remove_punctuation(line.rstrip().lower()).split()
        tokens_length = len(tokens)
        for i in range(tokens_length):
            token = tokens[i]
            if len(token) < 13:
                if i == 0:
                    initial_word[token] = initial_word.get(token, 0) + 1
                else:
                    prev_token = tokens[i - 1]
                    if i == tokens_length - 1:
                        add2dict(transitions, (prev_token, token), 'END')
                    if i == 1:
                        add2dict(second_word, prev_token, token)
                    else:
                        prev_prev_token = tokens[i - 2]
                        add2dict(transitions, (prev_prev_token, prev_token), token)

    initial_word_total = sum(initial_word.values())
    for key, value in initial_word.items():
        initial_word[key] = value / initial_word_total

    for prev_word, next_word_list in second_word.items():
        second_word[prev_word] = list2probabilities(next_word_list)

    for word_pair, next_word_list in transitions.items():
        transitions[word_pair] = list2probabilities(next_word_list)

    # print('Training successful.')


def sample_word(dictionary):
    p0 = np.random.random()
    cumulative = 0
    for key, value in dictionary.items():
        cumulative += value
        if p0 < cumulative:
            return key
    assert False


def generate(number_of_sentences):
    for i in range(number_of_sentences):
        sentence = []

        word0 = sample_word(initial_word)
        sentence.append(word0)

        word1 = sample_word(second_word[word0])
        sentence.append(word1)

        while True:
            word2 = sample_word(transitions[(word0, word1)])
            if word2 == 'END':
                break
            sentence.append(word2)
            word0 = word1
            word1 = word2
        print(i, ' '.join(sentence))


def generate_sentence_from_one_word(word):
    sentence = []

    sentence.append(word)

    word1 = sample_word(second_word[word])
    sentence.append(word1)

    while True:
        word2 = sample_word(transitions[(word, word1)])
        if word2 == 'END':
            break
        sentence.append(word2)
        word = word1
        word1 = word2
    # print(' '.join(sentence))
    return ' '.join(sentence)



imported_to_server = "../notebooks/scripts/word_predic/"
# imported_to_server = ""



data = load_data(imported_to_server + 'data/qa_Appliances.json.gz')
data = data['question'] + ' ' + data['answer']
data.to_csv(imported_to_server + 'data/qa_data.txt', sep='\t', index=False, header=False)
train_markov_model(imported_to_server + 'data/qa_data.txt')

if __name__ == '__main__':
    # generate(1)
    generate_sentence_from_one_word("is")