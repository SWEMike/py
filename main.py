__author__ = 'michael'


def mean(*values, dec=2):
    tmp = 0
    for v in values:
        tmp += v
    return round(tmp / len(values), dec)

print("Mean:", mean(20, 23, 23, 29, dec=1))