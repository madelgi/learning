import survey
import random
"""
Exercise 7.1:

    In the NSFG dataset, the difference in mean weight for first births is 2.0
    ounces. Compute the p-value of this difference

"""
def weight_p_value():
    p_value = 0

    i = 0
    while i < 100:
        if i % 10 == 0: print i

        if abs(get_diff_means()) > 2.0:
            p_value += 1

        i += 1

    p_value = p_value / float(1000)
    return p_value

def get_diff_means():
    table = survey.Pregnancies()
    table.ReadRecords()
    firsts = []
    others = []

    i = 0
    while i < 4413:
        rc = random.choice(table.records)

        if getattr(rc, 'outcome') == 1 and getattr(rc, 'birthwgt_oz') != 'NA':
            firsts.append(getattr(rc, 'birthwgt_oz'))
            i += 1

    j = 0
    while j < 4735:
        rc = random.choice(table.records)

        if getattr(rc, 'outcome') == 1 and getattr(rc, 'birthwgt_oz') != 'NA':
            others.append(getattr(rc, 'birthwgt_oz'))
            j += 1

    return (mean(firsts) - mean(others))

def mean(vals):
    return (sum(vals) / float(len(vals)))

"""
Exercise 7.3:

    Using the data from the NSFG, what is the posterior probability that the
    distribution of birth weights is different for first babies and others?

"""

if __name__ == '__main__':
    # Exercise 7.1
    print weight_p_value()
