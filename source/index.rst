.. _index:
   
picoDAQ
=======

Why should reading from your data acquisition system be any harder
than reading from a file? With picoDAQ, it isn’t. Reading 10 seconds
of data from two analog channels into a `NumPy array
<https:numpy.org>`_ is literally as easy as:

.. code-block::

    with AnalogIn(channels=[0,1], rate=100*kHz) as ai:
        data = ai.read(10*s)

If you like the sound of that, :ref:`get one of the supported devices
<supportedhardware>` (don’t worry, very inexpensive options exist),
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
   :maxdepth: 2
   :hidden:

   supportedhardware
   installation
   firstrun
   cookbook
   apiref
   hwspecs
