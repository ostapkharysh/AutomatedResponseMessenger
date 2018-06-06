initial_word = {}
lst = [['i', 'have', 'a', '9', 'year', 'old', 'badger', '1', 'that', 'needs', 'replacing', 'will', 'this', 'badger', '1', 'install', 'just', 'like', 'the', 'original', 'one', 'i', 'replaced', 'my', 'old', 'one', 'with', 'this', 'without', 'a', 'hitch'], ['model', 'number', 'this', 'may', 'help', 'insinkerator', 'model', 'badger1', 'badger', '1', '13', 'hp', 'garbage', 'disposal', 'product', 'details', 'bellacor', 'number309641', 'upc050375000419', 'brand', 'sku500181']]

for tokens in lst:
    for i in range(len(tokens)):
        token = tokens[i]
        if len(token) < 13:
            if i == 0:
                initial_word[token] = initial_word.get(token, 0) + 1
            else:
                prev_token = tokens[i - 1]
                # if i == len(tokens) - 1:
                #     add2dict(transitions, (prev_token, token), 'END')
                # if i == 1:
                #     add2dict(second_word, prev_token, token)
                # else:
                #     prev_prev_token = tokens[i - 2]
                #     add2dict(transitions, (prev_prev_token, prev_token), token)
        else:
            pass
