import xmlrpc.client
from enum import Enum

from pynput.keyboard import Key
from pynput.keyboard import Listener

BARNUS_RASPBERRY_PI_IP = '192.168.0.73'
BARNUS_RASPBERRY_PI = 'raspberrypi'
SERVER_IP = BARNUS_RASPBERRY_PI_IP
# SERVER_IP = 'localhost'

# sudo ufw allow 8000
# sudo ufw status verbose
rpi = xmlrpc.client.ServerProxy(f'http://{SERVER_IP}:8000')


class Color(Enum):
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    LIME = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    SILVER = (192, 192, 192)
    GRAY = (128, 128, 128)
    MAROON = (128, 0, 0)
    OLIVE = (128, 128, 0)
    GREEN = (0, 128, 0)
    PURPLE = (128, 0, 128)
    TEAL = (0, 128, 128)
    NAVY = (0, 0, 128)


def turn_on(pixel, color=Color.WHITE):
    """
    Kigyújt, felgyújt egy lámpát (pixelt).
    :param pixel: Hanyadik lámpát (pixelt) gyújtsa fel.
    0-tól kezdődik a lámpák számozása (angolul "indexelése").
    :param color: Milyen színű legyen a lámpa. Ha a "color" paraméter nélkül hívod meg
    a "turn_on" függvényt, akkor az alapértelmezett szín a fehér lesz.
    """
    rpi.set_brightness(0.1)
    rpi.clear()
    rpi.set_pixel(pixel, *color.value)
    rpi.show()


def is_key(actual_key, expected_key):
    """
    Függvény, ami összehasonlítja, hogy a ténylegesen lenyomott billentyű (=actual_key)
    megegyezik-e a várt (elvárt) billentyűvel (=expected_key-jel).

    :param actual_key: A ténylegesen lenyomott billentyű.
    :param expected_key: A várt (elvárt) billentyű.
    :return: Ha a ténylegesen lenyomott billentyű megegyezik a várt (elvárt) billentyűvel,
    akkor a függvény True-t ad vissza, egyébként False-t.
    """

    # A közönséges, normális billentyűket a "key.char"-ral tudod lekérdezni,
    # pl. "if key.char == 'f'". Tehát a közönséges billentyűknek van ".char" attribútumuk.
    # Ha tehát egy billentyűnek van ".char" attribútuma, akkor az egy közönséges billentyű.
    #
    # A beépített "hasattr()" függvény mondja meg, hogy egy objektumnak (pl. egy billentyűnek)
    # van-e ".char" attribútuma.
    #
    # A "normal_key" az egy Boolean (igaz/hamis értéket tároló) változó.
    # Azt mutatja meg, hogy a lenyomott billentyű közönséges vagy speciális-e.
    normal_key = hasattr(actual_key, 'char')

    # A különleges billentyűknek (pl. Escape, Space, Tab) nincsen ".char" attribútumuk,
    # őket máshogyan kell kezelni, máshogyan kell összehasonlítani.
    # A különleges billentyűket a "keyboard.Key" alatt éred el, pl. "keyboard.Key.esc".
    # A különleges billentyűk teljes listáját itt találod:
    # https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key

    if normal_key:
        return actual_key.char == expected_key
    else:
        return actual_key == expected_key


def handle_key(key):
    """
    Függvény, ami lekezeli (=handle) az adott billentyűt,
    azaz reagál az adott billentyűre.

    :param key: A lenyomott billentyű.
    :return: Alapesetben semmit nem adunk vissza.
    Ha False-t adunk vissza, akkor azzal befejeztetjük a programot.
    """

    # Ez a print() csak a debuggolást segíti. Ki lehet törölni, ha zavar.
    print(f'{key} was pressed.')

    if is_key(key, Key.esc):
        # Ha Escape-et nyomtak le, akkor lépjünk ki a programból.
        # Ha False-t adunk vissza, akkor a program kilép.
        return False
    elif is_key(key, 'f'):
        turn_on(0, Color.BLUE)
    elif is_key(key, 'a'):
        turn_on(3)
        turn_on(2, Color.GREEN)
    else:
        turn_on(1)


with Listener(on_press=handle_key) as listener:
    listener.join()
