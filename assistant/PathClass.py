import os
from settings import BASEDIR
import re


# import yaml


class PathClass:
    def __init__(self):
        self.pth = __file__

    def tree(self):
        tree = []
        pattern_theme = 'type: theme'
        #         tree: str = """
        # Themes          Path                Number of projects
        # ------------------------------------------------------
        # Bash            ~/Projects/BASH     5
        # Books           ~/Projects/BOOKS    1
        # Configs         ~/Projects/CONFIGS  2
        # Python          ~/Projects/PYTHON   50
        #         """
        dirs = os

        with dirs.scandir(BASEDIR) as essences:
            for essence in essences:
                yml_path = essence.path + '/.aaa/.aaa.yml'
                if os.path.exists(yml_path):
                    # print(f'Каталог {essence.name} по пути {essence.path}')

                    with open(yml_path, 'r', encoding='utf=8') as type_of_dir:
                        yml = type_of_dir.read()
                        # print(re.search(pattern_theme, yml))
                        print(yml)
                        tree.append(essence.name)
                        print()

        return tree
