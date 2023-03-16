import zlib

sin = "hello world!hello world!hello world!hello world!"
cin = zlib.compress(sin.encode())
print(cin)
din = zlib.decompress(cin).decode()
print(din)
