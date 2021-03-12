import datetime
import arrow


def extract_date_from_message(message):
    now = datetime.datetime.now()

    numbers = [int(word) for word in message.split() if word.isdigit()]

    # numbers == [24, 12, 2021]
    if len(numbers) == 3:
        pass  # pass == do nothing

    # numbers == [24, 12]
    elif len(numbers) == 2:
        numbers.append(now.year)
        # numbers == [24, 12, 2021]

    # numbers == [24]
    elif len(numbers) == 1:
        numbers.append(now.month)
        numbers.append(now.year)
        # numbers == [24, 12, 2021]

    else:  # if len(numbers) == 0 or len(numbers) > 3:
        numbers = [now.day, now.month, now.year]
        # numbers == [24, 12, 2021]

    numbers.reverse()
    # numbers == [2021, 12, 24]

    return numbers


def teszt1():
    now = datetime.datetime.now()

    assert extract_date_from_message('!mi lesz ekkor: 3') == [now.year, now.month, 3]
    assert extract_date_from_message('+mi_lesz ekkor: 3 11') == [now.year, 11, 3]
    assert extract_date_from_message('+mi_lesz_ekkor: 3 11 2019') == [2019, 11, 3]
    assert extract_date_from_message('@mi_lesz ekkor') == [now.year, now.month, now.day]
    assert extract_date_from_message('@mi_lesz_ekkor 22 3 11 19 2019') == [now.year, now.month, now.day]
    assert extract_date_from_message('+mi_lesz_ekkor: 3 furcsa 11 input 2019 ez') == [2019, 11, 3]

    # Kb. így kell majd használnod:
    message_content = '@mi_lesz_ekkor 18 12'
    datumok_listaja1 = extract_date_from_message(message_content)
    # A csillagot ne felejtsd el a datumok_listaja1 elott! A magyarázatot lásd lentebb,
    # a teszt2() függvényben.
    datum1 = arrow.get(*datumok_listaja1)
    datum1_szovegkent = str(datum1)
    assert datum1_szovegkent == '2021-12-18T00:00:00+00:00'

    datumok_listaja2 = extract_date_from_message('!@mi lesz_ekkor: 19')
    datum2 = arrow.get(*datumok_listaja2)
    datum2_szovegkent = str(datum2)
    assert datum2_szovegkent == '2021-03-19T00:00:00+00:00'


def teszt2():

    def fuggveny_ami_ket_parametert_var(elso_parameter, masodik_parameter):
        return elso_parameter + masodik_parameter

    def fuggveny_ami_egy_darab_listat_var(lista):
        lista.reverse()
        return lista

    assert fuggveny_ami_ket_parametert_var(1, 2) == 3

    szamok_listaja = [1, 2]
    assert fuggveny_ami_egy_darab_listat_var(szamok_listaja) == [2, 1]

    assert fuggveny_ami_egy_darab_listat_var([1, 2]) == [2, 1]

    # Normális esetben a "fuggveny_ami_ket_parametert_var" csak akkor működik,
    # ha két paramétert adsz neki:
    assert fuggveny_ami_ket_parametert_var(1, 2) == 3

    # Ha a két paramétered viszont egy listába van becsomagolva,
    # akkor egy csillagot kell tenned a lista paraméter neve elé
    # (tehát *szamok_listaja). A csillag ugyanis "szétrobbantja"
    # a listát az elemeire és a "szétrobbantott" elemeket
    # adja át a függvénynek:
    szamok_listaja = [1, 2]
    assert fuggveny_ami_ket_parametert_var(*szamok_listaja) == 3

    # Ha nem robbantottuk volna szét a listát az elemeire, akkor hibát kapnánk.
    #
    # Ez tehát nem megy:
    #   fuggveny_ami_ket_parametert_var(szamok_listaja)
    #
    # Ez viszont megy:
    #   fuggveny_ami_ket_parametert_var(*szamok_listaja)


teszt1()
teszt2()
