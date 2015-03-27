"""Quick and Dirty Machine Learning in Python."""
# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
%matplotlib inline

np.set_printoptions(precision=4)

# <codecell>

image_name = "motorcycle.jpg"
img = Image.open(image_name)
print img
plt.imshow(img)

# <codecell>

# Scale down the image.
img.thumbnail((50, 50))  # Default resizing using nearest approch. (bilinear or bicubic)

# Load image into array h x w x RGB
data = np.array(img)
# Reshape to one dimentional array
data = np.reshape(data, (data.shape[1] * data.shape[0], 3))

# <codecell>

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

Rx = []
Gy = []
Bz = []

for pixel in data:
    Rx.append(pixel[0])
    Gy.append(pixel[1])
    Bz.append(pixel[2])
ax.scatter(Rx, Gy, Bz, zdir='z', c='b', marker='x')
Rx = []
Gy = []
Bz = []

ax.set_xlabel('Red')
ax.set_xlim([0, 256])
ax.set_ylabel('Green')
ax.set_ylim([0, 256])
ax.set_zlabel('Blue')
ax.set_zlim([0, 256])

plt.show()

# <codecell>

klust = 6
img = Image.open(image_name)
data = np.array(img)
data = np.reshape(data, (data.shape[1] * data.shape[0], 3))
ncenters = (np.random.rand(3, klust) * 256)
ocenters = np.zeros(ncenters.shape)
sub = np.subtract(ncenters, ocenters)
while int(np.sum(sub)) != 0:
    ocenters = ncenters.copy()
    sqrt_err = np.array([((data - ncenters[:, i])**2).sum(axis=1) for i in range(klust)])
    labels = np.argmin(sqrt_err, axis=0)
    for j in range(klust):
        cond = np.array([(labels == j) for each in range(3)], np.int32).transpose()
        moment = np.multiply(data, cond)
        moment = np.sum(moment, axis=0)
        mass = np.sum(cond, axis=0)[0] + 0.1
        ncenters[:, j] = np.divide(moment, mass)
    sub = np.subtract(ncenters, ocenters)

colors = []
for each in new_centroids.T:
    colors.append((each[0] / 256, each[1] / 256, each[2] / 256))
cmap = mpl.colors.ListedColormap(colors)

fig = plt.figure(figsize=(8, 3))
ax = fig.add_axes([0, 0, 2, 0.15])
cb = mpl.colorbar.ColorbarBase(ax, cmap=cmap, spacing='proportional', orientation='horizontal')
plt.show()

# <codecell>

img = Image.open(image_name)

# Load image into array h x w x RGB
data = np.array(img)
print data.shape
print data

# <codecell>

data = np.reshape(data, (data.shape[1] * data.shape[0], 3))
print data.shape
print data

# <codecell>

klust = 6
# Produce a matrix 3 x k with random values 0 - 256 not including 256.
ncenters = (np.random.rand(3, klust) * 256)
print ocenters.shape
print ocenters

# <codecell>

ocenters = ncenters.copy()
print ((data - ncenters[:, 0])**2).sum(axis=1)

# <codecell>

sqrt_err = np.array([((data - ncenters[:, i])**2).sum(axis=1) for i in range(klust)])
print sqrt_err.shape
print sqrt_err

# <codecell>

labels = np.argmin(sqrt_err, axis=0)
print labels.shape
print labels

# <codecell>

cond = np.array([(labels == 1) for i in range(3)], np.int32).transpose()
print cond.shape
print cond

# <codecell>

moment = np.multiply(data, cond)
print moment
moment = np.sum(moment, axis=0)
print moment

# <codecell>

mass = np.sum(cond, axis=0)[0]
print mass

# <codecell>

print np.divide(moment, mass)

# <codecell>

for j in range(klust):
    cond = np.array([(labels == j) for each in range(3)], np.int32).transpose()
    moment = np.multiply(data, cond)
    moment = np.sum(moment, axis=0)
    mass = np.sum(cond, axis=0)[0]
    ncenters[:, j] = np.divide(moment, mass)

# <codecell>

print ocenters
print ncenters
sub = np.subtract(ncenters, ocenters)
print sub
print int(np.sum(np.abs(sub)))

# <codecell>

klust = 6
ncenters = (np.random.rand(3, klust) * 256)

# <codecell>

ocenters = ncenters.copy()
sqrt_err = np.array([((data - ncenters[:, i])**2).sum(axis=1) for i in range(klust)])
labels = np.argmin(sqrt_err, axis=0)
for j in range(klust):
    cond = np.array([(labels == j) for each in range(3)], np.int32).transpose()
    moment = np.multiply(data, cond)
    moment = np.sum(moment, axis=0)
    mass = np.sum(cond, axis=0)[0] + 0.1
    ncenters[:, j] = np.divide(moment, mass)

# <codecell>

print ocenters
print ncenters
sub = np.subtract(ncenters, ocenters)
print sub
print int(np.sum(np.abs(sub)))

# <codecell>

colors = []
for each in ncenters.T:
    colors.append((each[0] / 256, each[1] / 256, each[2] / 256))
cmap = mpl.colors.ListedColormap(colors)

fig = plt.figure(figsize=(8, 3))
ax = fig.add_axes([0, 0, 2, 0.15])
cb = mpl.colorbar.ColorbarBase(ax, cmap=cmap, spacing='proportional', orientation='horizontal')
plt.show()
