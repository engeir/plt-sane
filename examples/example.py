# plastik

# General imports
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import plastik

SAVEDIR = "examples/figures"

# Log tick format -------------------------------------------------------------------- #


def log_tick_format():
    # 1
    y = np.exp(np.linspace(-3, 5, 100))
    base = 2  # Default is 10, but 2 works equally well
    plt.figure()
    plastik.log_tick_format(plt.gca(), "x", base=base)
    plt.plot(y)
    plt.savefig(f"{SAVEDIR}/log_tick_format1.png")
    plastik.dark_theme(plt.gca(), fig=plt.gcf())
    plt.savefig(f"{SAVEDIR}/log_tick_format1_dark.png")
    plt.show()
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
    plt.show()
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
    plt.show()
    plt.close("all")


# Topside legends -------------------------------------------------------------------- #


def topside_legends():
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
    plt.show()
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
    plt.show()
    plt.close("all")


# Ridge ------------------------------------------------------------------------------ #


def ridge():
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
    plt.show()
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
    plt.show()
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
    plt.show()
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
    plt.show()
    plt.close("all")


# Dark theme ------------------------------------------------------------------------- #


def dark_theme():
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
    plt.show()
    plt.close("all")


# Color map -------------------------------------------------------------------------- #
def color_map():
    prints = plastik.colors.create_colorlist("gist_rainbow", 20)
    print(prints)
    color_map = plastik.colors.create_colorlist("gist_rainbow", 20, map=True)
    # First 5 colors in the map
    first_five = [mpl.colors.to_hex(c) for c in color_map(range(5))]
    print(first_five)
    # All 20 colors in the map, with the last one repeated 30 times
    print([mpl.colors.to_hex(c) for c in color_map(range(50))])
    # All colors in the map
    color_list = [mpl.colors.to_hex(c) for c in color_map(range(20))]
    print(all(j == k for j, k in zip(prints, color_list)))  # True
    # A new map based on raw input (first five from gist_rainbow, n=20) is created and
    # samples are drawn from it.
    print(first_five)
    print(plastik.colors.create_colorlist(first_five, 20))

    custom_colors = ["#123456", "#654321", "#fedcba", "#abcdef", "#aa11aa", "#11aa11"]
    custom_colors_map = plastik.colors.create_colorlist(custom_colors, 20, map=True)
    print([mpl.colors.to_hex(c) for c in custom_colors_map(range(20))])

    # Plot the colors
    # As a color swatch 1
    plt.figure()
    plastik.colors.make_color_swatch(plt.gca(), color_map)
    # As a color swatch 2
    plt.figure()
    plastik.colors.make_color_swatch(plt.gca(), color_map, no_ticks=True, resolution=7)
    # As a color swatch 3
    plt.figure()
    plastik.colors.make_color_swatch(plt.gca(), color_map, no_border=True, ratio=50)
    # As an inset with other data
    plt.figure()
    ax = plt.gca()
    x0, y0, width, height = 0.52, 0.8, 0.40, 0.25
    ax.scatter(
        np.arange(20),
        np.ones(20),
        c=custom_colors_map(range(20)),
    )
    ax2 = ax.inset_axes([x0, y0, width, height])
    plastik.colors.make_color_swatch(ax2, custom_colors_map, no_border=True, ratio=5)
    plt.show()

    # And as our final trick, let us use a pre-defined colour palette for a section of
    # the colour map, in addition to adding in some of our own.
    viridis = plastik.colors.create_colorlist("cmc.batlow", 14)
    v_check = plastik.colors.create_colorlist(viridis, 14)
    v_check2 = plastik.colors.create_colorlist([viridis[0], viridis[-1]], 14)
    print(viridis)  # True viridis (by definition)
    print(v_check)  # True viridis (equivalent to above)
    print(v_check2)  # Incorrect (fills in between according to a different method)
    # Now combine viridis with some random colours.
    custom = viridis.copy()
    for _ in range(3):
        custom.append("#6543ff")
    for _ in range(3):
        custom.insert(0, "#2eff2e")
    # Plot the color_map alone.
    plt.figure(figsize=(10, 1), layout="constrained")
    plastik.colors.make_color_swatch(plt.gca(), custom, no_ticks=False)
    # As an inset with other data
    plt.figure()
    ax = plt.gca()
    x0, y0, width, height = 0.52, 0.8, 0.40, 0.15
    ax.scatter(
        np.arange(len(custom)),
        np.ones(len(custom)),
        c=custom,
    )
    ax2 = ax.inset_axes([x0, y0, width, height])
    plastik.colors.make_color_swatch(ax2, custom, ratio=2 * len(custom), no_border=True)
    plt.show()


if __name__ == "__main__":
    color_map()
