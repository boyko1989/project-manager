import os
import yaml
from settings import BASEDIR


class Indexator:
    """"""
    def __init__(self):
        self.pth = __file__

    def __dir_travel(self, type_of_search):
        """Шаблонный метод обхода по каталогам
        """
        tree = {}

        dirs = os.walk(BASEDIR, topdown=True, onerror=None, followlinks=False)
        for item in dirs:
            path_to_dir = item[0]
            yml_path = path_to_dir + '/.aaa/.aaa.yml'
            isExclude = ('.git' in item[0]) or ('node_modules' in item[0])
            if isExclude:
                continue
            if os.path.exists(yml_path):
                with open(yml_path) as type_of_dir:
                    yml = yaml.safe_load(type_of_dir)
                    if yml['type'] == type_of_search:
                        tree[path_to_dir.split('/').pop()] = path_to_dir

        return tree

    def ls_of_themes(self):
        tree = self.__dir_travel('theme')

        return tree

    def ls_of_projects(self):
        tree = self.__dir_travel('project')

        return tree
