import logging
import psycopg2
from db import dataBaseConfig
import psycopg2.extras

def getCursorSgp():
    con = psycopg2.connect(dbname=dataBaseConfig.DB_NAME, user=dataBaseConfig.DB_USER, password=dataBaseConfig.DB_PASS, host=dataBaseConfig.DB_HOST)
    logging.debug("Conectada BD local")
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return cur