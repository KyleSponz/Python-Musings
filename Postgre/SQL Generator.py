import psycopg2
from psycopg2 import sql

def create_table(table_name, nft):
    """ create tables in the PostgreSQL database"""


def create_table(table_name, nft):
    """ create tables in the PostgreSQL database"""
     col_list = [
        {"col_name": "id", "col_type": "serial", "col_constraint": "primary key"},
        {"col_name": "somethingSilly", "col_type": "varchar", "col_constraint": None},
        {"col_name": "somethingCool", "col_type": "varchar", "col_constraint": None}
    ]

    composed_list = []

    for col in col_list:
        col_cmp = []
        col_cmp.append(sql.Identifier(col["col_name"]))
        col_cmp.append(sql.SQL(" "))
        col_cmp.append(sql.SQL(col["col_type"]))
        if col.get("col_constraint"):
            col_cmp.append(sql.SQL(" "))
            col_cmp.append(sql.SQL(col["col_constraint"]))
        composed_list.append(sql.Composed(col_cmp))

    base_sql = sql.SQL(
        "CREATE TABLE IF NOT EXISTS {table} ({fields})"). \
     format(table=sql.Identifier(table_name),
           fields=sql.SQL(",").join(composed_list)
           )

    try:
    # read database configuration
        params = setparams()
    # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
    # create a new cursor
        cur = conn.cursor()
    # execute the INSERT statement TODO remove to run queries
        cur.execute(base_sql)
    # commit the changes to the database
        conn.commit()
    # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
         conn.close()

if __name__ == '__main__':


    create_table("test_node_18")