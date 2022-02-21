import os
import time

if os.name == "posix":
    var = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"

time.sleep(2)

os.system(var)
print("*********************")
print("*                   *")
print("*       Hola        *")
print("*                   *")
print("*********************")

time.sleep(2)
os.system(var)

print("*********************")
print("*                   *")
print("*     Me  llamo     *")
print("*                   *")
print("*********************")

time.sleep(2)
os.system(var)

print("*********************")
print("*                   *")
print("*       Angel       *")
print("*                   *")
print("*********************")

time.sleep(2)
