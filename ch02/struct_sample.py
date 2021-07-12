import struct

with open('output', 'rb') as f:
    chunk = f.read(16)
    result = struct.unpack('dicccc', chunk)
    print(result)
