#!/usr/bin/env python

# this script is for calculation of visual angle
# example vaCal.py 2.5 70
# written by Uksu, Choi (uschoi@nict.go.jp)

import sys
from math import exp, expm1
import math
from decimal import *
import argparse
# getcontext().prec = 2

## help
parser = argparse.ArgumentParser()
parser.add_argument("val1", help="Width (cm)",type=float)
parser.add_argument("val2", help="Height (cm)",type=float)
parser.add_argument('--version', action='version', version='Version 0.1')
print parser.parse_args()

## run the script
size = float(sys.argv[1])
dist = float(sys.argv[2])

visual_angle_rad = math.atan2(size,dist)
visual_angle_degree = visual_angle_rad*(180/math.pi)


print '[Visual Angle] =',"{0:.2f}".format(visual_angle_degree), 'degree'
