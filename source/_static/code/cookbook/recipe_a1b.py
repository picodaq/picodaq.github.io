with AnalogIn(channel=0, rate=50*kHz) as ai:
    data, times = ai.read(200*ms, times=True)

plt.plot(times, data)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
