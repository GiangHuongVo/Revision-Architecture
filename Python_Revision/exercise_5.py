#Réaliser un programme qui affiche tous les
# nombres pairs jusqu’au nombre saisi par l’utilisateur
num = int(input("Entrer le nombre: "))
print("LE nombre pairs est: ")
for i in range(2, num + 1, 2):
    print(i, end=" ")

print("LE nombre impairs est: ")
for i in range(1, num + 1, 2):
    print(i, end=" ")