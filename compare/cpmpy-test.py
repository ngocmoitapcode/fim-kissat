#pip install python-sat
#pip install cpmpy

import numpy as np
from cpmpy import *

# TDB = np.array(
#       [[False, True, False, False, False],
#        [False, False, False, False, True],
#        [True, False, True, False, False],
#        [True, False, False, False, True],
#        [False, True, True, False, False],
#        [False, False, False, True, True],
#        [False, False, True, True, True],
#        [True, True, True, False, False],
#        [True, True, False, False, True],
#        [True, True, True, False, True]])
def generate_TDB_from_input(input_file):
    TDB = []
    with open(input_file) as f:
        for line in f:
            TDB.append([bool(int(x)) for x in line.split()])
    f.close()
    return np.array(TDB)
TDB = generate_TDB_from_input("input/converted_data.txt")
nrT, nrI = TDB.shape
freq=4

Items = boolvar(shape=nrI, name="items")
Trans = boolvar(shape=nrT, name="transactions")

m = Model()
#m += [Trans[t] == (~any(Items[i] for i in range(nrI) if not TDB[t,i]))
#      for t in range(nrT)]
# same as above but with numpy magic
for T, negrow in zip(Trans, ~TDB):
    m += T == ~any(Items[np.where(negrow)])

m += (sum(Trans) >= freq)
# The potentially more effective version of the above:
# That this does not work is a bug in the CPMpy PySAT translation
#for I, col in zip(Items, TDB.T):
#    m += I.implies(sum(Trans[np.where(col)] >= freq))

print(m)

stdCounter=m.solveAll(solver='ortools', display=lambda: print(Items.value(), Trans.value()))
print(stdCounter)