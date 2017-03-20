# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#bsm_functions.py

# value function
def bsm_call_value(S0,K,T,r,sigma):
    '''Valuation of European call option in BSM model.
    Analytical formula.
    
    Parametres
    ==========
    S0:float
       initial stock/index level
    K:float
      strike price
    T:float
      maturity date
    t:float
      constant risk-free rate
    sigma:float
          volatility factor in diffusion term
          
    Returns
    =======
    Value:float
          present value of the European call option
    '''
    from math import log, sqrt, exp
    from scipy import stats
    S0=float(S0)
    d1=(log(S0/K)+(r+0.5*sigma**2)*T/(sigma*sqrt(T)))
    d2=(log(S0/K)+(r-0.5*sigma**2)*T/(sigma*sqrt(T)))
    value=(S0*stats.norm.cdf(d1,0.0,1.0)-K*exp(-r*T)*stats.norm.cdf(d2,0.0,1.0))
    # stats.norm.cdf--->cumulative distribution function for normal dis
    return value

# vega function
def bsm_vega(S0,K,T,r,sigma):
    '''Vega of European call option in BSM model.
    
    Parametres
    ==========
    S0:float
       initial stock/index level
    K:float
      strike price
    T:float
      maturity date
    r:float
      constant risk-free rate
    sigma:float
          volatility factor in diffusion term
          
    Returns
    =======
    vega:float
        partial derivation of BSM fomular with respect
    '''
    from math import log, sqrt
    from scipy import stats
    S0=float(S0)
    d1=(log(S0/K)+(r+0.5*sigma**2)*T/(sigma*sqrt(T)))
    vega=S0*stats.norm.cdf(d1,0.0,1.0)*sqrt(T)
    return vega
    
#Implied volatility function
def bsm_call_imp_vol(S0,K,T,r,C0,sigma_est,it=100):
    '''Implied volatility of European call option in BSM model.
    
    Parametres
    ==========
    S0:float
       initial stock/index level
    K:float
      strike price
    T:float
      maturity date
    r:float
      constant risk-free rate
    sigma_est:float
          estimate of impl.volatility
    it:integer
    number of iteration  
    
    Returns
    =======
    sigma_est:float
        numerically estimated implied volatility
    '''
    for i in range(it):
        sigma_est -=((bsm_call_value(S0,K,T,r,sigma_est)-C0)/bsm_vega(S0,K,T,r,sigma_est))
        return sigma_est
    
#usage
print(bsm_call_imp_vol(100,105,300,0.05,101,2,it=100))
    
    
    
    