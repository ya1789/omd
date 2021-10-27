class CountVectorizer(object):

    def __init__(self):
        self.feature_names = dict()

    def fit_transform(self, corpus):
        # разбиваем предложения на слова
        words = []
        for sentence in corpus:
            words.append(sentence.lower().split())

        # составляем словарь уникальных пронумерованных слов
        for sentence in words:
            for word in sentence:
                if self.feature_names.get(word) is None:
                    self.feature_names.update({word: len(self.feature_names)})

        # векторизируем предложение
        out = []
        for sentence in words:
            array = [0] * len(self.feature_names)
            for word in sentence:
                array[self.feature_names[word]] += 1
            out.append(array)

        return out

    def get_feature_names(self):
        return list(self.feature_names.keys())


corpus = [
 'Crock Pot Pasta Never boil pasta again',
 'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(count_matrix)
