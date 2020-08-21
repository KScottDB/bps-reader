import bps.asm
import glob

with open(glob.glob("*.bps")[0], "rb") as flashlight:
    with open("out.txt", "wt") as out:
        bps.asm.disassemble(flashlight, out)