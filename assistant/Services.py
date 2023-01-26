from Models import *

# Core Functionality
with db:
    # parent = ThemeModel.select()

    # parent = ThemeModel.select().where(ThemeModel.name == 'root')
    # print(parent[0])

    parent_id = ThemeModel.get(ThemeModel.name == 'root')
    print(parent_id)

    # parent = ThemeModel.get('id')
    # projects = [
    #     {'name': 'AAA', 'path': '/home/p_boyko/Projects/AAA', 'git': 'IS', 'git_remote':'git@github.com:boyko1989/project-manager.git', 'parent':4},
    # ]
    # ProjectModel.insert_many(projects).execute()

print('Done')

