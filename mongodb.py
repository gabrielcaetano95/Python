#!/usr/bin/python3
..
from pymongo import MongoClient
f.rom pprint import pprint

try:
    con = MongoClient('mongodb://userchat:4linux@192.168.202.113/projeto') #string de conexão
    db = con['projeto'] #dbase
except Exception as e:
    print("Falha de conexao")
    exit()

db.conta.update({'_ID':2.0}, {"$set":{"titular":"Gabriela Valle de Castro Madeira"}})
# for registro in db.conta.find():
#     print(registro)

busca = [x for x in db.conta.find()]
print(busca[0]['titular'])

