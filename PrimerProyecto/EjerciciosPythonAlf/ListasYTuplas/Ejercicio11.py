v1 = [1, 2, 3]
v2 = [-1, 0, 2]
producto_escalar = 0
for i in range(len(v1)):
    producto_escalar += v1[i] * v2[i]
print("El producto escalar de {} y {} es {}".format(v1, v2, producto_escalar))