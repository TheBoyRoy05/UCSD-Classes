# project.py


import pandas as pd
import numpy as np
from pathlib import Path
import re
import requests
import time


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def get_book(url):
    time.sleep(0.5)
    text = requests.get(url).text.replace('\r\n', '\n')
    
    start_pattern = r"\*\*\* START OF THE PROJECT GUTENBERG EBOOK [^\*]+ \*\*\*"
    end_pattern = r"\*\*\* END OF THE PROJECT GUTENBERG EBOOK [^\*]+ \*\*\*"
    start_match = re.search(start_pattern, text)
    end_match = re.search(end_pattern, text)
    
    return text[start_match.end():end_match.start()]


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def tokenize(book_string):
    tokens = ['\x02']
    paragraphs = re.split(r'\n{2,}', book_string.strip())
    token_pattern = re.compile(r"\w+|[^\w\s]")
    
    for paragraph in paragraphs:
        if paragraph.strip():
            paragraph_tokens = token_pattern.findall(paragraph)
            tokens.extend(paragraph_tokens)
            tokens.extend(['\x03', '\x02'])
    
    if tokens[-1] == '\x02': tokens.pop()
    if tokens[-1] != '\x03': tokens.append('\x03')
    
    return tokens


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


class UniformLM(object):
    def __init__(self, tokens):
        self.mdl = self.train(tokens)
        
    def train(self, tokens):
        return pd.Series(list(set(tokens))).value_counts(normalize=True)
    
    def probability(self, words):
        return np.prod(np.array([self.mdl[word] if word in self.mdl else 0 for word in words]))
        
    def sample(self, M):
        return " ".join(np.random.choice(self.mdl.index, p=self.mdl.values, size=M))


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


class UnigramLM(object):
    def __init__(self, tokens):
        self.mdl = self.train(tokens)
        
    def train(self, tokens):
        return pd.Series(tokens).value_counts(normalize=True)
    
    def probability(self, words):
        return np.prod(np.array([self.mdl[word] if word in self.mdl else 0 for word in words]))
        
    def sample(self, M):
        return " ".join(np.random.choice(self.mdl.index, p=self.mdl.values, size=M))


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


class NGramLM(object):
    def __init__(self, N, tokens):
        self.N = N
        ngrams = self.create_ngrams(tokens)

        self.ngrams = ngrams
        self.mdl = self.train(ngrams)

        if N < 2:
            raise Exception('N must be greater than 1')
        elif N == 2:
            self.prev_mdl = UnigramLM(tokens)
        else:
            self.prev_mdl = NGramLM(N-1, tokens)

    def create_ngrams(self, tokens):
        return [tuple(tokens[i:i + self.N]) for i in range(len(tokens) - self.N + 1)]
        
    def train(self, ngrams):
        ncounts = pd.Series(ngrams).value_counts()
        
        n1gram = pd.Series([ngram[:-1] for ngram in ngrams])
        n1counts = n1gram.value_counts()
        
        probs = pd.Series([ncounts[key] / n1counts[key[:-1]] for key in ngrams])
        df = pd.DataFrame({'ngram': ngrams, 'n1gram': n1gram, 'prob': probs})
        return df.drop_duplicates(ignore_index=True)
    
    def probability(self, words):
        tuples = [tuple(words[max(0, i - self.N):i]) for i in range(1, len(words) + 1)]
        prob = 1
        for tup in tuples:
            LM = self
            for _ in range(self.N - len(tup)):
                LM = LM.prev_mdl
                
            probs = LM.mdl.set_index('ngram')['prob'] if len(tup) != 1 else LM.mdl
            tup = tup[0] if len(tup) == 1 else tup
            prob *= probs[tup] if tup in probs.index else 0
            
        return prob

    def sample(self, M):
        res = ["\x02"]
        for i in range(M - 1):
            LM = self
            for _ in range(self.N - i - 2):
                LM = LM.prev_mdl
                
            choices = LM.mdl[LM.mdl['n1gram'] == tuple(res[-self.N + 1:])]
            res.append(np.random.choice(choices['ngram'], p=choices['prob'])[-1])
            
        res.append("\x03")
        return " ".join(res)