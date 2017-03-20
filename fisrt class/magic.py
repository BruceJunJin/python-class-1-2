loops=25000000
from math import *
a=range(1,loops)
def f(x):
	return 3*log(x)+cos(x)**2 
%timeit r=[f(x) for x in a]

import numpy as np
a=np.arange(1,loops)
%timeit r=3*np.log(a)+np.cos(a)**2 
