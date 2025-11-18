from picodaq.mockstim import mocksampled

vvv = mocksampled(produce, scale=1*V, rate=fs, duration=dur)
plt.plot(vvv)
plt.xlabel('Sample #')
plt.ylabel('Planned output (V)')
