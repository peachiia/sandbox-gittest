import numpy as np
x = int(input("Enter the number: "))
a = np.zeros([2,2])
b = (x*5)+1
print("Plus = ", a+b)

a[1][0] = 3
a[0][0] = 2
print("Minus = ", a-b)