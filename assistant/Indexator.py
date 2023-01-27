import os
import yaml
import random
import hashlib
from settings import BASEDIR


class Indexator:
    """"""

    def __init__(self):
        self.pth = __file__

    def dir_travel(self, callback, kwargs={}):
        """Метод обхода по каталогам
        Задача просто открыть файл .aaa.yml и передать значение требуемого поля

        Сделать именованные параметры, в соответствии с которыми будет вызываться тот или иной метод
        """
        tree = {}

        dirs = os.walk(BASEDIR, topdown=True, onerror=None, followlinks=False)
        for item in dirs:

            isExclude = ('.git' in item[0]) or ('node_modules' in item[0])
            if isExclude:
                continue
            path_to_dir = item[0]
            yml_path = path_to_dir + '/.aaa/.aaa.yml'

            if os.path.exists(yml_path):

                # !!! Вызов коллбэка !!!
                dict_back = callback(yml_path, **kwargs)

                # TODO в дальнейшем сделать метод универсальным на return
                # Сделать проверку на то, что возвращает callback
                # Словари и списки обрабатывать разными способами
                if len(dict_back) != 0:
                    dict_value = list(dict_back.values())[0]
                    dict_key = list(dict_back.keys())[0]
                    tree[dict_key] = dict_value

        return tree

    def test_callback(self, yml_path, **kwargs):
        for kwarg in kwargs.items():
            print(kwarg)
            print()

    def fild_search(self, yml_path, **kwargs):
        dict_back = {}
        # print(kwargs['type_fild'])
        # print(kwargs.items())
        with open(yml_path) as yml_file:
            yml = yaml.safe_load(yml_file)
            if yml[kwargs['type_fild']] == kwargs['type_of_search']:
                essent_path = yml_path.split('/')

                del essent_path[-1]
                del essent_path[-1]

                essent_path = '/'.join(essent_path)
                dict_back[yml['name']] = essent_path

        return dict_back

    def values_search(self, yml_path, **kwargs):
        """Метод должен возвращать список уникальных значений по ключам

        Например, если нужно узнать список всех тем или список всех проектов

        """
        dict_back = {}
        with open(yml_path) as yml_file:
            yml = yaml.safe_load(yml_file)

            # создание случайного ключа
            head = random.randint(1, 10000000000)
            tail = random.randint(1, 10000000000)
            key = hashlib.md5(str(head + tail).encode()).hexdigest()
            dict_back[key] = yml[kwargs['type_fild']]

        return dict_back


if __name__ == '__main__':
    pass
