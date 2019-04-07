## Import Packages
import numpy as np
import scipy as sp
import math
from scipy import optimize
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
  
## Calculate 10th order taylor polynomial  
def get10Taylor(x):
  total = 0
  terms = []
  for i in range(0, 10):
    terms.append((x**i)/(np.math.factorial(i)))
    total += terms[i]
  return total

## Graph relative error
def plotDifference(start, finish):
  xlist = []
  ylist = []
  for i in np.linspace(start, finish, 100):
    xlist.append(i)
    value = abs((np.exp(i) - get10Taylor(i))/np.exp(i))
    ylist.append(value)
  plt.plot(xlist, ylist,'ro')
  plt.yscale('log')
  plt.savefig('differenceGraph.png')
  plt.show()

## Graph relative error of corrected taylor series approximation in a given domain from start to finish
## A very fast value is 0.14190910481820962
def plotAccurate(start, finish, divisor):
  xlist = []
  ylist = []
  for i in np.linspace(start, finish, 100):
    xlist.append(i)
    ylist.append(relativeError(i, divisor))
  plt.plot(xlist, ylist,'r.')
  plt.yscale('log')
  plt.savefig('accurateGraph.png')
  plt.show()
  
## Calculates the 10th order taylor series's approximation of e^x with a given x and divisor
def algorithm(x, divisor):
  taylorInterval = get10Taylor(divisor)
  taylorTotal = 0
  divisions = abs(int(math.floor(x / divisor))) ## Finds number of divisions (excluding remainder)
  remainder = (x % divisor)
  if x < 0:
    taylorTotal = (taylorInterval ** divisions)
    taylorTotal /= get10Taylor(remainder)
    taylorTotal = 1 / taylorTotal
  elif x > 0:
    taylorTotal = (taylorInterval ** divisions)
    taylorTotal *= get10Taylor(remainder)
  else:
    taylorTotal = 1
  return taylorTotal
  
## Calculates the relative error between the approximated 10th order taylor series and the actual value of e^x
def relativeError(x, divisor):
  return abs((np.exp(x) - algorithm(x, divisor)))/np.exp(x)
  
## Calculates the largest divisor that yields an acceptable error in a given range
def calculateLargestDivisor(start, finish, minDivisor, maxDivisor):
  largest = minDivisor
  for i in np.linspace(minDivisor, maxDivisor, 99999):
    high = relativeError(100, i);
    if (i > largest and high < (1e-13)):
      largest = i
  print(str(largest))
  
## Graphs a comparison of different dividends
def graphComparison():
  xlist = []
  ylist1 = []
  ylist2 = []
  ylist3 = []
  divisor1 = 0.06
  divisor2 = 0.14190910481820962
  divisor3 = 0.165
  for i in np.linspace(-100, 100, 100):
    xlist.append(i)
    ylist1.append(relativeError(i, divisor1))
    ylist2.append(relativeError(i, divisor2))
    ylist3.append(relativeError(i, divisor3))
  plt.plot(xlist, ylist1,'r.')
  plt.plot(xlist, ylist2,'b.')
  plt.plot(xlist, ylist3,'g.')
  plt.yscale('log')
  plt.savefig('comparisonGraph.png')
  plt.show()

# Extra stuff
def sinAlgorithm(x, divisor):
  return ((algorithm(x, divisor))**1j - (algorithm(-x, divisor)**1j))/2j

def sinRelativeError(x, divisor):
  return abs((np.sin(x) - sinAlgorithm(x, divisor)))/np.sin(x)

def cosAlgorithm(x, divisor):
  return ((algorithm(x, divisor))**1j + (algorithm(-x, divisor)**1j))/2

def cosRelativeError(x, divisor):
  return abs((np.cos(x) - cosAlgorithm(x, divisor)))/np.cos(x)

def sinPlotAccurate(start, finish, divisor):
  xlist = []
  ylist = []
  for i in np.linspace(start, finish, 10000):
    xlist.append(i)
    ylist.append(sinRelativeError(i, divisor))
  plt.plot(xlist, ylist,'r.')
  plt.yscale('log')
  plt.savefig('sinAccurateGraph.png')
  plt.show()

def cosPlotAccurate(start, finish, divisor):
  xlist = []
  ylist = []
  for i in np.linspace(start, finish, 10000):
    xlist.append(i)
    ylist.append(cosRelativeError(i, divisor))
  plt.plot(xlist, ylist,'r.')
  plt.yscale('log')
  plt.savefig('cosAccurateGraph.png')
  plt.show()

plotDifference(-100, 100)