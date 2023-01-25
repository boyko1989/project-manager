import os
import yaml
from settings import BASEDIR


class PathClass:
    def __init__(self):
        self.pth = __file__

    def ls_of_themes(self):
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
                    if yml['type'] == 'theme':
                        tree[path_to_dir.split('/').pop()] = path_to_dir

        return tree
