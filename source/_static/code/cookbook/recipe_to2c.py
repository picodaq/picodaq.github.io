with DigitalOut(rate=50*kHz) as do:
    with DigitalIn(lines=[0, 1]) as di:
        do[0].stimulus(train1)
        do[1].stimulus(train2, delay=20*ms)
        do.run()
        data, times = di.readall(times=True)


plt.plot(times, data[:,0] + 2)
plt.plot(times, data[:,1])
plt.xlabel('Time (s)')
plt.ylabel('Input (logic)')
plt.yticks([0, 1, 2, 3], [0, 1, 0, 1])
