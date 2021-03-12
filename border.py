lista = [0, 1, 2, 2, 3]


def border1(border):
    index = lista.index(border)
    return lista[index:]


def border2(border):
    new_list = []
    item_found = False
    for item in lista:
        if item == border:
            item_found = True
        if item_found:
            new_list.append(item)

    return new_list

print(border1(2))
print(border2(2))
