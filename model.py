from dao import connection

def consulta_postagens():
    
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            '''
            SELECT 
                id,
                titulo,
                resumo,
                conteudo,
                autor
            FROM
                postagens
            ORDER BY
                id ASC
            '''
        )

        return cursor.fetchall()
    finally:
        conn.close()

def apagar_postagem(id):

    conn = connection()
    cursor = conn.cursor()

    try:
        query = '''
                DELETE FROM postagens WHERE id = %s;
                '''

        cursor.execute(query, (id,))

        conn.commit()
    finally:
        conn.close()

def realizar_postagem(id, titulo, resumo, conteudo, autor):
    
    conn = connection()
    cursor = conn.cursor()

    try:
        query = '''
            INSERT INTO postagens (id, titulo, resumo, conteudo, autor)
            VALUES (%s, %s, %s, %s, %s)
        '''

        valores = (id, titulo, resumo, conteudo, autor)

        cursor.execute(query, valores)

        conn.commit()
    finally:
        conn.close()


def editar_postagem(id, titulo, resumo, conteudo, autor):
    conn = connection()
    cursor = conn.cursor()

    try:
        query = '''
            UPDATE postagens
            SET titulo = %s,
                resumo = %s,
                conteudo = %s,
                autor = %s
            WHERE id = %s
        '''

        valores = (titulo, resumo, conteudo, autor, id)

        cursor.execute(query, valores)

        conn.commit()
    finally:
        conn.close()
