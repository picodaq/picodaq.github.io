with AnalogOut(rate=10*kHz) as ao:
    with AnalogIn(channel=0) as ai:
        ao[0].stimulus(train, delay=500*ms)
        data, times = ai.read(3*s, times=True)

plt.plot(times, data, '.-', markersize=1, linewidth=0.1)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
