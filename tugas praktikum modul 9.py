import os
import time
from termcolor import cprint

os.system('cls')

def animasi_bendera():
    lebar = 25 
    kibaran = 2       
    pola_gelombang = [0, 1, 2, 3, 2, 1]

    while True:
        for gerakan in range (len(pola_gelombang)):
            os.system("cls")
            
            for i in range(3):
                gelombang = " " * pola_gelombang[(gerakan + i) % len(pola_gelombang)]
                cprint("│", 'dark_grey', 'on_dark_grey', end='')
                cprint(gelombang + " " + " " * lebar, 'red', 'on_red')

            for i in range(3):
                gelombang = " " * pola_gelombang[(gerakan + kibaran + i) % len(pola_gelombang)]
                cprint("│", 'dark_grey', 'on_dark_grey', end='')
                cprint(gelombang + " " + " " * lebar, 'white', 'on_white')

            for _ in range(8):
                cprint("│", 'dark_grey', 'on_dark_grey')
            

            time.sleep(0.1)

animasi_bendera()
