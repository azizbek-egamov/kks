import psycopg2

def sql_connect():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="15995",
            host="localhost",
            database="kinobot"
        )
        connection.commit()

        return True
    except (Exception, psycopg2.Error):
        return False
    
def sql_connection():
    connection = psycopg2.connect(
        user="postgres",
        password="15995",
        host="localhost",
        database="kinobot"
    )
    connection.commit()

    return connection

def create_table():
    if sql_connect() == True:
        conn = sql_connection()
        cursor = conn.cursor()
        create_table = """CREATE TABLE kinolar(
            code  SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            info TEXT NOT NULL,
            url TEXT NOT NULL
        );
        """
        cursor.execute(create_table)
        conn.commit()
    else:
        print("Bazaga ulanishda xatolik yuz berdi")        
                                
def add_information(name, info, url):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()
            
            insert_query = """ INSERT INTO kinolar (name, info, url) VALUES (%s, %s, %s) """
            
            cursor.execute(insert_query, (name, info, url))
            conn.commit()
            return True
        except:
            return False
    else:
        return False
                
def kino_info(id, v):
    if sql_connect() == True:
        conn = sql_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM kinolar WHERE {v} = %s", (id,))
        
        res = cursor.fetchall()
        conn.commit()
        if not res:
            return False
        else:
            for i in res:
                return list(i)
    else:
        return False
    
print(kino_info("10", "code"))
    
def delete(keys):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()
            cursor.execute("delete from kinolar where code = %s", (keys,))
            conn.commit()
            return True
        except:
            return False
    else:
        return False