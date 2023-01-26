from settings import db
from peewee import *


# Define Models
class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField(max_length=50)
    path = CharField()  # max_length=255

    class Meta:
        database = db
        order_by = 'id'


class ThemeModel(BaseModel):
    # parent = ForeignKeyField(model=ThemeModel, field=Model.ThemeModel.id, on_delete='CASCADE')
    class Meta:
        db_table = 'themes'


class ProjectModel(BaseModel):
    git = CharField(null=True)
    git_remote = CharField(null=True)
    parent = ForeignKeyField(model=ThemeModel, field=ThemeModel.id, on_delete='CASCADE')

    class Meta:
        db_table = 'projects'
