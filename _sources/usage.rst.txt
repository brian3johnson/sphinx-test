Usage
=====

.. _installation:

Installation
------------

To use sphinx-test, first install it using pip:

.. code-block:: console

   (venv) $ pip install sphinx-test

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:


The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

link to lumache doc at :doc:`LUMACHE </apidoc/lumache>`

lumache module: :mod:`lumache`
lumache.get_random_ingredients: :func:`lumache.get_random_ingredients`