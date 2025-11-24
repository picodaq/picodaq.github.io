import matplotlib.pyplot as plt
from picodaq.mockstim import mockstim

plandata1 = mockstim(train1, rate=50*kHz)
plandata2 = mockstim(train2, rate=50*kHz)
plt.plot(plandata1)
plt.plot(plandata2)
plt.xlabel('Sample #')
plt.ylabel('Planned output (V)')
