import psycopg2
import os
from pprint import pprint


class Database:
    def __init__(self):
        try:
            postgresdb = 'fresh'
            Host="localhost"
            User="postgres"
            Password="test"

            if os.getenv('env') == "testing":
                postgresdb = 'freshs'
                Host="localhost"
                User="postgres"
                Password= "test"

            self.connection = psycopg2.connect(
                    database=postgresdb, host=Host, user=User,
                    password=Password, port="5432"
                )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint('cannot connect to database')

    def create_tables(self):
        tables = (
            """
                CREATE TABLE IF NOT EXISTS user_table4(
                    ID SERIAL PRIMARY KEY NOT NULL,
                    firstname VARCHAR(20) NOT NULL,
                    lastname VARCHAR(20) NOT NULL
                );
            """
        )
        self.cursor.execute(tables)

    def add_user(self, firstname, lastname):
        insert = f"""INSERT INTO user_table4(
            firstname, lastname) VALUES (
            '{firstname}',
            '{lastname}');"""
        self.cursor.execute(insert)
if __name__ == '__main__':
    db_name = Database()
    db_name.create_tables()