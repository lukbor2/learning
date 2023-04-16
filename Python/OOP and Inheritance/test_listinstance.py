from listinstance import ListInstance

class Spam(ListInstance):
    def __init__(self):
        self.data1 = 'food'

x = Spam()
print(x)