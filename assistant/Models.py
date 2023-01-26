from peewee import *
from datetime import date

connection = SqliteDatabase('myprojects.sqlite')


# cursor = connection.cursor()

class Test(Model):
    title_of_record = CharField()
    date_of_record = DateField()

    class Meta:
        database = connection


class Dependent(Model):
    owner = ForeignKeyField(Test, related_name='depend')
    name = CharField()
    recorde_type = CharField()

    class Meta:
        database = connection


connection.connect()
# connection.create_tables([Test, Dependent])

# first record
# first_test = Test(title_of_record='My First record from ORM', date_of_record=date(1960, 1, 15), is_relative=True)
# first_test.save()

# # next expr
# second_test = Test.create(title_of_record='New record in SQLite', date_of_record=date.today(), is_relative=True)
#
# # record update
# second_test.name = 'Update of record from ORM'
# second_test.save()

# first_test_dep = Dependent.create(owner=1, name='Depend record', recorde_type='New record')

connection.close()
