# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 21:31:18 2018

@author: pfdlo
"""

class Colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
from matplotlib import rc
import pandas as pd 
import scipy.fftpack
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# settings
numberProfiles = 1000
startTimeUsec = 0
incrementTimeUsec = 500
profileNumberOfPoints = 256
radialPositionFileName = 'marte_allprofiles/ProfileRadialPosition.gz'
radialDensityFileName = 'marte_allprofiles/ProfileRadialDensity.gz'

# timeAxis
timeAxis = np.linspace(0,numberProfiles-1,numberProfiles)
for i in range(len(timeAxis)):
    timeAxis[i] = startTimeUsec + timeAxis[i]*incrementTimeUsec

# print(len(timeAxis))

# open data
file = open(radialPositionFileName, "rb")
radialPosition = np.fromfile(file, '<f4')
file.close()
file = open(radialDensityFileName, "rb")
radialDensity = np.fromfile(file, '<f4')
file.close()

radialPositionArray = np.zeros((numberProfiles, profileNumberOfPoints))
for i in range(numberProfiles):
    radialPositionArray[i][0:profileNumberOfPoints] = radialPosition[(0 + i*profileNumberOfPoints):(profileNumberOfPoints  + i*profileNumberOfPoints)]

radialDensityArray = np.zeros((numberProfiles, profileNumberOfPoints))
for i in range(numberProfiles):
    radialDensityArray[i][0:profileNumberOfPoints] = radialDensity[(0 + i*profileNumberOfPoints):(profileNumberOfPoints + i*profileNumberOfPoints)]


X, Y = np.meshgrid(radialDensityArray[0][:],timeAxis)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X, Y, radialPositionArray, rstride=128, cstride=128, cmap='plasma', shade=False)
# ax.plot_surface(X, Y, radialPositionArray, rcount=128, ccount=128, cmap='plasma', shade=False)
ax.contour3D(X, Y, radialPositionArray, 256, cmap='plasma')
# ax.set_xlim(0.0, 1.0)
# ax.set_ylim(timeAxis[0], timeAxis[numberProfiles-1])
# ax.set_zlim(0, 1e19)
# ax.set_xlabel("r [m]")
ax.set_xlabel("n$_e$ [m$^{-3}$]")
ax.set_ylabel("t [us]")
ax.set_zlabel("r [m]")
ax.view_init(120, 50)
plt.show()


# plt.plot(radialPositionArray[0][:],radialDensityArray[0][:])
# plt.plot(radialPositionArray[100][:],radialDensityArray[100][:])
# plt.plot(radialPositionArray[227][:],radialDensityArray[227][:])
# plt.plot(radialPositionArray[350][:],radialDensityArray[350][:])
# plt.plot(radialPositionArray[500][:],radialDensityArray[500][:])
# plt.plot(radialPositionArray[600][:],radialDensityArray[600][:])
# plt.plot(radialPositionArray[700][:],radialDensityArray[700][:])
# plt.plot(radialPositionArray[500][0:255])
# plt.plot(radialPositionArray[501][0:255])
# plt.plot(radialPositionArray[502][0:255])
# plt.plot(radialPositionArray[503][0:255])
# plt.plot(radialPositionArray[504][0:255])
# plt.plot(radialPositionArray[505][0:255])
# plt.plot(radialPositionArray[506][0:255])
# plt.plot(radialPositionArray[507][0:255])
# plt.plot(radialPositionArray[508][0:255])
# plt.plot(radialPositionArray[509][0:255])
# plt.show()



# ax.plot_surface(X, Y, Z, cmap='autumn', shade=True, lw=.5)

# x = np.linspace(-50,50,100)
# y = np.arange(25)
# X,Y = np.meshgrid(x,y)
# Z = np.zeros((len(y),len(x)))

# for i in range(len(y)):
#     damp = (i/float(len(y)))**2
#     Z[i] = 5*damp*(1 - np.sqrt(np.abs(x/50)))
#     Z[i] += np.random.uniform(0,.1,len(Z[i]))

# # ax.plot_surface(X, Y, Z, cmap='autumn', shade=True, lw=.5)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# # ax.plot_surface(X, Y, Z, cmap='autumn', shade=False, lw=.5)
# ax.plot_surface(X, 0, 2, cmap='autumn', shade=False, lw=.5)
# # ax.set_xlim(0.0, 1.0)
# # ax.set_ylim(timeAxis[0], timeAxis[numberProfiles-1])
# # ax.set_zlim(0, 1e19)
# ax.set_xlabel("r [m]")
# ax.set_ylabel("t [us]")
# ax.set_zlabel("n$_e$ [m$^{-3}$]")
# ax.view_init(20,120)
# plt.show()