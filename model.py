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

def apagar_postagem(id):

    conn = connection()
    cursor = conn.cursor()

    query = '''
            DELETE FROM postagens WHERE id = %s;
            '''

    cursor.execute(query, (id,))

    conn.commit()
    
    conn.close()

def realizar_postagem(id, titulo, resumo, conteudo, autor):
    
    conn = connection()
    cursor = conn.cursor()

    query = '''
        INSERT INTO postagens (id, titulo, resumo, conteudo, autor)
        VALUES (%s, %s, %s, %s, %s)
    '''

    valores = (id, titulo, resumo, conteudo, autor)

    cursor.execute(query, (valores))
     
    conn.commit()
    conn.close()


def editar_postagem(id, titulo, resumo, conteudo, autor):

    conn = connection()
    cursor = conn.cursor()

    query = '''


            '''
    
