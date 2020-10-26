#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici
def diff_btw_2(fichier_1,fichier_2) -> bool:
    with open(fichier_1,'r') as f_1, open(fichier_2,'r') as f_2:
        same = True
        while same:
            char_1 = f_1.read()
            char_2 = f_2.read()
            same = char_1 == char_2
        return -1 if  same else f_1.tell()
def change(paste):
    with open(paste,'r') as f, open('text.txt','x') as f_1:
        char_paste = f.read()
        new_text = char_paste.replace(' ','   ')
        f_1.write(new_text)
    return None
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    # print(diff_btw_2('exemple.txt','exemple_1.txt'))
    print(change('exemple.txt'))
