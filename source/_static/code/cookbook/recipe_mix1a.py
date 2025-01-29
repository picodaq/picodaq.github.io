from picodaq import *
import matplotlib.pyplot as plt

with AnalogIn(channel=0, rate=50*kHz) as ai:
    with DigitalIn(line=0, rate=50*kHz) as di:
        adata = ai.read(200*ms)
        ddata = di.read(200*ms)

plt.plot(adata)
plt.plot(ddata)
plt.xlabel('Sample #')
plt.ylabel('Voltage (V) / Binary value')
