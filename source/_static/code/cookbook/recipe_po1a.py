from picodaq import *
from picodaq.stimulus import Pulse, Train, Deltas

pulse = Pulse(amplitude=1*V, duration=50*ms)
delta = Deltas(amplitude=0.2*V)
train = Train(pulse, pulseperiod=200*ms, pulsecount=10,
              perpulse=delta)
with AnalogOut(rate=50*kHz) as ao:
    ao[0].stimulus(train)
    ao.run()
