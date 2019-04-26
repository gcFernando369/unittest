# Fernando González Colín  #
# Ciudad de México, México #
# gc.fernando.96@gmail.com #
# April, 2019              #
# Simple sample functions  #

import numpy as np

def factorial(n):
    """
    what is the factorial of n?
    """
    res=1
    for x in range(n,0,-1): res*=x
    return res

def isPowerOf(n,x):
    """
    is n power of x?
    """
    res=(np.log(n)/np.log(x))%1
    return res==0

def addDigitsUntilOne(n):
    """
    For example given number is 59, the result will be 5.
    Step 1: 5 + 9 = 14
    Step 1: 1 + 4 = 5
    """
    if n<10: return n
    _next=0
    for ch in str(n): _next+=int(ch)
    return addDigitsUntilOne(_next)

def isASimpleProgression(nums):
    """
    The sequence 2, 6, 18, 54, ... is a geometric progression with common ratio 3. 
    Similarly, 10, 5, 2.5, 1.25, ... is a geometric sequence with common ratio 1/2.
    """
    differences=[]
    for i in range(len(nums)-1): differences.append(nums[i]-nums[i+1])
    if len(set(differences))==1: return True
    return False

def traveledDistance(travel):
    """
    A robot moves in a plane starting from the original point (0,0). 
    The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
    The trace of robot movement is shown as the following:
    UP 5
    DOWN 3
    LEFT 3
    RIGHT 2
    And the traveled distance is 2.236 [u]
    """
    pos=[0,0]
    fac={'UP':[1,1],'DOWN':[1,-1],'RIGHT':[0,1],'LEFT':[0,-1]}
    for step in travel:
        d,l=step.split()
        f=fac[d]
        pos[f[0]]+=int(l)*f[1]
    return np.around(np.linalg.norm(pos),decimals=3)
