with DigitalIn(line=0, rate=50*kHz) as di:
    data, times = di.read(200*ms, times=True)

plt.plot(times, data)
plt.xlabel('Time (s)')
plt.ylabel('Binary value')
