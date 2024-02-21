import json

bateaux_positions = []

def indexation(val : int) -> list :
    tableau = []
    k = 0
    m = 0
    x =0
    for j in range(26):
        if j < val:
            x = j + 65
            tableau.append(chr(x))
        else :
            tableau.insert(0, " ")
            tableau.pop(-1)
            return tableau
    while k <= 26 and len(tableau) < val:
        for l in range(27):
            if len(tableau) >= val:
                tableau.insert(0, " ")
                tableau.pop(-1)
                return tableau
            x = 65 + k
            z = chr(x)
            chaine = z + str(l)
            tableau.append(chaine)
        k = k + 1
        if k > 26:
            while m <= 26 and len(tableau) < val:
                    for n in range(27):
                        if len(tableau) >= val:
                            tableau.insert(0, " ")
                            tableau.pop(-1)
                            return tableau
                        x = 65 + m
                        y = chr(x)
                        y = y + y
                        chaine2 = y + str(n)
                        tableau.append(chaine2)
                    m = m + 1
    tableau.insert(0, " ")
    tableau.pop(-1)
    return tableau

def generate_card(tuple1 : list) -> list:
    print(tuple1[0], tuple1[1])
    carte = []
    if tuple1[0] != tuple1[1]:
        print("Les deux valeurs inscrites dans le tuple doivent être égales")
        return
    if type(tuple1[0]) is not int:
        print("Les données doivent être des nombres entiers")
        return
    if tuple1[0] < 10:
        print("Les deux nombres doivent être supérieurs à 10")
        return
    if tuple1[0] > 999:
        print("La taille du tableau ne doit pas excéder 999")
        return
    for i in range(tuple1[0]):
        t = []
        for j in range(tuple1[1]):
            t.append("*")
        t.insert(0, i+1)
        t.pop(-1)
        carte.append(t)
    return carte

"""def fonction_1(carte : list, bat : list) -> list:
    liste_bateaux = []
        liste_bateaux.append(b)
    if int(b[i][0][0]) == int(b[i][-1][0]):
        for j in range(int(b[i][1][2]) - int(b[i][0][2]) + 1):
            if carte[int(b[i][0][0]) - 1][j+1] != '#':
                carte[int(b[i][0][0]) - 1][j+1] = '#'
            else:
                print("Vous ne pouvez pas placer de bateaux à cet endroit ci")
                return -1
    elif int(b[i][0][2]) == int(b[i][1][2]):
        for k in range(int(b[i][1][0]) - int(b[i][0][0]) + 1):
            if carte[k][int(b[i][0][2]) - 1] != "#":
                carte[k][int(b[i][0][2]) - 1] = "#"
            else:
                print("Vous ne pouvez pas placer de bateaux à cet endroit ci")
                return -1

    return carte"""

def placement_bateaux_suite(carte : list, bat : list) -> list:
    tmp = []
    for bateau in bat:
        tmp.append(command_separator(bateau, carte))
        bateaux_positions.append(tmp[-1])
        #fonction_1(carte, bateau)
        #print(bateau)
        for coord in tmp: 
            write_coord_in_card(coord, carte)
    """for obj in tmp:
        print(tmp)"""
    return carte

def write_coord_in_card(list_coord_single_boat: str, carte: list):
    coord_begin, coord_end = list_coord_single_boat.split(',')
    abs_begin, ord_begin = coord_begin.split("-")
    abs_end, ord_end = coord_end.split("-")
    if len(list_coord_single_boat) < 6:
        print("Vous devez entrer DEUX valeurs")
        return
    for i in range(len(list_coord_single_boat)):
        if i > 11:
            print("Ces coordonnées n\'existent pas")
            return -1
    if type(list_coord_single_boat[0]) is not str or type(int(list_coord_single_boat[-1])) is not int:
        print("Ces coordonnées sont impossibles")
    if abs_begin != abs_end and ord_begin != ord_end:
        print("Vous ne pouvez pas placer de bateaux en diagonale")
    if ord_begin.isdigit() and ord_end.isdigit() and abs_begin.isdigit() and abs_end.isdigit() :
        if(abs(int(abs_begin) - int(abs_end)) < 2 or abs(int(abs_begin) - int(abs_end)) > 5 
           or abs(int(ord_begin) - int(ord_end)) < 2 or abs(int(abs_begin) - int(abs_end)) > 5):
            print("La taille d'un bateau doit être comprise entre 3 et 5 cases")
        if ord_begin == ord_end:
            if int(abs_begin) < int(abs_end):
                for i in range(int(abs_end) - int(abs_begin) + 1):
                    if carte[int(ord_begin)][int(abs_begin) + i] == "#":
                        return -1
                for i in range(int(abs_end) - int(abs_begin) + 1):
                    carte[int(ord_begin)][int(abs_begin) + i] = "#"
            else:
                for i in range(int(abs_begin) - int(abs_end) + 1):
                    if carte[int(ord_begin)][int(abs_begin) - i] == "#":
                        return -1
                for i in range(int(abs_begin) - int(abs_end) + 1):
                    carte[int(ord_begin)][int(abs_begin) - i] = "#"
        elif abs_begin == abs_end:
            if int(ord_begin) < int(ord_end):
                for i in range(int(ord_end) - int(ord_begin) + 1):
                    if carte[int(ord_begin) + i][int(abs_begin)] == "#":
                        return -1
                for i in range(int(ord_end) - int(ord_begin) + 1):
                    carte[int(ord_begin) + i][int(abs_begin)] = "#"
            else:
                for i in range(int(ord_begin) - int(ord_end) + 1):
                    if carte[int(ord_end) - i][int(abs_begin)] == "#":
                        return -1
                for i in range(int(ord_begin) - int(ord_end) + 1):
                    carte[int(ord_end) - i][int(abs_begin)] = "#"
    return carte


def command_separator(post: list, carte: list) -> str :
        #post = ["AA1, 1",  "AA1, 5"] == a la position dans la carte 
        if post[0].find(',') and post[1].find(','):
            abs_bat_begin, oord_bat_begin  = post[0].split(',') #     abs_bat_begin = AA1 && oord_bat_begin = "1"
            abs_bat_end, oord_bat_end = post[1].split(',') #          abs_bat_end = AA1 && oord_bat_end = "5"
        buffer: str = ""
        abs_bat_begin.replace(" ", "")
        abs_bat_end.replace(" ", "")
        for pos in carte[0]:         
            if abs_bat_begin == pos:
                int_pos : int = carte[0].index(abs_bat_begin)
                buffer = buffer + str(int_pos) + "-" + str(oord_bat_begin).replace(' ', '') 
            if abs_bat_end == pos:
                int_pos2 : int = carte[0].index(abs_bat_end)
                buffer = buffer + "," + str(int_pos2) + "-" + str(oord_bat_end).replace(' ', '')
        return buffer


def tirs(x: int,y :int , carte :list) -> bool:
    if x > len(carte[y]):
        return False
    if y > len(carte):
        return False
    if carte[y][x] == "#":
        carte[y][x] = "X"
        return True
    else:
        carte[y][x] = "O"
        return False

def est_coule(carte : list) -> bool:
    for bateau in bateaux_positions:
        coord_begin, coord_end = bateau.split(',')
        abs_begin, ord_begin = coord_begin.split("-")
        abs_end, ord_end = coord_end.split("-")
        if ord_begin == ord_end:
                if int(abs_begin) < int(abs_end):
                    for i in range(int(abs_end) - int(abs_begin) + 1):
                        if carte[int(ord_begin)][int(abs_begin) + i] != "X":
                            return False
                else:
                    for i in range(int(abs_begin) - int(abs_end) + 1):
                        if carte[int(ord_begin)][int(abs_begin) - i] != "X":
                            return False
        elif abs_begin == abs_end:
                if int(ord_begin) < int(ord_end):
                    for i in range(int(ord_end) - int(ord_begin) + 1):
                        if carte[int(ord_begin) + i][int(abs_begin)] != "X":
                            return False
                else:
                    for i in range(int(ord_begin) - int(ord_end) + 1):
                        if carte[int(ord_end) - i][int(abs_begin)] != "X":
                            return False
        return True
 
def print_my_card(my_list: list) -> None:
    for obj in my_list: 
        print(obj)

def simple_print(game: list):
    for obj in game:
        for char in obj:
            print('{:<5s}'.format(str(char)), end="")
        print("")


#point d'entrée du processus
"""if __name__ == '__main__':
    temp = input("Veuillez entrer deux nombres définissant la taille de la carte sous la forme d'un tuple")
    temp_buffer_without = temp[1:]
    temp_buffer_without = temp_buffer_without[:-1]
    data1, data2 = temp_buffer_without.split(',')
    temp_arr = [int(data1), int(data2)]
    tab = generate_card(temp_arr)
    #bat = [["A, 1", "A, 5"], ["B1", "B4"], ["C4", "C6"], ["C1", "C3"], ["A4", "D4"], ["AA1, 1",  "AA1, 5"]]
    bat = [["A, 1", "A, 5"], ["C, 1", "E, 1"], ["W, 10", "W, 13"]]
    temp_bat_array = []
    tab.insert(0, indexation(temp_arr[0]))
    tmp = placement_bateaux_suite(tab, bat)
    simple_print(tmp)
    state = tirs(1, 1, tmp)
    state = tirs(1, 2, tmp) 
    state = tirs(1, 3, tmp) 
    state = tirs(1, 4, tmp) 
    state = tirs(1, 5, tmp) 
    if state == True :
        print("Touché")
    else: 
        print("Raté...")   
    simple_print(tmp)
    if est_coule(tmp):
        print("Coulé")
    else:
        print("Dommage...")"""