import Mainpack as mp
print(mp.x)
print(mp.mainpackdemo())
print("-------------------")

import Mainpack.Subpack2 as ms2
print(ms2.sub)
print(ms2.subpackdemo2())
print("---------------------")

from Mainpack.Subpack2 import Arith as ar

print(ar.addn(4,5))
print(ar.subn(10,5))