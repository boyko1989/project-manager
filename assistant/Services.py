from Models import *

# Core Functionality
with db:
    # db.create_tables([ThemeModel, ProjectModel])
    python = ThemeModel(name='Python', path='/home/p_boyko/Projects/PYTHON').save()
    bash = ThemeModel.create(name='Bash', path='/home/p_boyko/Projects/BASH')
    network = ThemeModel.insert(name='Network', path='/home/p_boyko/Projects/NETWORK').execute()

print('Done')
