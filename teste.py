import middleware.db_middleware as db2

lista=list(db2.get_itens())


for tupla in lista:
    print(tupla)
