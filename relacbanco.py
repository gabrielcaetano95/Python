#!/usr/bin/python3

import psycopg2
from objeto2 import Cliente, Poupanca


try:
    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux') #conexão
    cur = con.cursor() #operador no sql
except Exception as e:
    print("Erro: {}".format(e))
    exit()

cur.execute("select * from conta where id = 4;")

#pessoa = cur.fetchone()
pessoa = cur.fetchone()
cliente3 = Cliente(pessoa[1],pessoa[0],pessoa[2])
print(cliente3.titular,cliente3.nconta,cliente3.valorcc)






# cur.execute("insert into conta(titular, saldocc) values('joao', 7000)")
# con.commit()



cur.close()
con.close()
