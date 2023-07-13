
with open("pokemon_list.txt", "r") as f:
    pokemon_lista = f.readlines()
    
pokemon_lista = [elemento.strip('\n') for elemento in pokemon_lista]


def validate(name, p_l = pokemon_lista):
    pass

if __name__ == '__main__':
    name = input('nombre: ')
    print(validate(name))
