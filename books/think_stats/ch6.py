import survey
import csv
import random
from math import e
import erf
import Pmf

"""
Exercise 6.1:

    Write a function named `Skewness` that computes g_1 for a
    sample

"""
def extract_preglength():
    table = survey.Pregnancies()
    table.ReadRecords()

    preglengths = []

    for record in table.records:
        if getattr(record, 'outcome') == 1:
            preglengths.append(getattr(record, 'prglength'))

    return preglengths

def skewness(vals):
    """Take a list of vals and compute the skew"""
    mean = sum(vals)/float(len(vals))
    m2 = 0
    m3 = 0

    for i in xrange(len(vals)):
        m2 += (vals[i] - mean)**2
        m3 += (vals[i] - mean)**3

    m2 *= 1/float(len(vals))
    m3 *= 1/float(len(vals))

    return (m3/(m2**(3/2.0)))

def main():
    # Exercise 6.1
    print skewness(extract_preglength())

"""
Exercise 6.3:

    Compute the median, mean, skewness, and Pearson's skewness of the income
    data. TODO

"""
def extract_income():
    with open('08in11si.csv') as cfile:
        incomes = csv.reader(cfile)
        for row in incomes:
            print row

"""
Exercise 6.4

    Write a definition for a class that represents a random variable with a
    Gumbel distribution. TODO

"""
class RandomVariable(object):
    """Parent class for all random variables."""

class Gumbel(RandomVariable):

    def __init__(self, mu, beta):
        self.mu = float(mu)
        self.beta = float(beta)
        self.exp = Exponential(1/self.beta)

    def cdf(self, val):
        exp = -(val - self.mu)/self.beta
        return e**(-(e**val))

    def generate(self):
        const = e**(self.mu/self.beta)
        return e**(-const/self.exp.generate())

class Exponential(RandomVariable):

    def __init__(self, lam):
        self.lam = lam

    def generate(self):
        return random.expovariate(self.lam)

"""
Exercise 6.6

    In order to join Blue Man Group, you have to be male between 5'10" and
    6'1". What percentage of the U.S. male population is in this range?

Answer:

    Distribution of heights (for men) is roughly normal, w/ mean 178 cm
    and variance 59.4 cm.
"""
def blue_men(min_height=177.8, max_height=185.42, mu=178, sigma=7.707):
    return (erf.NormalCdf(max_height, mu, sigma)
                - erf.NormalCdf(min_height, mu, sigma))


"""
Exercise 6.9

    Write a function that takes PMF_X and PMF_Y and returns PMF_{X+Y}
"""
def pmf_sum(pmfx, pmfy):
    sum_pmf = []
    for x in pmfx.Values():
        for y in pmfy.Values():
            sum_pmf.append(x+y)

    return Pmf.MakePmfFromList(sum_pmf)

def pmf_max(pmfx, pmfy):
    max_pmf = []
    for x in pmfx.Values():
        for y in pmfy.Values():
            sum_pmf.append(max(x,y))

    return Pmf.MakePmfFromList(sum_pmf)

"""
Exercise 6.15

    Write a function called MakePmfFromCdf that takes a Cdf object and returns
    a Pmf
"""

if __name__ == '__main__':
    main()
