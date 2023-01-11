numbers = int(input("Entrer le nombre: "))
print(f"Le nombre est: ")
for i in range(1, numbers+1):
    print(i, end=" ")

print()
num = int(input("Entrer le nombre: "))
print("LE nombre inverse est: ")
for i in range(num, 0, -1):
    print(i, end=" ")