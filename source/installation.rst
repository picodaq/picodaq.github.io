.. _installation:

Installation
============


All you need to get started with picoDAQ is a single Python library,
called `picodaq`. There are no hardware drivers to install.

The latest version of the library is always
available through the python package archive and may be installed as follows.

Command line
------------

In Windows, Mac OS, and many versions of Linux, a simple

.. code-block::

    pip install picodaq

gets you the latest. This works without restriction in `virtual
environments <https://docs.python.org/3/library/venv.html>`_ as well.

IDEs
----
    
Many Python IDEs provide convenient front ends for ``pip``. For
instance, in PyCharm, in Settings -> Project -> Python Interpreter,
you can click the “+” icon to show a list of available packages, which
includes picodaq. In VSCode, one of the easiest methods is to type
``!pip install picodaq`` in an Interactive session. Be sure to first
create a virtual environment, unless you want to install picodaq
system-wide.

Jupyter
-------

Picodaq works without limitation in a local Jupyter notebook. Use
``!pip install picodaq`` to install the library. While picodaq can be
installed in Google Colab or other cloud-based notebooks, this is
probably not useful because the virtual machine will not have access
to your hardware.


Verifying software installation
-------------------------------

Open your favorite Python IDE or Notebook. Type

.. code-block::

    import picodaq
    print(picodaq.version)
    
and run that code. You should be greeted with a version number, like

.. code-block:: text

    "0.1.240124"

If, instead, you receive a ModuleNotFoundError exception, make sure
that the environment used by your IDE includes the place where you
installed the ``picodaq`` library. It may be helpful to

.. code-block::

    import sys
    print(sys.path)
    
Troubleshooting strategies for this situation vary by
IDE. Fortunately, advice is broadly available on the internet.

Next steps
----------

Now that you have installed picoDAQ, the next step is to :ref:`see if
it works <firstrun>`.
