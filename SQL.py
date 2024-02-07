import pymysql
import pandas as pd


# 조회할 MySQL 데이터베이스에 맞게 변경하셔야 합니다.
# You will need to change informations below for your MySQL database

RDS_USERNAME='ENTER YOUR ID'                    # ID
RDS_PASSWORD='ENTER YOUR PASSWORD'              # Password
RDS_DATABASE='ENTER YOUR DATABASE NAME'         # Database Name
RDS_HOST='ENTER YOUR DATABASE HOST URL'         # Host url
RDS_DIALECT='mysql'                             
RDS_PORT=3306                                   # Port No. 



def connect_RDS():
    try:
        host = RDS_HOST
        port = 3306
        username = RDS_USERNAME
        password = RDS_PASSWORD
        database = RDS_DATABASE
        conn = pymysql.Connect(user=username, password=password, host=host, port=port, database=database,
                                use_unicode = True, charset='utf8mb4')
    except Exception as exc:
        print(f'RDS Connection Failure : {exc.__str__()}')
    return conn


def get_sqldata(query): # convert sql format to pd.DataFrame
    conn = connect_RDS()
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        columns = [x[0] for x in cursor.description]
        db_data = pd.DataFrame(result, columns=columns)
    
    conn.close()
    return db_data

class SqlQuery:
    @staticmethod 
    def sample_query():   # Write a query statement referring to the example. Query must be write as a doctstring format
        return '''
            SELECT
                id,
                name,
                phonenumber
            FROM user_table as users
            LEFT JOIN prescription_data as pd
                ON users.id = pd.user_id
            WHERE
                phonenumber IS NOT NULL
            ORDER BY
                name DESC,
                phonenumber ASC;
                '''