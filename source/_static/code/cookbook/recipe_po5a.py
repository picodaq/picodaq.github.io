from picodaq import *
from picodaq.stimulus import TTL, Train

pulse = TTL(duration=50*ms)
train = Train(pulse, pulseperiod=200*ms, pulsecount=10)
with DigitalOut(rate=50*kHz) as do:
    do[0].stimulus(train)
    do.run()
