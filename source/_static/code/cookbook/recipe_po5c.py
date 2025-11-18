with DigitalOut(rate=50*kHz) as do:
    with DigitalIn(line=0) as di:
        do[0].stimulus(train)
        data, times = di.read(2*s, times=True)

plt.plot(times, data, '.-', markersize=1, linewidth=0.1)
plt.xlabel('Time (s)')
plt.ylabel('Input (logic)')
plt.yticks([0,1])
