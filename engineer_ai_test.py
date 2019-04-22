from random import randint
from time import sleep

import requests

SENTENCE = "Virtue signalling is society's version of Proof of Stake"

def case_one(SENTENCE):
    for w in SENTENCE.split():
        while True:
            response = requests.get('https://www.amazon.com/s?k={}&ref=nb_sb_noss'.format(w))
            if w in response.content.decode():
                print('{} found'.format(w))
                break
            else:
                print('{} not found'.format(w))
            sleep(randint(1, 4))


if __name__ == '__main__':
    case_one(SENTENCE)