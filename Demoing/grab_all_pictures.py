import os
import glob
from subprocess import call

folders = glob.glob("*")

real = []
for i in folders:
    if not ".py" in i:
        if not ".txt" in i:
            if not "Base" in i:
                real.append(i)

for i in real:
    os.chdir(i)
    call(['python','picture_grab.py'])
    os.chdir("../")
