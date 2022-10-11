class CountVectorizer():
    def __init__(self):
        self.names_numerated = dict()

    def fit_transform(self, corpus):
        words_list = []
        out = []
        for line in corpus:
            words_list.append((line.lower()).split())
        for line in words_list:
            for word in line:
                if self.names_numerated.get(word) is None:
                    self.names_numerated.update({word: len(self.names_numerated)})
        for line in words_list:
            vector = [0] * len(self.names_numerated)
            for word in line:
                vector[self.names_numerated[word]] += 1
            out.append(vector)

        return out

    def get_feature_names(self):
        return list(self.names_numerated.keys())


if __name__ == "__main__":
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
