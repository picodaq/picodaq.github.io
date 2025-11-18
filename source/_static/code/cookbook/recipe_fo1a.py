from picodaq import *
from picodaq.stimulus import Square, Train

pulse = Square(amplitude=1*V, duration=100*ms)
train = Train(pulse, pulseperiod=200*ms, pulsecount=10)
with AnalogOut(rate=50*kHz) as ao:
    ao[0].stimulus(train)
    ao.run()
