import matplotlib.pyplot as plt
from picodaq.stimulus import Wave, Train
from picodaq.mockstim import mockstim

pulse = Wave(data=sinedata, scale=8*V)
train = Train(pulse, pulseperiod=1/f_wave, pulsecount=10)
plandata = mockstim(train, rate=50*kHz)
plt.plot(plandata)
plt.xlabel('Sample #')
plt.ylabel('Planned output (V)')
