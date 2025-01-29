import numpy as np

with DigitalIn(lines=[0, 1], rate=50*kHz) as di:
    data = di.read(200*ms, raw=True)

bits = np.unpackbits(data, bitorder='little').reshape(-1, 8).T
plt.imshow(bits[:,:200], aspect='auto', interpolation='none')
plt.xlabel('Byte #')
plt.ylabel('Bit #')
