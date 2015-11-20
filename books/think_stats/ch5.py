import random
import matplotlib.pyplot as plt
import numpy as np
import Cdf
import myplot
import erf
import numpy as np
import relay
import brfss
import math

"""
Exercise 5.4

    Write a program that simulates the Monty Hall problem and use it to
    estimate the probability of winning if you stick and if you switch.
"""
def monty_hall_stick():
    answer = random.randint(1,3)
    guess = random.randint(1,3)

    return answer == guess

def monty_hall_switch():
    answer = random.randint(1,3)
    guess = random.randint(1,3)

    # choose what to reveal
    options = [1,2,3]
    options.remove(answer)

    if guess in options:
        options.remove(guess)

    reveal = random.choice(options)

    # switch answer to the other door
    final_guess = [1,2,3]

    final_guess.remove(reveal)
    final_guess.remove(guess)

    return final_guess[0] == answer


def run_monty_simulation(n=1000):
    i = 0
    switch_total = 0
    stick_total = 0

    while i < n:
        if monty_hall_stick():
            stick_total += 1

        if monty_hall_switch():
            switch_total += 1

        i += 1

    return (switch_total, stick_total)
