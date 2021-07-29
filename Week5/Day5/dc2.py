#  a class is a blueprint which enables you to create multple of the same things easily
#  an instance is one item created from a class
#  prevents users from accesing information in the class that we dont want them tp have access to
#  abstraction is not knowing how a class works internally but uses it for their uses externally of the class
# inheritance is when one class takes another class as a parameter and gains all its parents methods
#  you can inherit methods from two different classes but the first one is the dominant one
#  polymorphism is using the same method name for different instances and getting different results
#  the rules in which a class inherits from its ancestors and the order
import random
class Card():
    def __init__(self) -> None:
        self.suit =["heart","diamond","spade","club"]
        self.card = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"] 
    def get_card(self):
        suit = random.choice(self.suit)
        value = random.choice(self.card)
        card = value + " " + suit
        return card
    def get_deck(self):
        deck = []
        for suit in self.suit:
            for value in self.card:
                card = value + " " + suit
                deck.append(card)
        return deck        
 
class Deck(Card):
    def shuff_deck(self):
        x = self.get_deck()
        random.shuffle(x)
        return x
       
    def deal_card(self):
        deck = self.shuff_deck()
        card = deck.pop()
        return card

x = Card()
y = Deck()
# print(x.get_card()) 
# print(x.get_deck())
print(y.shuff_deck())      
        