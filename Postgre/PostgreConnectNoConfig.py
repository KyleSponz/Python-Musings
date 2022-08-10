#!/usr/bin/python

#############################################################################################################
# Stripped out the configuration file logic for use when login credentials are managed by some other source #
#############################################################################################################

import psycopg2


def setparams():
    connectionparams = {'host': '192.168.1.211', 'database': 'python musings', 'user': 'kyle', 'password': '1qaz2wsx3#'}
    return connectionparams


def connect():
    connection = None
    try:
        params = setparams()

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
