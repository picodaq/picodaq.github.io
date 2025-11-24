import matplotlib.pyplot as plt
from picodaq.mockstim import mockstim

plandata1 = mockstim(train1, rate=50*kHz)
plandata2 = mockstim(train2, rate=50*kHz, delay=20*ms)
plt.plot(plandata1 + 2)
plt.plot(plandata2)
plt.xlabel('Sample #')
plt.ylabel('Planned output (logic)')
plt.yticks([0, 1, 2, 3], [0, 1, 0, 1])
