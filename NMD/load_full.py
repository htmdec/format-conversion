import numpy as np
import nmdfile
import h5py

print("Reading")
with open("exhibit 1/C103-SRS - array 2.NMD", "rb") as f:
    buf = f.read()

start = buf.find(b"<SAMPLE ")
stop = buf.find(b"</SAMPLE>") + len(b"</SAMPLE>")

xml_contents = buf[start:stop]

with open("exhibit1.xml", "w") as f:
    f.write(xml_contents.decode("utf-8"))

with h5py.File("exhibit1.h5", "w") as f:
    i = 0
    while stop < len(buf):
        print(i)
        start = stop
        num_rows = int.from_bytes(buf[start:start+4], byteorder='little')
        start += 4
        stop = start + num_rows * 8
        arr = np.frombuffer(buf[start:stop], dtype="f8")
        f.create_dataset(f"/array_{i:05d}", data = arr)
        i += 1
