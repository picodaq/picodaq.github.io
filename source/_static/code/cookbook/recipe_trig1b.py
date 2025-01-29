from picodaq import *
import matplotlib.pyplot as plt

with AnalogIn(channel=0, rate=100*kHz) as ai:
    ai.trigger(0, polarity=-1)
    data = ai.read(100*ms)
                    
plt.plot(data)
plt.xlabel('Sample #')
plt.ylabel('Voltage (V)')
