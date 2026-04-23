from dao import connection

def consulta_postagens():
    
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        '''
        SELECT 
            *
        FROM
            postagens
        '''
    )

    dados = cursor.fetchall()

    conn.close()

    retorno = {}

    for i in dados:
        retorno[f"{len(retorno)+1}"] = i["nome"]

    return retorno