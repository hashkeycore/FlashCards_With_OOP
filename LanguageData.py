import pandas as pd


class LanguageData:
    all_cards = []
    words_to_repeat = []

    def __init__(self):
        self.data = self.all_cards
        self.length = len(self.all_cards)


    def prep_data_for_panda(self):
        for word in self.data:
            french = word.french
            english = word.english
            self.words_to_repeat.append([french, english])

    @classmethod
    def write_csv(cls, path):
        df = pd.DataFrame(cls.words_to_repeat, columns=['French', 'English'])
        with open(path, 'w') as file:
            df.to_csv(file, index=0)

    @classmethod
    def read_from_csv(cls, path):
        with open(path, 'r') as file:
            words_data = pd.read_csv(file)
            words_dict = words_data.to_dict(orient='records')
            # Create Word Obj
            for word in words_dict:
                w = Word(word['French'], word['English'])
                cls.all_cards.append(w)
            # print(cls.all_obj)


class Word:
    def __init__(self, french: str, english: str):
        self.french = french
        self.english = english

    def __repr__(self):
        return f'Word[{self.french},{self.english}]'
