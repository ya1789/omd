from collections import Counter
import math

class CountVectorizer:

    def __init__(self):
        self.feature_names = {}

    def get_feature_names(self):
        return list(self.feature_names.keys())

    def set_feature_names(self, corpus):
        idx = 0
        for sentence in corpus:
            sentence = sentence.lower().split(' ')
            for word in sentence:
                if word not in self.feature_names.keys():
                    self.feature_names[word] = idx
                    idx += 1
        return self.feature_names

    def fit_transform(self, corpus):
        matrix = []
        self.set_feature_names(corpus)
        for sentence in corpus:
            sentence = sentence.lower().split(' ')
            feature_freq = [0] * len(self.feature_names)
            cnt = Counter(sentence)
            for k in cnt.keys():
                feature_freq[self.feature_names[k]] = cnt[k]
            matrix.append(feature_freq)
        return matrix


def tf_transform(count_matrix):
    tf_matrix = []
    for vector in count_matrix:
        word_cnt = sum(vector)
        tf_row = [round(i / word_cnt, 3) for i in vector]
        tf_matrix.append(tf_row)
    return tf_matrix


def idf_transform(count_matrix):
    n_docs = len(count_matrix)
    word_freq = [0] * len(count_matrix[0])
    for vector in count_matrix:
        word_freq = [j + bool(k) for j, k in zip(word_freq, vector)]
    return [round(math.log((n_docs + 1) / (word + 1)) + 1, 3) for word in word_freq]


class TfidfTransformer:
    def tf_transform(self, count_matrix):
        tf_matrix = []
        for vector in count_matrix:
            word_cnt = sum(vector)
            tf_row = [round(i / word_cnt, 3) for i in vector]
            tf_matrix.append(tf_row)
        return tf_matrix

    def idf_transform(self, count_matrix):
        n_docs = len(count_matrix)
        word_freq = [0] * len(count_matrix[0])
        for vector in count_matrix:
            word_freq = [j + bool(k) for j, k in zip(word_freq, vector)]
        return [round(math.log((n_docs + 1) / (word + 1)) + 1, 3) for word in word_freq]

    def fit_transform(self, count_matrix):
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        tfidf_matrix = [[round(x * y, 3) for x, y in zip(tf_vec, idf)] for tf_vec in tf]
        return tfidf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tf_idf = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self.tf_idf.fit_transform(count_matrix)

if __name__ == '__main__':
    corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)

    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    tf_matrix = tf_transform(count_matrix)
    print(tf_matrix)
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    idf_matrix = idf_transform(count_matrix)
    print(idf_matrix)
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
