# plastik

# General imports
import matplotlib.pyplot as plt
import numpy as np

import plastik

SAVEDIR = "examples/figures"

## Log tick format --------------------------------------------------------------------- #

# 1

y = np.exp(np.linspace(-3, 5, 100))
base = 2  # Default is 10, but 2 works equally well
plt.figure()
plastik.log_tick_format(plt.gca(), "x", base=base)
plt.plot(y)
plt.savefig(f"{SAVEDIR}/log_tick_format1.png")
plastik.dark_theme(plt.gca(), fig=plt.gcf())
plt.savefig(f"{SAVEDIR}/log_tick_format1_dark.png")
plt.close("all")

# 2
y = np.exp(np.linspace(-3, 5, 100))
base = 2  # Default is 10, but 2 works equally well
fig = plt.figure()
ax = fig.add_subplot(111)
ax.loglog()
plastik.log_tick_format(ax, "both", base=base)
ax.plot(y)
plt.savefig(f"{SAVEDIR}/log_tick_format2.png")
plastik.dark_theme(ax, fig=fig)
plt.savefig(f"{SAVEDIR}/log_tick_format2_dark.png")
plt.close("all")

# 3
y = np.exp(np.linspace(-3, 5, 100))
fig = plt.figure()
ax = fig.add_subplot(111)
ax = plastik.log_tick_format(ax, "y")

# If you do:
ax.semilogy(y)
# the axis will be re-set, in which case you will have to run
plastik.log_tick_format(ax, "y")
# again. (But just use plt.plot(), so much easier.)
plt.savefig(f"{SAVEDIR}/log_tick_format3.png")
plastik.dark_theme(ax, fig=fig)
plt.savefig(f"{SAVEDIR}/log_tick_format3_dark.png")
plt.close("all")

## Topside legends --------------------------------------------------------------------- #

# 1
y = np.linspace(-3, 5, 100)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(y, label="Topside legend 1")
ax.plot(y + 1, label="Topside legend 2")
ax.plot(y + 2, label="Topside legend 3")
ax.plot(y + 3, label="Topside legend 4")
plastik.topside_legends(ax, c_max=2, side="bottom", alpha=0.2)
plt.savefig(f"{SAVEDIR}/topside_legends1.png")
plastik.dark_theme(ax, fig=fig)
plt.savefig(f"{SAVEDIR}/topside_legends1_dark.png")
plt.close("all")

# 2
y = np.linspace(-3, 5, 100)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(y, label="Topside legend 1")
ax.plot(y + 1, label="Topside legend 2")
ax.plot(y + 2, label="Topside legend 3")
ax.plot(y + 3, label="Topside legend 4")
plastik.topside_legends(ax, c_max=3, side="top right", alpha=1)
plt.savefig(f"{SAVEDIR}/topside_legends2.png")
plastik.dark_theme(ax, fig=fig)
plt.savefig(f"{SAVEDIR}/topside_legends2_dark.png")
plt.close("all")

## Ridge ------------------------------------------------------------------------------- #

# Set up
x = np.linspace(1e-1, 3e1, 1000) ** 2


def func(x, s):
    return 10 / ((x - s) ** 2 + 1)


dt = [func(x, 3), func(x, 1), func(x, 0), func(x, 100), func(x, 300), func(x, 500)]
dta = [(x, y) for y in dt]

lab = [f"{i}" for i in range(6)]

# 1
r = plastik.Ridge(dta, "gsz", xlabel="bottom", ylabel="xlabel")
r.main()
f = r.figure
ell = r.lines
a = r.top_axes
axs = r.all_axes
a.legend(ell, lab)
plt.savefig(f"{SAVEDIR}/ridge1.png")
plastik.dark_theme(r.bottom_axes, keep_yaxis=True, fig=f)
plastik.dark_theme(r.ax)
plt.savefig(f"{SAVEDIR}/ridge1_dark.png")
plt.close("all")


# 2
r = plastik.Ridge(dta, "gs", ylabel="xlabel")
r.main()
f = r.figure
ell = r.lines
a = r.top_axes
axs = r.all_axes
a.legend(ell, lab)
plastik.topside_legends(a, ell, c_max=6, side="right")
for ax in axs:
    plastik.log_tick_format(ax, which="y")
plt.savefig(f"{SAVEDIR}/ridge2.png")
plastik.dark_theme(r.bottom_axes, keep_yaxis=True, fig=f)
plastik.dark_theme(r.ax)
plt.savefig(f"{SAVEDIR}/ridge2_dark.png")
plt.close("all")

# 3
r = plastik.Ridge(
    dta, "s", xlabel="bottom axis label", ylabel="xlabel", pltype="semilogx"
)
r.main()
f = r.figure
ell = r.lines
a = r.top_axes
axs = r.all_axes
a.legend(ell, lab)
plastik.topside_legends(a, ell, c_max=5, side="right")
for ax in axs:
    plastik.log_tick_format(ax, which="x")
plt.savefig(f"{SAVEDIR}/ridge3.png")
plastik.dark_theme(r.bottom_axes, keep_yaxis=True, fig=f)
plastik.dark_theme(r.ax)
plt.savefig(f"{SAVEDIR}/ridge3_dark.png")
plt.close("all")

# 4
r = plastik.Ridge(dta, "bz", ylabel="xlabel", pltype="loglog")
r.main()
f = r.figure
a = r.bottom_axes
axs = r.all_axes
for ax in axs:
    plastik.log_tick_format(ax, which="both")
plt.savefig(f"{SAVEDIR}/ridge4.png")
plastik.dark_theme(r.bottom_axes, keep_yaxis=True, fig=f)
plastik.dark_theme(r.ax)
plt.savefig(f"{SAVEDIR}/ridge4_dark.png")
plt.close("all")

## Dark theme -------------------------------------------------------------------------- #

# 1
y = np.exp(np.linspace(-3, 5, 100))
plt.figure()
# Sets axes and labels of given axis to white
plastik.dark_theme(plt.gca())
plastik.log_tick_format(plt.gca(), "both", base=2)
plt.plot(y)
plt.xlabel("white label")
plt.ylabel("ylabel")
plt.savefig(f"{SAVEDIR}/dark_theme.png")
plt.close("all")
