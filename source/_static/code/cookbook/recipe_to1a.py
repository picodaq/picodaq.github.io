from picodaq import *
from picodaq.stimulus import Square, Triangle, Train

pulse1 = Triangle(amplitude=0.7*V, duration=100*ms)
train1 = Train(pulse1, pulseperiod=200*ms, pulsecount=10)
pulse2 = Square(amplitude=1*V, duration=25*ms)
train2 = Train(pulse2, pulseperiod=100*ms, pulsecount=20)
with AnalogOut(rate=50*kHz) as ao:
    ao[0].stimulus(train1)
    ao[1].stimulus(train2)
    ao.run()
