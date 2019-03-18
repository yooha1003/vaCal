#!/usr/bin/env python

# this script is for calculation of visual angle
# example vaCal.py 2.5 70
# written by Uksu, Choi (uschoi@nict.go.jp)

import sys
from math import exp, expm1
import math
from decimal import *
# getcontext().prec = 2

size = float(sys.argv[1])
dist = float(sys.argv[2])

visual_angle_rad = math.atan2(size,dist)
visual_angle_degree = visual_angle_rad*(180/math.pi)


print '[Visual Angle] =',"{0:.2f}".format(visual_angle_degree), 'degree'
