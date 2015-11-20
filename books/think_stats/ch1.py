import survey

"""
Exercise 1.3

    In this exercise, we will explore the data in the Pregnancies
    table

"""
def ex13():
    table = survey.Pregnancies()
    table.ReadRecords()
    print 'Number of pregnancies', len(table.records)

# Part 2 of ex13. This function iterates through Pregnancies and counts
# the numbe of live births.
def loop_table():
    table = survey.Pregnancies()
    table.ReadRecords()
    live_births = 0

    for record in table.records:
        if getattr(record, 'outcome') == 1:
            live_births += 1

    print live_births

# Part 3 of ex1.3. This is similar to part two, except now we divide the
# the live births into two groups: first born child, and other.
def loop_table_groups():
    table = survey.Pregnancies()
    table.ReadRecords()
    live_births_first = 0
    live_births_other = 0

    for record in table.records:
        if getattr(record, 'outcome') == 1:
            if getattr(record, 'birthord') == 1:
                live_births_first += 1
            else:
                live_births_other += 1

    return live_births_first, live_births_other

# Part 4 of ex1.3. Now, we compute the average pregnancy length for babies
# in each of the two groups
def pregnancy_lengths():
    table = survey.Pregnancies()
    table.ReadRecords()

    live_births_first = 0
    first_length = 0
    live_births_other = 0
    other_length = 0

    for record in table.records:
        if getattr(record, 'outcome') == 1:
            if getattr(record, 'birthord') == 1:
                first_length += getattr(record, 'prglength')
                live_births_first += 1
            else:
                other_length += getattr(record, 'prglength')
                live_births_other += 1

    avg_first = float(first_length)/live_births_first
    avg_other = float(other_length)/live_births_other

    return avg_first, avg_other

if __name__ == '__main__':
    print pregnancy_lengths()
