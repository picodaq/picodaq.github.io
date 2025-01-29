from picodaq import *
import matplotlib.pyplot as plt

with DigitalIn(line=0, rate=50*kHz) as di:
    data = di.read(200*ms)

plt.plot(data)
plt.xlabel('Sample #')
plt.ylabel('Binary value')
