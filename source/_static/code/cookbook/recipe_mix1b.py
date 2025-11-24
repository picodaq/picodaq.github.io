import numpy as np

adata = []
ddata = []
K = 10
with AnalogIn(channel=0, rate=50*kHz) as ai:
    with DigitalIn(line=0) as di:
        for k in range(K):
            adata.append(ai.read(50*ms))
            ddata.append(di.read(50*ms))
adata = np.concatenate(adata, 0)
ddata = np.concatenate(ddata, 0)

plt.plot(adata)
plt.plot(ddata)
plt.xlabel('Sample #')
plt.ylabel('Voltage (V) / Binary value')
