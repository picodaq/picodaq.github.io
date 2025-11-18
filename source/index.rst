.. _index:
   
picoDAQ
=======

Why should reading from your data acquisition system be any harder
than reading from a file? With picoDAQ, it isn’t. Reading data from a
DAQ into a `NumPy array <https:numpy.org>`_ is literally as easy as:

.. code-block::

    with AnalogIn(channels=[0,1], rate=100*kHz) as ai:
        data = ai.read(10*s)

(That reads 10 seconds of data from channels 0 and 1 at a rate of 100
kilohertz.)

If you like the sound of that, :ref:`get one of the supported devices
<supportedhardware>` or build one yourself following our tutorial,
:ref:`install the library <installation>`, and :ref:`start acquiring
data <firstrun>`!


Getting Started
---------------

* :ref:`supportedhardware`
* :ref:`installation`
* :ref:`firstrun`


How-To Guides
-------------

* :ref:`cookbook`


Reference
---------

* :ref:`apiref`
* :ref:`hwspecs`

  
.. toctree::
   :maxdepth: 3
   :titlesonly:
   :hidden:

   supportedhardware
   installation
   firstrun
   cookbook
   apiref
   hwspecs
