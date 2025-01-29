with DigitalIn(lines=[0, 1], rate=50*kHz) as di:
    data = di.read(200*ms)

plt.plot(data)
plt.xlabel('Sample #')
plt.ylabel('Binary value')
