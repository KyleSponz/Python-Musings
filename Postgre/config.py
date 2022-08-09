###############################################################################################################
# This is the standard way to implement databases. This file reads the associated .ini file in this repo to   #
# configure the database connection                                                                           #
###############################################################################################################

from configparser import ConfigParser


def config(filename='server_info.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    database = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            database[param[0]] = param[1]

    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return database