import nltk

'calculates number of sentences within essay'


def num_sents(essay):

    return len(nltk.sent_tokenize(essay))


'calculates number of words wtihin essay'


def num_words(essay):

    counter = 0
    sents = nltk.sent_tokenize(essay)
    for sent in sents:
        counter += len(nltk.word_tokenize(sent))
    return counter


'calculates average sentence length within essay'


def avg_sent(essay):

    counter = 0
    sents = nltk.sent_tokenize(essay)
    for sent in sents:
        counter += len(nltk.word_tokenize(sent))
    return round(counter / len(sents), 4)


'simplifies the grade from each different essay set into a range from 0-3'


def grade(s_num, d_score):
    if s_num == 1:
        if 2 <= d_score <= 3:
            return 0
        elif 3 < d_score <= 6:
            return 1
        elif 6 < d_score <= 9:
            return 2
        else:
            return 3
    elif s_num == 2:
        if d_score == 1:
            return 0
        elif 2 <= d_score <= 3:
            return 1
        elif 3 < d_score <= 5:
            return 2
        else:
            return 3
    else:
        return d_score


def get_features(essay):

    return num_sents(essay), num_words(essay), avg_sent(essay)