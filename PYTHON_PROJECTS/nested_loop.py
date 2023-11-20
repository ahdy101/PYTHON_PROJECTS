import time
start=time.time()

for i in range(10):
    for j in range(100):
        print(0, end="")
    print()

print(round(time.time() - start), 2)