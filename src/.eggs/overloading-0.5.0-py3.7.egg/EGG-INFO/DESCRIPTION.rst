

``overloading`` is a module that provides function and method dispatching
based on the types and number of runtime arguments.

When an overloaded function is invoked, the dispatcher compares the supplied
arguments to available signatures and calls the implementation providing the
most accurate match:

.. code:: python

    @overload
    def biggest(items: Iterable[int]):
        return max(items)

    @overload
    def biggest(items: Iterable[str]):
        return max(items, key=len)

.. code:: python

    >>> biggest([2, 0, 15, 8, 7])
    15
    >>> biggest(['a', 'abc', 'bc'])
    'abc'


Features
========

* Function validation during registration and comprehensive resolution rules
  guarantee a well-defined outcome at invocation time.
* Supports the `typing`_ module introduced in Python 3.5.
* Supports optional parameters.
* Supports variadic signatures (``*args`` and ``**kwargs``).
* Supports class-/staticmethods.
* Evaluates both positional and keyword arguments.
* No dependencies beyond the standard library

.. _typing:   https://docs.python.org/3/library/typing.html


Documentation
=============

The full documentation is available at https://overloading.readthedocs.org/.




