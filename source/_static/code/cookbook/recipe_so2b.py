from picodaq.mockstim import mocksampled

vvv = mocksampled(produce, scale=1*V, rate=fs, duration=10*s)
plt.plot(vvv)
plt.xlabel('Sample #')
plt.ylabel('Planned output (V)')
plt.xlim(50000, 60000)
