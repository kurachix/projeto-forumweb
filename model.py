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

def apagar_postagem(postagem_id):

    conn = connection()
    cursor = conn.cursor()

    query = '''
            DELETE FROM postagens WHERE id = %s;
            '''

    cursor.execute(query, (postagem_id,))

    conn.commit()
    
    conn.close()