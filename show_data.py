import pandas as pd
import gzip
from collections import Counter



def parse(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)

def getDF(path):
    i = 0
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')

df = getDF('qa_Appliances.json.gz')

lst = []
for i in range(len(df)):
    if len(df['answer'][i]) <= 10:
        #print("QUESTION:")
        #print(df['question'][i])
        #print("ANSWER:")
        #print(df['answer'][i])
        lst.append(df['answer'][i].strip(".!").lower())
        #print()

print(Counter(lst))