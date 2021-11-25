# plt-sane

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> Sane defaults to matplotlib

## TODO

* Add and set up tests in pre-commit
* Set up actions

```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import plt_sane
# import uit_scripts.plotting.figure_standards as fig_std

# ax_size = fig_std.set_rcparams_dynamo(matplotlib.rcParams)
fig = plt.figure()
a = np.exp(np.linspace(-3, 5, 100))
# ax = fig.add_axes(ax_size)
base = 2  # Default is 10, but 2 works equally well
# ax.loglog()
# ax = log_tick_fix(ax, "both")
# ax.semilogx(base=base)  # This is not needed. Re-sets in the formatter function
plt_sane.log_tick_format(ax, "x", base=base)
# ax.semilogy()
# log_tick_fix(ax, "y")

# Do plotting ...
ax.plot(a)
plt.show()
```
