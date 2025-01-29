import numpy as np

data = []
ddata = []
K = 20
with AnalogIn(channel=0, rate=100*kHz) as ai:
    with DigitalIn(line=0) as di:
        ai.episodic(duration=19*ms, period=0*ms)
        ai.trigger(0, polarity=1)
        for k in range(K):
            data.append(ai.read())
            ddata.append(di.read())
data = np.stack(data, 1)
ddata = np.stack(ddata, 1)
                    
plt.plot(data)
plt.plot(ddata)
plt.xlabel('Sample #')
plt.ylabel('Voltage (V)')
