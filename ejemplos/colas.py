from collections import deque
import time

cola = deque()

cola.append(7)
cola.append(2)
cola.append(8)
cola.append(3)
cola.append(300)

print("cola Actual")
print(cola)

while cola:
    n=cola.popleft()
    print("numero: ", n)
    print("Elementos")
    print(cola)
    time.sleep(2)