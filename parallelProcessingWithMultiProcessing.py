import collections
import time
from pprint import pprint
Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])
Scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='math', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='physics', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='chemistry', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

pprint(Scientists)

def transform(x):
    print("processing happening for "+x.name)
    time.sleep(1)
    result = {'name':x.name,'age':2020-x.born}
    print("processing completed for "+x.name)
    return result

# start = time.time()
# result = tuple(map(transform,Scientists))
# end = time.time()
# print("total time =",end-start)

# pprint(result)

import multiprocessing
pool = multiprocessing.Pool(multiprocessing.cpu_count())

start = time.time()
result = pool.map(transform,Scientists)
pool.close()
pool.join()
end = time.time()
print("total time =",end-start)
pprint(result)