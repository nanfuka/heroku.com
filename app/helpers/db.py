import psycopg2
import os
from pprint import pprint


class Database:
    def __init__(self):
        try:
            postgresdb = 'dfdert8uao9scl'
            Host="ec2-54-235-68-3.compute-1.amazonaws.com"
            User="asyxokpadmpxsb"
            Password="bb906ae0286b861205bb135cef3529aa1e2a64abaaf6a79587a6e8d56f155e4f"
            port="5432"

            if os.getenv('env') == "testing":
                postgresdb = 'dfdert8uao9scl'
                Host="ec2-54-235-68-3.compute-1.amazonaws.com"
                User="asyxokpadmpxsb"
                port="5432"

                Password= "bb906ae0286b861205bb135cef3529aa1e2a64abaaf6a79587a6e8d56f155e4f"

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