from picodaq import *
import matplotlib.pyplot as plt

with AnalogIn(channel=0, rate=50*kHz) as ai:
    data = ai.read(200*ms)

plt.plot(data)
plt.xlabel('Sample #')
plt.ylabel('Voltage (V)')
