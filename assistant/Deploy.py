import os
import subprocess
from settings import BASEDIR
from assistant.Indexator import Indexator as Index
from assistant.Array_functions import Array_functions as pthc  # path cleaner


class Deploy:
    """Класс для копирования всего каталога проектов

    1. Класс должен определить все удалённые репозитории
    2. Должен иметь связь с облачным хранилищем
    3. Определить тактику для резервирования всех каталогов и отдельных файлов
    4. Уметь реализовать перенос
    """

    def get_remote_rep(self, yml_path, **kwargs):
        """Получает удалённые репозитории в конкретном каталоге"""
        dict_of_remote = {}
        path = pthc.aaa_del(yml_path)

        path_git = path + '/.git'

        if os.path.exists(path_git):
            os.chdir(path)
            base_path = os.path.join(BASEDIR, 'AAA')
            os.chdir(base_path)
            item_remote_path = subprocess.check_output(['git', 'remote', '-v']) \
                .decode(encoding='utf-8') \
                .split('\n')[1] \
                .split('\t')[1] \
                .split(' ')[0]

            dict_of_remote[path] = item_remote_path

        return dict_of_remote

    def git_searcher(self):
        pass

    def git_remote_search(self, path):
        """Возвращаем словарь с удалёнными репозиториями Git"""
        git_remote_searcher = Index()
        dict4def = {'key': 'Hello World!'}
        dict_of_remote = git_remote_searcher.dir_travel(self.get_remote_rep, dict4def)
        # print(dict_of_remote)

        return dict_of_remote
