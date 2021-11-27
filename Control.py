from LanguageData import *
from random import randint


class Control:
    try:
        LanguageData.read_from_csv('data/words_to_repeat.csv')
    except:
        LanguageData.read_from_csv("data/french_words.csv")

    def __init__(self):
        self.control = LanguageData()
        self.card = None
        self.length = len(self.control.data)

    def get_card(self):
        self.card = self.control.data[randint(0, self.length)]
        print(self.card)
        #self.remove_card(self.card)
        #print(self.card)

    def remove_card(self, card):
        self.control.data.remove(card)


    def write_csv(self):
        self.control.prep_data_for_panda()
        LanguageData.write_csv('data/words_to_repeat.csv')


#c = Control()
#c.get_card()
