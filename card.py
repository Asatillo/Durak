class Card():
    
    def __init__(self, _type, value):
        self.type = _type
        self.value = value

    def get_name(self):
        return f'% of %', self.value, self.type 