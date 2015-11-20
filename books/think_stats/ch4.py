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
Exercise 4.1:

    Use `expovariate` to generate 44 values from an exponential distribution with mean
    32.6. Plot the CCDF on a log-y scale and compare it to figure 4.3.
"""
def expo_test():
    i = 0
    vals = []

    while i < 44:
        vals.append(random.expovariate(1/32.6))
        i += 1

    new_cdf = Cdf.MakeCdfFromList(vals)
    myplot.Cdf(new_cdf, complement=True, xscale='linear', yscale='log')
    myplot.Show()

"""
Exercise 4.3:

    Write a wrapper function that takes a paremeter for alpha and x_m and generates a
    value from the corresponding pareto distribution. Use this function to generate a
    sample from a Pareto distribution, compute the CCDF, and plot it on a log-log scale.
"""
def pareto_wrapper(alpha, xmin):
    return xmin * random.paretovariate(alpha)

def pareto_test():
    i = 0
    vals = []

    while i < 100:
        vals.append(pareto_wrapper(1,0.5))
        i += 1

    new_cdf = Cdf.MakeCdfFromList(vals)
    myplot.Cdf(new_cdf, complement=True, xscale='log', yscale='log')
    myplot.Show()

"""
Exercise 4.4:

    Generate 6 million values from a distribution w/ alpha = 1.7 and x_m = 100 cm.
    What is the mean?
"""
def pareto_height():
    i = 0
    vals = []

    while i < 6000000:
        vals.append(pareto_wrapper(1.7,100))
        i += 1
        print i

    new_cdf = Cdf.MakeCdfFromList(vals)
    print new_cdf.Mean()

"""
Exercise 4.5:

    Zipf's law predicts that in a body of text ('corpus'), the distribution of word
    frequencies is roughly Pareto.
"""
# def parse_text():
#     poe = open('data/poe.html', 'r')
#     tree = html.fromstring(poe)

"""
Exercise 4.7

    Use erf.NormalCdf to investigate the frequency of rare events in a normal distribution.
    What fraction of the population has an IQ greater than the mean? What fraction is over
    115, 130, or 145?
"""
def normal_test():
    percentiles = {}
    percentiles['115'] = 1-erf.NormalCdf(115,100,15)
    percentiles['130'] = 1-erf.NormalCdf(130,100,15)
    percentiles['145'] = 1-erf.NormalCdf(145,100,15)

    percentiles['190'] = 6000000000*(1 - erf.NormalCdf(190,100,15))

    return percentiles

"""
Exercise 4.8

    Plot the CDF of pregnancy lengths for all live births. Does it look like
    a normal distribution?

"""
def preggo_cdf():
    pass

"""
Exercise 4.9

    Write a function called Sample that generates 6 samples from a normal
    distribution with mu = 0 and sigma = 1. Sort and return the values. Write
    a function called samples that calls sample 1000 times and returns a list of
    lists. apply zip to this list of lists, compute the mean of each resulting list.
"""
def sample(n=6):
    vals = []

    for i in xrange(0,n):
        vals.append(np.random.normal(0,1))

    return sorted(vals)

def samples(n=6, m=1000):

    return [sample(n) for i in range(m)]

def final():
    lists = zip(*samples())
    return map(lambda s: np.mean(s), lists)

"""
Exercise 4.10:

    Write  a function called ``NormalPlot`` that takes a sequence of values and
    generates a normal probability plot. Use the running speeds (from ``relay.py``)
    to generate a normal probability plot. Is the normal distribution a good model
    for this data?
"""
def NormalPlot(vals):
    size = len(vals)
    rand_vals = [np.random.normal(0,1) for i in xrange(size)]

    # clear current figure
    plt.clf()
    # plot graph
    plt.plot(sorted(vals), sorted(rand_vals), 'b.', markersize=3)
    plt.show()

def check_speeds():
    NormalPlot(relay.GetSpeeds(relay.ReadResults()))

"""
Exercise 4.11

    Write a program that reads adult weights from the BRFSS and generates
    normal probability plots for w and log w.
"""
def LogNormalPlot(vals):
    size = len(vals)
    rand_vals = [np.random.lognormal(0,1) for i in xrange(size)]

    # clear current figure
    plt.clf()
    # plot graph
    plt.plot(sorted(vals), sorted(rand_vals), 'b.', markersize=3)
    plt.show()


def brfss_prob():
    table = brfss.Respondents()
    table.ReadRecords()

    weights = []

    for record in table.records:
        weight = getattr(record, 'weight2')

        if weight != 'NA':
            weights.append(weight)

    NormalPlot(weights)
    LogNormalPlot(weights)

"""
Exercise 4.14:

    Write a function named ``weibullvariate`` that takes lam and k and
    returns a random value from the Weibull distribution with those
    parameters
"""
def weibullvariate(lam,k):
    p = random.random()
    x = lam * (-math.log(1-p))**(1/k)

    return x

def main():
    # Exercise 4.1
    # expo_test()

    # Exercise 4.3
    # pareto_test()

    # Exercise 4.4
    # pareto_height()

    # Exercise 4.5
    # parse_text()

    # Exercise 4.7
    # print normal_test()

    # Exercise 4.9
    #print final()

    # Exercise 4.10
    check_speeds()

if __name__ == '__main__':
    main()
