# -*- coding: utf-8 -*-
"""
Created on Sun Dec 5 00:25:04 2021

@author: Perry
"""
# import csv and matplotlib
import csv
import matplotlib.pyplot as plt

# read data.csv into a dictionary called data
data = csv.DictReader(open("data.csv"))

# split the data into three lists for x, y, and z
x = []
y = []
z = []
for row in data:
    x.append(float(row["x"]))
    y.append(float(row["y"]))
    z.append(float(row["z"]))

# create a 3d line plot with the x, y, and z values
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
plt.show()