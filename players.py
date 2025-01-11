class Player():
    def __init__(self, name, handsize, deck):
        self.name = name
        self.__handsize = handsize
        self.cards = {}
        self.knowledge = {}
        self.__init_cards(deck)

    def __init_cards(self, deck):
        for i in range(self.__handsize):
            self.draw_card(deck, i)

    def draw_card(self, deck, id):
        if len(deck) == 0:
            self.cards[id] = None
            new_knowledge = {"color":None, "value":None}
        else:
            self.cards[id] = deck.pop()
            new_knowledge = {"color":"u", "value":"u"}
        self.knowledge[id] = new_knowledge
    
    def give_hint(self, player, hint):
        #print ("gave hint: ", hint)
        if isinstance(hint, int):#value
            pos = 1
            typ = "value"
        elif isinstance(hint, str):#color
            hint = hint.title()
            pos = 0
            typ = "color"
        else:
            raise Exception(f"Hint must be a string or integer, is {type(hint)}")

        for key in player.cards:
            if hint == player.cards[key][pos]:
                player.knowledge[key][typ] = hint

    def discard(self, pos, deck, discard):
        discard.append(self.cards[pos])
        self.draw_card(deck, pos)
    
    def __repr__(self):
        cards = []
        for key in self.cards:
            new_entry = f"{self.cards[key][0]}({self.knowledge[key]['color']}) {self.cards[key][1]}({self.knowledge[key]['value']})"
            cards.append(new_entry)
        return f"{self.name} has these cards: {cards}"

            



        
        