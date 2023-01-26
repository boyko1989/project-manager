from Models import *

# Core Functionality
with db:
    db.create_tables([ThemeModel, ProjectModel])

print('Done')
