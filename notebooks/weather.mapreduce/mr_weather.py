#!/usr/bin/python
"""
count the number of measurements of each type
"""
import sys
sys.path.append('/usr/lib/python2.6/dist-packages')
from mrjob.job import MRJob
import re
from sys import stderr

WORD_RE = re.compile(r"[\w']+")

#logfile=open('log','w')
#logfile=stderr

class MRWeather(MRJob):

    def my_mapper(self, _, line):
        try:
            self.increment_counter('MrJob Counters','my_mapper',1)
            elements=line.split(',')
            #logfile.write('%s\n' % type(line))
            if elements[1]=='TMAX' or elements[1]=='TMIN':
                measure = 1
                key = (elements[0],elements[2])
            else:
                key = ('NA','NA')
                measure = 0
            n_days = sum([e!='' for e in elements[3:]])

        except Exception, e:
            stderr.write('Error in line:\n'+line)
            stderr.write(e)
            self.increment_counter('MrJob Counters','mapper-error',1)
            key = ('error','error')
            measure = 0
            n_days = 0

        finally:
            yield key, (measure, n_days)

            
    def my_combiner(self, word, counts):
        self.increment_counter('MrJob Counters','my_combiner',1)
        sum1=0
        sum2=0
        for measure, n_days in counts:
            sum1 = sum1 + measure
            sum2 = sum2 + n_days
        yield word, (sum1,sum2)

    def my_reducer1(self, word, counts):
        self.increment_counter('MrJob Counters','my_reducer1',1)
        sum1 = 0
        sum2 = 0
        for measure, n_days in counts:
            sum1 = sum1 + measure
            sum2 = sum2 + n_days
        if sum1 ==2:
            yield word[0], (word[1], sum2)
        else:
            yield ('NA'), ('NA', 0)
    def my_reducer2(self, word, counts):
        self.increment_counter('MrJob Counters','my_reducer2',1)
        n_year = 0
        for year, n_days in counts:
            if n_days>0:
                n_year= n_year+1
        if n_year == 0:
            yield 'NA', 0
        else:
            yield word, n_year
            
    def steps(self):
        return [self.mr(mapper=self.my_mapper, combiner=self.my_combiner, reducer = self.my_reducer1),
                self.mr(reducer=self.my_reducer2)]

if __name__ == '__main__':
    MRWeather.run()