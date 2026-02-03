# lab.py


import pandas as pd
import numpy as np
import os
import re


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def match_1(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_1("abcde]")
    False
    >>> match_1("ab[cde")
    False
    >>> match_1("a[cd]")
    False
    >>> match_1("ab[cd]")
    True
    >>> match_1("1ab[cd]")
    False
    >>> match_1("ab[cd]ef")
    True
    >>> match_1("1b[#d] _")
    True
    """
    pattern = r'^..\[..\].*$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_2(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_2("(123) 456-7890")
    False
    >>> match_2("858-456-7890")
    False
    >>> match_2("(858)45-7890")
    False
    >>> match_2("(858) 456-7890")
    True
    >>> match_2("(858)456-789")
    False
    >>> match_2("(858)456-7890")
    False
    >>> match_2("a(858) 456-7890")
    False
    >>> match_2("(858) 456-7890b")
    False
    """
    pattern = r'^\(858\)\s\d{3}-\d{4}$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_3(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_3("qwertsd?")
    True
    >>> match_3("qw?ertsd?")
    True
    >>> match_3("ab c?")
    False
    >>> match_3("ab   c ?")
    True
    >>> match_3(" asdfqwes ?")
    False
    >>> match_3(" adfqwes ?")
    True
    >>> match_3(" adf!qes ?")
    False
    >>> match_3(" adf!qe? ")
    False
    """
    pattern = r'^[\w\s\?]{5,9}\?$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_4(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_4("$$AaaaaBbbbc")
    True
    >>> match_4("$!@#$aABc")
    True
    >>> match_4("$a$aABc")
    False
    >>> match_4("$iiuABc")
    False
    >>> match_4("123$$$Abc")
    False
    >>> match_4("$$Abc")
    True
    >>> match_4("$qw345t$AAAc")
    False
    >>> match_4("$s$Bca")
    False
    >>> match_4("$!@$")
    False
    """
    pattern = r'^[\$][^abc\$]*[\$][Aa]+[Bb]+[Cc]+$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_5(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_5("dsc80.py")
    True
    >>> match_5("dsc80py")
    False
    >>> match_5("dsc80..py")
    False
    >>> match_5("dsc80+.py")
    False
    """
    pattern = r'^[\w]+\.py$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_6(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_6("aab_cbb_bc")
    False
    >>> match_6("aab_cbbbc")
    True
    >>> match_6("aab_Abbbc")
    False
    >>> match_6("abcdef")
    False
    >>> match_6("ABCDEF_ABCD")
    False
    """
    pattern = r'^[a-z]+_[a-z]+$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_7(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_7("_abc_")
    True
    >>> match_7("abd")
    False
    >>> match_7("bcd")
    False
    >>> match_7("_ncde")
    False
    """
    pattern = r'^_.*_$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_8(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_8("ASJDKLFK10ASDO")
    False
    >>> match_8("ASJDKLFK0ASDo!!!!!!! !!!!!!!!!")
    True
    >>> match_8("JKLSDNM01IDKSL")
    False
    >>> match_8("ASDKJLdsi0SKLl")
    False
    >>> match_8("ASDJKL9380JKAL")
    True
    """
    pattern = r'^[^Oi1]+$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_9(string):
    '''
    DO NOT EDIT THE DOCSTRING!
    >>> match_9('NY-32-NYC-1232')
    True
    >>> match_9('ca-23-SAN-1231')
    False
    >>> match_9('MA-36-BOS-5465')
    False
    >>> match_9('CA-56-LAX-7895')
    True
    >>> match_9('NY-32-LAX-0000') # If the state is NY, the city can be any 3 letter code, including LAX or SAN!
    True
    >>> match_9('TX-32-SAN-4491')
    False
    '''
    pattern = r'^(NY-\d{2}-[A-Z]{3}-\d{4}|CA-\d{2}-(SAN|LAX)-\d{4})$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_10(string):
    '''
    DO NOT EDIT THE DOCSTRING!
    >>> match_10('ABCdef')
    ['bcd']
    >>> match_10(' DEFaabc !g ')
    ['def', 'bcg']
    >>> match_10('Come ti chiami?')
    ['com', 'eti', 'chi']
    >>> match_10('and')
    []
    >>> match_10('Ab..DEF')
    ['bde']
    
    '''
    clean = re.sub(r'[^\w]|a', '', string.lower())
    return re.findall(r'.{3}', clean)


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def extract_personal(s):
    return (re.findall(r'\w+@\w+\.[\w.]+', s), 
            re.findall(r'\d{3}-\d{2}-\d{4}', s), 
            re.findall(r'1\w{30,}', s),
            re.findall(r'\d+ [a-zA-Z]+ [a-zA-Z]+', s))


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def tfidf_data(reviews_ser, review):
    res = []
    words = review.split()
    for word in set(words):
        cnt = len(re.findall(fr'\b{word}\b', review))
        tf = cnt / len(words)
        idf = np.log(len(reviews_ser) / reviews_ser.str.contains(fr'\b{word}\b').sum())
        tfidf = tf * idf
        res.append({'word': word, 'cnt': cnt, 'tf': tf, 'idf': idf, 'tfidf': tfidf})
        
    return pd.DataFrame(res).set_index('word')

def relevant_word(out):
    return out.sort_values('tfidf', ascending=False).index[0]


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def hashtag_list(tweet_text):
    return tweet_text.apply(lambda x: re.findall(r'#([^\s]+)', x))

def most_common_hashtag(tweet_lists):
    all_tags = [tag for tags in tweet_lists for tag in tags]
    return tweet_lists.apply(lambda tags: max(tags, key=all_tags.count) if tags else np.nan)


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def create_features(ira):
    hashtags = hashtag_list(ira['text'])
    
    def clean(text):
        text = re.sub(r'https?://[^\s]+|@\w+|#[^\s]+|^RT', ' ', text)
        text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip().lower()
        return text
    text = ira['text'].apply(clean)
    
    return pd.DataFrame({
        'text': text,
        'num_hashtags': hashtags.apply(len),
        'mc_hashtags': most_common_hashtag(hashtags),
        'num_tags': ira['text'].apply(lambda x: len(re.findall(r'@\w+', x))),
        'num_links': ira['text'].apply(lambda x: len(re.findall(r'https?://[^\s]+', x))),
        'is_retweet': ira['text'].apply(lambda x: x.startswith('RT')),
    })
