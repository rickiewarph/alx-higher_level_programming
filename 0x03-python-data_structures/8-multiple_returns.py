#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        sent_length = len(sentence)
    else:
        sent_length = 0
    return (sent_length, sentence if not sentence else sentence[:1])
