import matplotlib.pyplot as plt
import time
import random
from collections import deque
import numpy as np
import os

def read_wifi():
	while True:
		f=os.popen('sudo iwconfig wlan0 | grep -e "Signal level"')
		line = f.read()
		splitted_line = line.split()
		level = splitted_line[3].split('=')
		print level[1]
		val = level[1]
		yield val
		time.sleep(0.1)


a1 = deque([0]*100)
ax = plt.axes(xlim=(0, 100), ylim=(0, 10))
d = read_wifi()

line, = plt.plot(a1)
plt.ion()
plt.ylim([-90,0])
plt.show()

for i in range(0,10000):
	a1.appendleft(next(d))
	datatoplot = a1.pop()
	line.set_ydata(a1)
	plt.draw()
	print a1[0]
	i += 1
	time.sleep(0.1)
	plt.pause(0.0001)

