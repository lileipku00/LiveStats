#!/usr/bin/env python

from array import array
from math import fabs
import random, sys

class MovingMedian:
    median = 0.0
    __index = sys.maxint

    def add(self, item):
        if(abs(item - self.median) < self.__index):
            if(abs(item - self.median) != 0):
                self.__index = abs(item - self.median)

        if(item > self.median):
            self.median += self.__index
        else:
            self.median -= self.__index

        return self.__index

def output(data, estimate, stype):
    data.sort()
    med = data[len(data)/2]
    pe = 100.0 * (fabs(estimate - med)/med)
    avg = sum(data) / len(data)

    print "{0}: Estimated: {1}, Actual: {2}, Avg: {3}, %Error {4}".format(stype, estimate, med, avg, pe)

def bimodal( low1, high1, mode1, low2, high2, mode2 ):
    toss = random.choice( (1, 2) )
    if toss == 1:
        return random.triangular( low1, high1, mode1 ) 
    else:
        return random.triangular( low2, high2, mode2 )


if __name__ == '__main__':
    count = int(sys.argv[1])
    random.seed()
    median = MovingMedian()

    x = [i for i in range(count)]
    random.shuffle(x)
    for i in x:
        median.add(i)

    output(x, median.median, "Uniform")

    median = MovingMedian()
    for i in range(count):
        x[i] = random.expovariate(1.0/435)
        median.add(x[i])

    output(x, median.median, "Random")

    median = MovingMedian()
    for i in range(count):
        x[i] = random.triangular(-1000, 1000, 999)
        median.add(x[i])

    output(x, median.median, "Triangular")

    median = MovingMedian()
    for i in range(count):
        x[i] = bimodal(0, 1000, 500, 500, 1500, 1400)
        median.add(x[i])

    output(x, median.median, "Bimodal")



