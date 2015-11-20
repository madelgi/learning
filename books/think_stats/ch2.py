import thinkstats
import survey
import Pmf
import operator
from math import sqrt

pweights = [1, 1, 1, 3, 3, 3, 591]

"""
Exercise 2.1:

    Calculate the mean, variance, and standard deviation of the pumpkins'
    weights.
"""
def Pumpkin(weights):
    m = thinkstats.Mean(weights)
    v = thinkstats.Var(weights)
    sd = sqrt(float(v))

    return (m, v, sd)

"""
Exercise 2.2:

    Reusing code from `survey.py` and `first.py`, compute the standard-deviation
    of gestation time for first babies and others. Does it look like the spread
    is the same for the two groups?
"""
def bb_gestation_sdev():
    table = survey.Pregnancies()
    table.ReadRecords()

    first_bbs = []
    other_bbs = []

    for record in table.records:
        if getattr(record, 'outcome') == 1:
            if getattr(record, 'birthord') == 1:
                first_bbs.append(getattr(record, 'prglength'))
            else:
                other_bbs.append(getattr(record, 'prglength'))

    first_sdev = sqrt(float(thinkstats.Var(first_bbs)))
    other_sdev = sqrt(float(thinkstats.Var(other_bbs)))

    return first_sdev, other_sdev

"""
Exercise 2.3:

    Write a function called Mode that takes a Hist object and returns
    the most frequent value.
"""
def Mode(hist):
    vals = hist.Values()
    mode = vals[0]
    freq = hist.Freq(vals[0])

    for val in vals[1:]:
        test = hist.Freq(val)

        if test > freq:
            freq = test
            mode = val

    return mode

def AllModes(hist):
    vals = hist.Values()
    freqs = [hist.Freq(vals[i]) for i in range(0, len(vals))]

    ziplist = zip(vals,freqs)

    ziplist.sort(key=lambda x: x[1])
    return ziplist

"""
Exercise 2.4:

    Write a function called RemainingLifetime that takes a Pmf of lifetimes
    and an age, and returns a new Pmf that represents the distribution of
    remaining lifetimes.
"""
def RemainingLifetime(lifetimes, age):
    i = 0

    while i <= age:
        lifetimes.Mult(i, 0)
        i += 1

    lifetimes.Normalize()
    return lifetimes

"""
Exercise 2.5:

    Write functions `PmfMean` and `PmfVar` that take a Pmf object and compute
    the mean and variance.
"""
def PmfMean(pmf):
    mean = 0

    for i in pmf.Values():
        mean += i*pmf.Prob(i)

    return mean

def PmfVar(pmf):
    var = 0
    mu = PmfMean(pmf)

    for i in pmf.Values():
        var += pmf.Prob(i)*(i - mu)**2

    return var

"""
Exercise 2.6:

    Write functions `ProbEarly`, `ProbOnTime`, and `ProbLate` that take a PMF and
    compute the fraction of births that fall into each bin.

    prglength
"""
def ProbEarly(pmf):
    """ Compute the probability of a child being born early. Assumes
    the input is a pmf of pregnancy lengths
    """
    prob = 0
    i = 0

    while i < 38:
        prob += pmf.Prob(i)
        i += 1

    return prob

def ProbOnTime(pmf):
    """ Compute the probability of a child being born on time. Assumes
    the input is a pmf of pregnancy lengths
    """
    prob = 0
    i = 38

    while i < 41:
        prob += pmf.Prob(i)
        i += 1

    return prob

def ProbLate(pmf):
    """ Compute the probability of a child being born late. Assumes
    the input is a pmf of pregnancy lengths
    """
    prob = 0
    i = 41

    while i < 50:
        prob += pmf.Prob(i)
        i += 1

    return prob

def ProbHelper():
    """ Helper function for the above three functions. Creates a pmf of
    pregnancy lengths using the data in whatever the name of that file
    is.
    """
    table = survey.Pregnancies()
    table.ReadRecords()

    preglengths = []
    for record in table.records:
        if getattr(record, 'outcome') == 1:
            preglengths.append(getattr(record, 'prglength'))

    preg_pmf = Pmf.MakePmfFromList(preglengths)
    return preg_pmf

"""
Exercise 2.7

    Write a function that computes the probability that a baby will be born during Week
    x, assuming they have not born prior to week x.
"""
def week_x(pmf, x):
    i = 0

    while i < x:
        pmf.Mult(i, 0)
        i += 1

    pmf.Normalize()
    return pmf.Prob(x)

if __name__ == '__main__':
    # Problem 1
    (m, v, sd) = Pumpkin(pweights)
    print "Mean: %d; Variance: %d; SDev: %d." % (m, v, sd)

    # Problem 2
    (first, others) = bb_gestation_sdev();
    print "First babies: %f, other babies: %f" % (first, others)

    # Problem 3
    hist = Pmf.MakeHistFromList([1,2,2,2,3,3,10,10,10,10,10,11])
    print Mode(hist)
    print AllModes(hist)

    # Problem 4
    age_pmf = Pmf.MakePmfFromList([1,2,3,3,4,4,4,5,5,5,5,5,5,5,6,6,7,7,7,8,8,9,10])
    print age_pmf.Prob(5)
    print age_pmf.Prob(8)
    print age_pmf.Prob(10)

    new_pmf = RemainingLifetime(age_pmf, 4)

    print new_pmf.Prob(5)
    print new_pmf.Prob(8)
    print new_pmf.Prob(10)

    # Problem 5
    pmf = Pmf.MakePmfFromList([1,2,2,3,5])
    print PmfMean(pmf)
    print pmf.Mean()
    print PmfVar(pmf)
    print pmf.Var()

    # Problem 6
    preg_pmf = ProbHelper()
    print ProbEarly(preg_pmf)
    print ProbOnTime(preg_pmf)
    print ProbLate(preg_pmf)

    # Problem 7
    print week_x(preg_pmf, 39)
