# plt-sane

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> Sane defaults to matplotlib

## TODO

* Add and set up tests in pre-commit
* Set up actions

## Install

```sh
# Into poetry project
poetry add git+https://github.com/engeir/plt-sane.git@main
# With pip
pip install git+https://github.com/engeir/plt-sane.git
```

## Usage

```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import plt_sane

a = np.exp(np.linspace(-3, 5, 100))
base = 2  # Default is 10, but 2 works equally well
plt.figure()
# ax.loglog()
# ax = log_tick_fix(ax, "both")
# ax.semilogx(base=base)  # This is not needed. Re-sets in the formatter function
plt_sane.log_tick_format(ax, "x", base=base)
# ax.semilogy()
# plt_sane.log_tick_format(ax, "y")

# Do plotting ...
ax.plot(a)
# If you do:
# ax.semilogx(a)
# the axis will be re-set, in which case you will have to run
# plt_sane.log_tick_format(ax, "x", base=base)
# again. (But just use plt.plot(), so much easier.)
plt.show()
```
