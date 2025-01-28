#!/usr/bin/python3

from picodaq import *
import matplotlib.pyplot as plt
import inspect
plt.ion()



def recipe_a1a():
    
    from picodaq import *
    import matplotlib.pyplot as plt

    with AnalogIn(channel=0, rate=20*kHz) as ai:
        data = ai.read(10*s)

    plt.plot(data)
    plt.xlabel('Sample #')
    plt.ylabel('Channel 0 (V)')

    
def recipe_a1b():

    with AnalogIn(channel=0, rate=20*kHz) as ai:
        data, times = ai.read(10*s, times=True)

    plt.plot(times, data)
    plt.xlabel('Time (s)')
    plt.ylabel('Channel 0 (V)')

    
    
def recipe_a1c():

    with AnalogIn(channel=0, rate=20*kHz) as ai:
        data = ai.read(10*s, raw=True)

    plt.plot(data)
    plt.xlabel('Sample #')
    plt.ylabel('Digital value')



def showandsave(name, obj):
    f = plt.figure(figsize=[5, 3])
    f.clf()
    obj()
    if f.axes:
        f.savefig(f"source/_static/imgs/cookbook/{name}.png")
    else:
        f.close()
    src = inspect.source(obj)
    

if __name__ == "__main__":
    vv = {k:v for k,v in vars().items()}
    for name, obj in vv.items():
        if name.startswith("recipe_") and callable(obj):
            showandsave(name, obj)
