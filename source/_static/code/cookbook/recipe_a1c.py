with AnalogIn(channel=0, rate=50*kHz) as ai:
    data = ai.read(200*ms, raw=True)

plt.plot(data)
plt.xlabel('Sample #')
plt.ylabel('Digital value')
