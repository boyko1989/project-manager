import os
import yaml
from settings import BASEDIR


class PathClass:
    def __init__(self):
        self.pth = __file__

    def ls_of_themes(self):
        tree = []
        dirs = os

        with dirs.scandir(BASEDIR) as essences:
            for essence in essences:                 # essence.name, essence.path
                yml_path = essence.path + '/.aaa/.aaa.yml'
                if os.path.exists(yml_path):

                    with open(yml_path) as type_of_dir:
                        yml = yaml.safe_load(type_of_dir)

                        if yml['type'] == 'theme':
                            tree.append(essence)

        return tree
