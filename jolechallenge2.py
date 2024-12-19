import random as ____
__ = ["bang","fri","Juletrærne","Angel","Holiday wreath", "Joyful celebration"]

def _(_):
    ____.seed(_)
    return chr(int((1+(____.randint(1,28)-5)/(2*2*(5**2)))*1e02))

print("".join([_(x) for x in __]))

