import pandas as pd


def load_lda():
    """
    Load LDA files, output from Mallet
    - dist: tabular file with document-topic distributions (note: remove first two columns from the original Mallet output)
    - words: topic-word scores
    - data: custom metadata, the same length as the dist variable
    - keys: custom labels in a dictionary, tied to the topic index, like this: {0:"economy",1:"health"}
    """

    dist = pd.read_csv('/path/tolda/full-postwar/dists-speech-bound-250',sep='\t')
    words = pd.read_csv('/path/tolda/full-postwar/ww-speech-bound-250',sep='\t',header=None)
    data = pd.read_csv('/path/tolda/full-postwar/data-speech-level-full.tsv',sep='\t',parse_dates=['date'])
    keys = pd.read_csv('/path/tolda/full-postwar/keys-speech-bound-250',sep='\t',header=0)
    keys = dict(zip(keys['index'],keys['label']))
    return words, dist, data, keys