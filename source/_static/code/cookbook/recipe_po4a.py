from picodaq import *
from picodaq.stimulus import Pulse, Train

pulse = Pulse(amplitude=1*V, duration=50*ms)
train = Train(pulse, pulseperiod=200*ms, pulsecount=10)
with AnalogOut(rate=10*kHz) as ao:
    ao[0].stimulus(train, delay=500*ms)
    ao.run()
