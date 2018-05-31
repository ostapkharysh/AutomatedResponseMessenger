import pandas as pd
import gzip
from collections import Counter


def load_data(path):
    df = []
    for line in gzip.open(path, 'rb'):
        df.append(eval(line))
    return pd.DataFrame.from_dict(df)


if __name__ == "__main__":
    df = load_data('qa_Appliances.json.gz')
    df.head()
