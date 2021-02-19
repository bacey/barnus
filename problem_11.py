# Tömb, mátrix, array, kétdimenziós tömb:
matrix = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
]

# A csupa nagybetűs változók a konstansok. A konstans "változók" értéke
# nem szokott változni a program futása során.
SOROK_SZAMA = 4
OSZLOPOK_SZAMA = 5


def letezik(sor, oszlop):
    try:
        # Ha egy változó nem érdekes, nem fontos a számunkra, akkor nem adunk neki rendes nevet,
        # csak egy aláhúzást. Az aláhúzással (_) szoktuk azt jelölni, hogy az adott változó
        # nem fontos, hogy az adott változót nem akarjuk később felhasználni:
        _ = matrix[sor][oszlop]

        # Ha a fenti sorban sikeresen be tudtuk olvasni a mátrix sor-oszlopadik elemét
        # egy aláhúzás nevű nem-fontos, lényegtelen változóba,
        # akkor a mátrix sor-oszlopadik eleme létezik, térjünk tehát vissza True-val:
        return True

    except IndexError:
        # Ha a mátrix sor-oszlopadik elemének beolvasása közben hiba (error),
        # más néven kivétel (exception) lépett fel, akkor a mátrix sor-oszlopadik eleme
        # nem létezik, térjünk tehát vissza False-szal:
        return False


for sor in range(SOROK_SZAMA):
    for oszlop in range(OSZLOPOK_SZAMA):
        if letezik(sor, oszlop):
            print(f'matrix[{sor}][{oszlop}] : {matrix[sor][oszlop]}')
        else:
            print(f'matrix[{sor}][{oszlop}] nem letezik')
