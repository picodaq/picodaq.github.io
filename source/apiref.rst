.. _apiref:

API Reference
=============

Primary classes
---------------

The most important classes you will use directly in your code are the
“Stream” classes:

* :ref:`AnalogIn <api-ai>`
* :ref:`AnalogOut <api-ao>`
* :ref:`DigitalIn <api-di>`
* :ref:`DigitalOut <api-do>`

as well as the classes used for parametric stimulation:

* :ref:`Pulse and friends <api-pulse>`
* :ref:`Train <api-train>`
* :ref:`Series <api-series>`
* :ref:`Deltas <api-deltas>`

You will also use various “units” constants:

* :ref:`Units for time, frequency, and voltage <api-units>`

and perhaps some auxiliary functions:

* :ref:`Functions to query connected devices <api-devices>`


Secondary classes
-----------------

The following classes are part of the `picodaq` API but are not
generally used directly outside the library itself:

* :ref:`PicoDAQ <api-device>`
* :ref:`BinaryReader <api-binreader>`
* :ref:`BinaryWriter <api-binwriter>`
* :ref:`Quantity <api-quantity>`

  
.. toctree::
   :maxdepth: 2
   :hidden:
   
   api-ai
   api-ao
   api-di
   api-do
   api-pulse
   api-train
   api-series
   api-deltas
   api-units
   api-devices
   api-device
   api-binreader
   api-binwriter
   api-quantity
