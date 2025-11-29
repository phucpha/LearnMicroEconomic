import numpy as np
R= np.arange(0, 1, 0.01)

def R_Plus_1(R):
    return 1+R

def R_Plus_1_Exp(R, exp):
    return R_Plus_1(R)**exp

nNumberOfYear = 10
R = 16.2/100
payPerYear = 100
bondPrice = 1000

def Price(nYear, R, payPerYear, bondPrice):
    PriceAccumulate = 0
    for year in range(1,nYear+1):
        PriceAccumulate = PriceAccumulate + payPerYear/(R_Plus_1_Exp(R,year))
    PriceAccumulate = PriceAccumulate + bondPrice/R_Plus_1_Exp(R,nYear)
    return PriceAccumulate
    
Price = Price(nNumberOfYear, R, payPerYear, bondPrice)

print(Price)