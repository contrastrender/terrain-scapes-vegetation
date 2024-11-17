import random

def random_color(use_alpha, fixed_alpha, seed):
    random.seed(seed)
    if use_alpha:
        return (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), fixed_alpha if fixed_alpha != None else random.uniform(0, 1))
    else:
        return (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))