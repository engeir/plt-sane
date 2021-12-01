import matplotlib.pyplot as plt
import numpy as np

from plastik import ridge


def r():
    # Data
    data = [
        (np.array([1, 2, 3]), np.array([6, 5, 7])),
        (np.array([22, 23, 24]), np.array([100, 1, -200])),
    ]
    ridge.ridge_plot(data, "slalomaxis", "grid", "squeeze")


if __name__ == "__main__":
    r()
    plt.show()
