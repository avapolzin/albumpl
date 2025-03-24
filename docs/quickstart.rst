.. _albumpl.quickstart:

Quickstart Guide
================

How to use ``albumpl``:
-----------------------

If you are using v0.2 or below, before doing anything you will need to register the new album-inspired colormaps. To do this:

.. code-block:: python

	from albumpl.cmap import register_all

	register_all()

This is necessary for any of the ``albumpl.palette`` functions that use the colormaps, such as ``set_default`` and ``set_default_cmap``. This is not necessary for versions >0.3.

* **To list all palettes and their properties:**

.. code-block:: python

	from albumpl.palette import list_palettes

	list_palettes()

You can also filter for number of colors in the color cycle or type of colormap (sequential/diverging) with the arguments mincolors and maptype.

* **To list all colormaps:**

.. code-block:: python

	from albumpl.cmap import list_maps

	list_maps()


* **To set palette as default for both color cycle and colormap:**

.. code-block:: python

	from albumpl.palette import set_default

	set_default('LondonCalling')


* **To set a palette as default for color cycle or colormap:**

.. code-block:: python

	from albumpl.palette import set_default_ccyle, set_default_cmap

	set_default_ccyle('Antisocialites')

*or*

.. code-block:: python

	set_default_cmap('RhumbLine')



* **To access colormaps without setting them as default:**

You can access all of the colormaps using strings -- i.e., 'Matangi' or 'MellonCollie_r' for the reversed 'MellonCollie' map.

.. code-block:: python

	import matplotlib.pyplot as plt
	from albumpl.cmap import * #yes, this is bad practice, but easiest in this case!

	register_all() #should only be run one time at the beginning of a script
	plt.imshow(image, cmap = 'Yoshimi')


If you are using version 0.2 or older you can access the colormaps via functions (offered as an option since it can be kind of nice for things like easily toggling whether a map is reversed or not) -- this is deprecated in v0.3 and above:

.. code-block:: python

	import matplotlib.pyplot as plt
	from albumpl.cmap import * #yes, this is bad practice, but easiest in this case!

	plt.imshow(image, cmap = Yoshimi())

To reverse the colormap, use the argument `reverse_cmap = True` or just feed the colormap the string "reverse" or "_r".

.. code-block:: python

	plt.imshow(image, cmap = Figure8(reverse_cmap = True))

*or*

.. code-block:: python

	plt.imshow(image, cmap = LiveThroughThis('reverse'))

*or*

.. code-block:: python

	plt.imshow(image, cmap = Post('_r'))


* **To access the colors in a color cycle/palette without setting a default:**

.. code-block:: python

	from albumpl.palette import return_colors

	return_colors('VampireWeekend')



All of the individual functions are detailed below.

.. automodule:: albumpl.palette
	:imported-members:
	:members:
	:undoc-members:
	:show-inheritance:


.. automodule:: albumpl.cmap
	:imported-members:
	:members:
	:undoc-members:
	:show-inheritance:
