from peewee import *


db = SqliteDatabase('users.db')


class User(Model):
    telegram_id = CharField(unique=True)

    class Meta:
        database = db


if __name__ == '__main__':
    User.create_table()
