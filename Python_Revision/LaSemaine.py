def semaine(nombre):
    match nombre:
        case 1:
            print('Lundi')
        case 2:
            print('Mardi')
        case 3:
            print('Mecredi')
        case 4:
            print('Jeudi')
        case 5:
            print('Vendredi')
        case 6:
            print('Samedi')
        case 7:
            print('Dimanche')
        case _:
            print('Pas de résultat trouvé')

nombre = int(input('Entrez le nombre : '))
print(f"Le nombre {nombre} est le {semaine(nombre)}")