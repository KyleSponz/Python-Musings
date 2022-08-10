#!/usr/bin/python

##############################################################################################################
# This is the actual connector and uses the config.py file to establish the database connection              #
##############################################################################################################


import psycopg2
from config import config


def connect():
    connection = None
    try:
        params = config()

        print('Connection made to the postgresql database')
        connection = psycopg2.connect(**params)

        var_cur = connection.cursor()

        print('Database version is - ')
        var_cur.execute('SELECT version()')

        version_of_database = var_cur.fetchone()
        print(version_of_database)

        var_cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()

