# Little guided workshop on how to alter existing code
# Keywords: electricity, field, vector, charge, force
# Licence:  MIT Licence
# Author:   tbisig@gmail.com

import matplotlib.pyplot as plt
from numpy import minimum
from numpy import absolute
from math import atan2
from math import sqrt
from math import cos
from math import sin
from math import pi
import random

epsilon_0 = 8.854187817*10E-12
scale = 0.5
charge_scale = 10**(-9)

# define the charges
charges = [[0.2,0.2,2.0],[0.7,0.7,-1.0],[0.5,0.3,1.0],[0.1,0.8,1.5],[0.8,0.1,-1.5],[0.4,0.3,2]]

sum_charges = 0
loc_charges = []
for c in charges:
  loc_charges.append([c[0],c[1]])
  sum_charges += absolute(c[2])

max_field = 1/(4*pi*epsilon_0)*sum_charges*charge_scale/(0.5*scale)**2
min_field = 0

def alp(w):
  return minimum(1.0, w/(max_field-min_field))

# this defines the grid of Points Of Interest (poi)
pois = []
for i in range(20):
  for j in range(20):
    t = [i/20.0,j/20.0]
    if t not in loc_charges:
      pois.append(t)
  
def getEFieldComponents(ch,p):

  field_x = 0.0
  field_y = 0.0
  
  # loop over all charges
  for c in ch:
    # calculate electrostatic field at point
    # p from charge 

    ####### -- for the students -- #######
    d_x = p[0]-c[0]
    d_y = p[1]-c[1]
    r = sqrt(d_x**2+d_y**2)
    f = 1/(4*pi*epsilon_0)*c[2]*charge_scale/r**2
    angle = atan2(d_y,d_x)
      
    field_x += f*cos(angle)
    field_y += f*sin(angle)

    ####### ---------------------- #######

    #field_x = max_field*random.random()
    #field_y = max_field*random.random()
  
  return [field_x, field_y]

# setting up the stage
ax = plt.axes()
fig, ax = plt.subplots()

# draw charges
for c in charges:
  if c[2]>=1:
    col = 'r'
  else:
    col = 'b'
  ax.add_artist(plt.Circle((c[0],c[1]), 0.02*sqrt(abs(c[2])), color=col))

# draw arrows
for l in pois:
  # get e-field components for a given location l
  f = getEFieldComponents(charges, l)
  # calculate 'length' of e-field arrow, to calculate relative strength
  abs_val = sqrt(f[0]**2+f[1]**2)
  ax.arrow(l[0], l[1], 0.005*f[0]/abs_val, 0.005*f[1]/abs_val, head_width=0.01, head_length=0.02, fc='k', ec='k', lw=0.02, alpha=alp(abs_val))

# remove axes in plot
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# set the plotting area to 'quadratic'
plt.gca().set_aspect('equal', adjustable='box')

# save picture
plt.savefig('field_vectors.png')
#plt.show() #uncomment if you run the code on a local python installation