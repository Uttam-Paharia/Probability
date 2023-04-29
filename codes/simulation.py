
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
simlen=10000
#number of bulbs
n =  5

#Probability of bulb to fuse  
p = 0.05

experiment=np.zeros(4)
acctual=np.zeros(4)
data_binom = binom.rvs(n,p,size=simlen)  #Simulating the event of jumping 10 hurdles
defects,stimulation = np.unique(data_binom , return_counts= True)
while np.size(defects) < 6:
    defects = np.append(defects , defects[np.size(defects) -1] + 1)
while np.size(stimulation) < 6:
    stimulation = np.append(stimulation , 0)
stimulation = np.cumsum(stimulation)/simlen

experiment[0]=stimulation[0] 
experiment[1]=stimulation[1]
experiment[2]=stimulation[5]-stimulation[1]
experiment[3]=stimulation[5]-stimulation[0]
acctual[0]=binom.cdf(0,n,p) 
acctual[1]=binom.cdf(1,n,p)
acctual[2]=binom.cdf(5,n,p)-binom.cdf(1,n,p)
acctual[3]=binom.cdf(5,n,p)-binom.cdf(0,n,p)
for i in range(4):
    print("For experiment "+str(i+1)+" stimulation value is "+str(experiment[i])+" and acctual value is "+str(acctual[i]))
