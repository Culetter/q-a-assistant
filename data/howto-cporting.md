> **Porting** **Extension** **Modules** **to** **Python** **3**
>
> ***Release*** ***3.13.3***
>
> **Guido** **van** **Rossum** **and** **the** **Python**
> **development** **team**
>
> **April** **27,** **2025**
>
> **Python** **Software** **Foundation** **Email:** **docs@python.org**

**Contents**

We recommend the following resources for porting extension modules to
Python 3:

> • The [Migrating C
> extensions](http://python3porting.com/cextensions.html) chapter from
> *Supporting* *Python* *3:* *An* *in-depth* *guide*, a book on moving
> from Python 2 to Python 3 in general, guides the reader through
> porting an extension module.
>
> • The [Porting
> guide](https://py3c.readthedocs.io/en/latest/guide.html) from the
> *py3c* project provides opinionated suggestions with supporting code.
>
> • The [Cython](https://cython.org/) and
> [CFFI](https://cffi.readthedocs.io/en/latest/) libraries offer
> abstractions over Python’s C API. Extensions generally need to be
> re-written to use one of them, but the library then handles
> differences between various Python versions and implementations.
>
> **1**
