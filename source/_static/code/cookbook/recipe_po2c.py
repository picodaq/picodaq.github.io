with AnalogOut(rate=50*kHz) as ao:
    with AnalogIn(channel=0) as ai:
        ao[0].stimulus(train)
        ao.run()
        data, times = ai.readall(times=True)

plt.plot(times, data, '.-', markersize=1, linewidth=0.1)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
