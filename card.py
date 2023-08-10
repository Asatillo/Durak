class Card():
    
    signs = {'hearts': '♥', 'diamonds': '♦', 'spades': '♠', 'club': '♣'}

    def __init__(self, _type: str, value: int, rank: str):
        '''
        _type: str - the type of the card (hearts, diamonds, spades, club)
        value: int - the numeric value of the card (6, 7, 8, 9, 10, 11, 12, 13, 14)
        rank: str - the rank of the card (6, 7, 8, 9, 10, J, Q, K, A)
        '''
        self.type = _type
        self.value = value
        self.rank = rank

    def get_name(self):
        return str(self)
    
    def __str__(self):
        return f'{Card.signs[self.type]}{self.rank} '