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
dataArrays = {"time": [], "x": [], "y": [], "z": [], "vx": [], "vy": [], "vz": [], "ax": [], "ay": [], "az": []}

for row in data:
    for key in dataArrays:
        dataArrays[key].append(float(row[key]))

# Plot x, y, and z velocity
plt.subplot(221)
plt.title("Velocity")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.plot(dataArrays["time"], dataArrays["vx"], label="x", color="red")
plt.plot(dataArrays["time"], dataArrays["vy"], label="y", color="green")
plt.plot(dataArrays["time"], dataArrays["vz"], label="z", color="blue")
plt.grid(True)
plt.legend()

# Plot x, y, and z acceleration
plt.subplot(223)
plt.title("Acceleration")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s^2)")
plt.plot(dataArrays["time"], dataArrays["ax"], label="x", color="red")
plt.plot(dataArrays["time"], dataArrays["ay"], label="y", color="green")
plt.plot(dataArrays["time"], dataArrays["az"], label="z", color="blue")
plt.grid(True)
plt.legend()

plt.subplot(122, projection='3d')
plt.title("Position")
plt.plot(dataArrays["x"], dataArrays["y"], dataArrays["z"], label="3D Trajectory", color="black")
plt.grid(True)

plt.show()