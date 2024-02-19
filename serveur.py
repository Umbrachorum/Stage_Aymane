import sys

def generate_card(tuple1 : list) -> list:
    tableau = []
    print(type(tuple1[0]) == int)
    if tuple1[0] != tuple1[1]:
        print("Les deux valeurs inscrites dans le tuple doivent être égales")
        return
    if type(tuple1[0]) is not int:
        print("Les données doivent être des nombres entiers")
        return
    if tuple1[0] < 10:
        print("Les deux nombres doivent être supérieurs à 10")
        return
    for i in range(tuple1[0]):
        t = []
        for j in range(tuple1[1]):
            t.append("*")
        tableau.append(t)
    return tableau

if __name__ == '__main__':
   tmp = generate_card([10,10])
   print(tmp)