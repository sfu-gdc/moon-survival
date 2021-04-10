from random import randint

def randint_around(pivot, radius):
    return randint(pivot-radius, pivot+radius+1)