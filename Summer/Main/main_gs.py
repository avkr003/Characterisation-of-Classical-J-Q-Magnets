import sys
import math
import threading
sys.path.append('/home/abhinav/Desktop/Academics/Summer/Python')
import numpy as np
import matplotlib.pyplot as plt
import time

from spin_gs import *

kb = 1.0

m = 4
n = 4
p = 1 

if p > 1:
	d = '3d'
elif p == 1:
	d = '2d'

qv = 1.0
jv = [0.0]*3
jv[0] = 0.0

iterations = 10000

spin_gs(jv,qv,iterations,m,n,p,d)