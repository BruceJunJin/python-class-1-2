from numpy import *
from time import *
t0=time()
S0=100
K=105
T=1.0
r=0.05
sigma=0.2
I=250000
z=random.standard_normal(I)
ST=S0*exp((r-0.5*sigma**2)*T+sigma*sqrt(T)*z)
hT=maximum(ST-K,0)
CO=exp(-r*T)*sum(hT)/I
typz=time()-t0
print("Option price is %5.3f" % CO)
print("Finished in %5.3f second" % typz)