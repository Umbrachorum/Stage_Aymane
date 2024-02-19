import json

def generate_card(tuple1 : list) -> list:
    tableau = []
    if tuple1[0] != tuple1[1]:
        print("Les deux valeurs inscrites dans le tuple doivent être égales")
        return
    if type(tuple1[0]) is not int:
        print("Les données doivent être des nombres entiers")
        return
    if tuple1[0] < 10:
        print("Les deux nombres doivent être supérieurs à 10")
        return
    if tuple1[0] * tuple1[1] > 999:
        print("La taille du tableau ne doit pas excéder 999")
        return
    for i in range(tuple1[0]):
        t = []
        for j in range(tuple1[1]):
            t.append("*")
        tableau.append(t)
    return tableau

def fonction_1(tab, bat) -> list:
    liste_bateaux = []
    if len(tab) == 0:
        return -1
    for i in range(len(bat)):
        if len(bat[i][0]) > 0:
            b = fonction_2(bat[i])
        else:
            break
        if int(b[0][0]) - int(b[1][0]) != 0:
            print("Vous ne pouvez pas placer de bateaux en diagonale")
        if int(b[1][2]) - int(b[0][2]) > 5 or int(b[1][2]) - int(b[0][2]) < 2:
            print("La taille d'un bateau doit être comprise entre 2 et 5 cases")
        liste_bateaux.append(b)
    for j in range(int(b[1][2]) - int(b[0][2]) + 1):
        tab[int(b[0][0]) - 1][j] = '#'
    return tab



def fonction_2(bateau : list) -> list:
    if len(bateau) != 2:
        print("Vous devez entrer DEUX valeurs")
        return
    if type(bateau[0][0]) is not str or type(int(bateau[0][1])) is not int or type(bateau[1][0]) is not str or type(int(bateau[1][1])) is not int:
        print("Le format de vos coordonnées est incorrect")
        return
    v = bateau[0][0].upper()
    x = ord(v) - 64
    v2 = bateau[1][0].upper()
    y = ord(v2) - 64
    boat = [str(x) + "-" + bateau[0][1], str(y) + "-" + bateau[1][1]]
    return boat

def print_my_card(my_list: list) -> None:
    for obj in my_list: 
        print(obj)




if __name__ == '__main__':
    temp = input("Veuillez entrer deux nombres définissant la taille de la carte sous la forme d'un tuple")
    temp_buffer_without = temp[1:]
    temp_buffer_without = temp_buffer_without[:-1]
    data1, data2 = temp_buffer_without.split(',')
    temp_arr = [int(data1), int(data2)]
    tab = generate_card(temp_arr)
    print_my_card(tab)
    bat = [["A1", "A5"]]
    temp_bat_array = []
    """ for obj in list(bat): 
        temp_bat_str = obj[1:]
        temp_bat_str = temp_bat_str[:-1]
        temp_bat_str = temp_bat_str.replace(' ', '')
        temp_bat_array.append(temp_bat_str.split(','))"""
    tmp = fonction_1(tab, bat)
    print_my_card(tmp)