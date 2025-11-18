with AnalogOut(rate=50*kHz) as ao:
    with AnalogIn(channel=0) as ai:
        ao[0].stimulus(train)
        data, times = ai.read(2*s, times=True)

plt.plot(times, data, '.-', markersize=1, linewidth=0.1)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
