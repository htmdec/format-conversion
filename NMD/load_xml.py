import numpy as np
import nmdfile
import h5py

print("Reading")
with open("exhibit 1/C103-SRS - array 2.NMD", "rb") as f:
    buf = f.read()
print("Parsing")
nmd = nmdfile.Nmdfile.from_bytes(buf)

with open("exhibit1.xml", "w") as f:
    f.write(nmd.xml.contents)

with h5py.File("exhibit1.h5", "w") as f:
    for i, a in enumerate(nmd.data):
        print(i)
        arr = np.frombuffer(a.values, dtype="f8")
        f.create_dataset(f"/array_{i:05d}", data = arr)
