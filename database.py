# SQlite DB
# Install peewee
from peewee import *
from os import path
db_connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(db_connection, "eMobilis.db"))

# Proceed to create a table inside the database
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


# Finally execute the table creation logic
User.create_table(fail_silently=True)


class Student(Model):
    name = CharField()
    adm_no = CharField()
    course = CharField()

    class Meta:
        database = db


Student.create_table(fail_silently=True)


class Teacher(Model):
    name = CharField()
    profession = CharField()
    reg_no = CharField(unique=True)

    class Meta:
        database = db


Teacher.create_table(fail_silently=True)


class Hesabu(Model):
    rate = CharField()
    principal = CharField()
    time = CharField()
    width = CharField()
    height = CharField()
    length = CharField()


    class Meta:
        database = db


Teacher.create_table(fail_silently=True)



