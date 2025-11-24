with AnalogOut(rate=fs) as ao:
    with DigitalOut() as do:
        with AnalogIn(channel=0) as ai:
            with DigitalIn(line=0) as di:
                ao[0].sampled(vv, scale=1*V)
                do[0].stimulus(train)
                ao.run()
                data, times = ai.readall(times=True)
                ddata = di.readall()

plt.plot(times, data, '.-', markersize=1, linewidth=0.1)
plt.plot(times, -1.5 + .3*ddata)
plt.xlabel('Time (s)')
plt.ylabel('Logic input / Voltage (V)')
plt.yticks([-1.5, -1.2, -1, 0, 1], ['Lo', 'Hi', -1, 0, 1])
