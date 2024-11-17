import random

def random_integer(min, max, seed):
    random.seed(seed)
    return random.randint(int(min), int(max))