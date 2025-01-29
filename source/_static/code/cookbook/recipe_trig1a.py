from picodaq import *
import matplotlib.pyplot as plt

with AnalogIn(channel=0, rate=100*kHz) as ai:
    with DigitalIn(line=0) as di:
        ai.trigger(0, polarity=1)
        data = ai.read(100*ms)
        ddata = di.read(100*ms)
                    
plt.plot(data)
plt.plot(ddata)
plt.xlabel('Sample #')
plt.ylabel('Voltage (V)')
