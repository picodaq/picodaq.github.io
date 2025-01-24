.. _firstrun:

First run
=========

Before anything else, make sure you have :ref:`installed the picodaq
library <installation>` and that you can `import` it into your Python
session.


Making connections
------------------

The first step after that is to connect your picoDAQ device to your
computer with a USB cable. Your computer may take a few moments
sniffing out its new friend, but pretty soon, the “status” light on
your picoDAQ should start to slowly blink green, indicating its
readiness to receive instructions. For this very first test, do not
attach anything to the picoDAQ’s BNC connectors.


Acquiring some data
-------------------

Run the following snippet of Python code, either through an IDE or
directly in the Python prompt:

.. code-block::
   
    from picodaq import *
    import matplotlib.pyplot as plt

    with AnalogIn(channel=0, rate=10*kHz) as ai:
        data = ai.read(1000)

    plt.plot(data)
    plt.show()

That will acquire 100 ms of data from channel “ai0”. Since nothing is
physically connected to that channel, you will only record noise. If
you put a finger on the shell of connector while recording, you will
get a much larger signal.

Today, in my office, the result looks like this:


.. image:: unconnected.png
  :width: 336
  :align: center
  :alt: Screenshot of plot of recording line noise

The horizontal axis is measured in samples, so this trace represents
100 ms. The vertical axis is in Volts. The blue trace represents the
first recording, the orange one a recording during which I touched the
connector to induce additional pickup.


Next steps
----------

That is it! If you got this far, your device is up and running and you are off to the races. We have collected a set of `cookbook recipes <cookbook>`_ to demonstrate the use of picoDAQ in different data acquisition scenarios. To delve into the details of the functionality of the ``AnalogIn`` class and its friends, read the `API reference <apiref>`_.


Troubleshooting
---------------

If the LED does not blink, first try a different USB cable or a
different USB port.

If that does not help, check if the picoDAQ shows up in your
computer’s device tree. For instance, in Linux, if you type

.. code-block::
   
    lsusb

into a terminal, you should see

.. code-block:: text

    Bus 003 Device 099: ID 2e8a:000a net.danielwagenaar picoDAQ

among the list of devices. (The “Bus” and “Device” numbers will be
different on your computer.) Likewise, in Windows, a line like “USB
Serial Device (COM3)” should show up under “Ports (COM & LPT)” in the
“Device Manager”. If you right-click on that line, choose
“Properties”, navigate to the “Details” tab, and select “Hardware Ids”
from the “Property” pull down, you should see “VID_2E8A&PID_000A”
among the spaghetti.

If the device shows up in the device tree, but does not work ...

If it does not show up at all...

If it shows up but with different IDs...
