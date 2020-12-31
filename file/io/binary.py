with open("binary", 'bw') as binary_file:
    binary_file.write(bytes(range(17)))

with open("binary", 'br') as bin_file:
    for b in bin_file:
        print(b)

a = 65534
b = 65535
c = 65536
x = 2998302

with open("binary2", 'bw') as binary_file2:
    binary_file2.write(a.to_bytes(2, "big"))
    binary_file2.write(b.to_bytes(2, "big"))
    binary_file2.write(c.to_bytes(4, "big"))
    binary_file2.write(x.to_bytes(4, "big"))
    binary_file2.write(x.to_bytes(4, "little"))

with open("binary2", 'br') as binary_file2:
    e = int.from_bytes(binary_file2.read(2), "big")
    print(e)
    f = int.from_bytes(binary_file2.read(2), "big")
    print(f)
    g = int.from_bytes(binary_file2.read(4), "big")
    print(g)
    h = int.from_bytes(binary_file2.read(4), "big")
    print(h)
    i = int.from_bytes(binary_file2.read(4), "big")
    print(i)
