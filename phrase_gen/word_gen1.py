import random


def today_phrase() -> str:
    """

    :rtype: returns random phrase for header 
    """
    with open('phrase_gen/science_words1.txt', "r") as data1:
        scifi = [word.replace("\n", "") for word in data1]

    with open('phrase_gen/adjectives.txt', "r") as data2:
        adj = [word.replace("\n", "") for word in data2]

    one = random.sample(range(0, len(scifi)), len(scifi))
    two = random.sample(range(0, len(adj)), len(scifi))

    candidates = set()
    for iteration in range(20):
        for idx in zip(one, two):
            candidates.add(str(adj[idx[-1]]) + " " + str(scifi[idx[0]]))

    chosen_phrase = random.choice(list(candidates))

    return chosen_phrase
