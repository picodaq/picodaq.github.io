import matplotlib.pyplot as plt
from picodaq.mockstim import mockstim

plandata = mockstim(series, rate=50*kHz)
plt.plot(plandata)
plt.xlabel('Sample #')
plt.ylabel('Planned output (V)')
