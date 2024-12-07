#memanggil file gempa dan import semuan method dan fungsi
from Gempa import *

#membuat objek
gempa1 = Gempa("banten", 1.2)
gempa2 = Gempa("palu", 6.1)
gempa3 = Gempa("cianjur", 5.6)
gempa4 = Gempa("jayapura", 3.3)
gempa5 = Gempa("garut", 4.0)

print("##info Gempa##")
print()
gempa1.dampak()

print("##info Gempa##")
print()
gempa2.dampak()

print("##info Gempa##")
print()
gempa3.dampak()

print("##info Gempa##")
print()
gempa4.dampak()

print("##info Gempa##")
print()
gempa5.dampak()