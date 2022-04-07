import sqlite3
from math import *


def functionsqrt(a: float, b: float, c: float):
    res = ''
    if b ** 2 - 4 * a * c < 0:
        res = 'Equation is unsolvable'
        return res
    res = 0
    if b ** 2 - 4 * a * c == 0:
        res = -b / (2 * a)
        return res
    res = []
    if b ** 2 - 4 * a * c > 0:
        x1 = (-b + sqrt(b ** 2 - 4 * a * c) / (2 * a))
        res.append(x1)
        x2 = (-b - sqrt(b ** 2 - 4 * a * c) / (2 * a))
        res.append(x2)
        return res


x = functionsqrt(1, -6, 9)
print(x)

con = sqlite3.connect(r'/home/alberdinamariya/PycharmProjects/petrochem1/db.sqlite3')
cur = con.cursor()

if x == 'Equation is unsolvable':
    x = (x,)
    cur.execute("""INSERT into basicchem_sqrtequation (unpossible) VALUES(?);""", x)
    con.commit()

elif type(x) == list:
    x = tuple(x)
    cur.execute("""INSERT into basicchem_sqrtequation (des_1, des_2) VALUES(?, ?);""", x)
    con.commit()

elif type(x) == float:
    x = (x,)
    cur.execute("""INSERT into basicchem_sqrtequation (des_1) VALUES(?);""", x)
    con.commit()
