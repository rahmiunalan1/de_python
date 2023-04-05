import random

print("Hello World!")

name = "Rahmi"

print("Hello " + name)
print("Hello", name)
print(id(name)) 

for left in range(7):
    for right in range(left,7):
        print(f"[{left}|{right}]", end=" ")
    print()
