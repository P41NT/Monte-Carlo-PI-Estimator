import random
import math

inside = 0

for i in range(0, 1000000):
    x2 = random.random()**2
    y2 = random.random()**2
    if math.sqrt(x2 + y2) < 1.0:
        inside += 1

val = (float(inside)/1000000)*4

print(val)
