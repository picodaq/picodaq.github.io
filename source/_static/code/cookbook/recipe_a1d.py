import numpy as np

data = []
times = []
K = 25
with AnalogIn(channel=0, rate=50*kHz) as ai:
    for k in range(K):
        dat, tms = ai.read(20*ms, times=True)
        print(f"Progress {k+1}/{K}", end="\r")
        data.append(dat)
        times.append(tms)
print()
data = np.concatenate(data, 0)
times = np.concatenate(times, 0)

plt.plot(times, data)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
