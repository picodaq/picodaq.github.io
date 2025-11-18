import matplotlib.pyplot as plt
from picodaq.mockstim import mockstim

plandata = mockstim(train, rate=10*kHz, delay=500*ms)
plt.plot(plandata)
plt.xlabel('Sample #')
plt.ylabel('Planned output (V)')
