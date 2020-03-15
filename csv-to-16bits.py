
file = open("oldcrap-data.csv", "r") 
out = open("oldcrap-data.bin", "wb");
lines = file.readlines()
for line in lines:
    line = line.strip("\n")
    xy = line.split(";")
    x = xy[0]
    y = xy[1]
    print(x, y)
    out.write(int(x).to_bytes(2, byteorder="little"))
    out.write(int(y).to_bytes(2, byteorder="little"))
file.close()
out.close()
