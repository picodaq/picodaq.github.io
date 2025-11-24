with AnalogOut(rate=50*kHz) as ao:
    with AnalogIn(channels=[0, 1]) as ai:
        ao[0].stimulus(train1)
        ao[1].stimulus(train2)
        ao.run()
        data, times = ai.readall(times=True)

plt.plot(times, data, '.-', markersize=1, linewidth=0.1)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
