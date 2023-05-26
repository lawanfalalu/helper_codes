import re
import pandas as pd

def sentence_pairs(text):
    sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)
    pairs = [(sentences[i], sentences[i+1]) for i in range(len(sentences)-1)]
    df = pd.DataFrame(pairs, columns=['Sentence 1', 'Sentence 2'])
    return df

paragraphs = """ This is the first sentence. This is the second sentence. This is the third sentence. This is the fourth sentence. This is the fifth sentence."""

sentence_pairs(paragraphs)