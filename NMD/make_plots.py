import matplotlib.pyplot as plt
import numpy as np
import h5py

with h5py.File("exhibit1.h5", "r") as f:
    for i in range(1600):
        print(i)
        plt.clf()
        plt.plot(f[f"/array_{i:05d}"][:])
        plt.title(f"Array {i:05d} -- Test {int(i//25)} -- Data Index {i % 25}")
        plt.savefig(f"frames/array_{i:05d}.png")
