from picodaq import *
from picodaq.stimulus import TTL, Train

pulse1 = TTL(duration=100*ms)
train1 = Train(pulse1, pulseperiod=200*ms, pulsecount=5)
pulse2 = TTL(duration=30*ms)
train2 = Train(pulse2, pulseperiod=100*ms, pulsecount=10)

with DigitalOut(rate=50*kHz) as do:
    do[0].stimulus(train1)
    do[1].stimulus(train2, delay=20*ms)
    do.run()
