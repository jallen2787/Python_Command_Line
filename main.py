from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('contacts', user='',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone = BigIntegerField()


db.connect()
db.drop_tables([Contact])
db.create_tables([Contact])

Contact(first_name='Jaline', last_name='Athena', phone=646-966-8125).save()
Contact(first_name='Noah', last_name='Nazir', phone=914-561-6573).save()
Contact(first_name='Geremy', last_name='Rodriguez', phone=203-675-7125).save()

Jaline = Contact.select().where(Contact.first_name == 'Jaline').get()
print(Jaline)

for contact in Contact.select():
    print(contact.first_name)