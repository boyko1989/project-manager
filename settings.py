from pathlib import Path
from peewee import *
import datetime

BASEDIR = Path(__file__).resolve().parent.parent

# Set DataBase
db = SqliteDatabase("db/database.sqlite")
