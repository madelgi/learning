import thinkstats
import survey
import Pmf
import operator
import relay
import Cdf
import myplot
from math import sqrt

"""
Exercise 3.1:

    Build a PMF of the data (see pg. 26) and compute the mean.
"""
class_size_list = [7]*8 + [12]*8 + [17]*14 + [22]*4 + [27]*6 + [32]*12 + [37]*8 + [42]*3 + [47]*2
class_size = Pmf.MakePmfFromList(class_size_list)

def student_pmf(pmf):
    new_pmf = pmf.Copy()

    for bucket, prob in pmf.Items():
        new_pmf.Mult(bucket, bucket)

    new_pmf.Normalize()
    return new_pmf

"""
Exercise 3.3

    Write a version of ``Percentile`` that uses the percentiole rank to compute the
    index of the corresponding percentile.
"""
def PercentileRank(scores, my_score):
    count = 0
    for score in scores:
        if score <= my_score:
            count += 1

    return 100.0*count / len(scores)

def Percentile(scores, percentile_rank):
    scores.sort()
    index = (percentile_rank/100.0) * len(scores) - 1
    return scores[int(index)]

"""
Exercise 3.5

    Download ``Cdf.py`` and ``relay.py`` and generate a plot that shows the
    CDF of running speeds.
"""
def compare_plots():
    pmf = relay.ex_helper()
    myplot.Pmf(pmf)
    myplot.Show(title='PMF of running speed',
               xlabel='speed (mph)',
               ylabel='probability')

    cdf = Cdf.MakeCdfFromPmf(pmf)
    myplot.Cdf(cdf)
    myplot.Show(title='Cdf of running speed',
               xlabel='speed (mph)',
               ylabel='cumulative probability')

"""
Exercise 3.6

    Using the pooled data, compute the distribution of birth weights and use it to find
    your percentile rank. If you were a first baby, find your percentile rank in the
    distribution for first babies. Other use the distribution for others.
"""
def WeightHelper(first=False):
    """ Creates a list of bb weights using the data in whatever the name
    of that file is.
    """
    table = survey.Pregnancies()
    table.ReadRecords()

    results = []

    for record in table.records:
        if getattr(record, 'outcome') == 1:
            if first and getattr(record, 'birthord') == 1:
                results.append(getattr(record, 'birthwgt_lb'))
            if (not first) and getattr(record, 'birthord') > 1:
                results.append(getattr(record, 'birthwgt_lb'))

#    weight_cdf = Cdf.MakeCdfFromList(results)
    return results

"""
Exercise 3.9

    Write a function called ``Sample``, that takes a Cdf and an integer, and returns
    a list of n values chosen at random
"""
import random

def Sample(cdf, n):
    results = []

    for i in xrange(n):
        results.append(sample_help(cdf))

    return results

def sample_help(cdf):
    bound = random.random()

    for val, prob in cdf.Items():
        if bound < prob:
            break
        bound -= prob

    return val

"""
Exercise 3.10

    Generate 1000 numbers from random.random and plot their PMF and CDF. Are
    they uniform?
"""
def rand_plots():
    vals = []

    for i in xrange(1000):
        vals.append(random.random())

    pmf = Pmf.MakePmfFromList(vals)
    myplot.Pmf(pmf)
    myplot.Show(title='PMF of rand vals',
               xlabel='speed (mph)',
               ylabel='probability')

    cdf = Cdf.MakeCdfFromPmf(pmf)
    myplot.Cdf(cdf)
    myplot.Show(title='Cdf of rand vals',
               xlabel='speed (mph)',
               ylabel='cumulative probability')


if __name__ == '__main__':
    # Exercise 3.1
    print class_size.Mean()
    print student_pmf(class_size).Mean()

    # Exercise 3.3
    scores = [77, 63, 21, 45, 89]
    rank = PercentileRank(scores, 77)
    print Percentile(scores, 99)

    # Exercise 3.5 (commented out cuz plots)
    # compare_plots()

    # Exercise 3.6
    print PercentileRank(WeightHelper(False), 6)

    # Exercise 3.9
    weight_cdf = Cdf.MakeCdfFromList(WeightHelper())
    print Sample(weight_cdf, 10000)

    # Exercise 3.10
    rand_plots()
