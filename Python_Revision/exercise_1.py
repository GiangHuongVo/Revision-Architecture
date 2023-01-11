# La fonction de convertir de cm en mettre
def covertirEnMettre (nombre):
    return nombre/100

nCm = float(input("Saisit un nombre de centimet: "))
print(f"{nCm}cm = {covertirEnMettre(nCm)}m")
