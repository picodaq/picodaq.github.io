from picodaq import *
from picodaq.stimulus import Square, Train

pulse = Square(amplitude=5*V, duration=100*ms,
               amplitude2=-2.5*V, duration2=200*ms)
train = Train(pulse, pulseperiod=500*ms, pulsecount=4)
with AnalogOut(rate=50*kHz) as ao:
    ao[0].stimulus(train)
    ao.run()
