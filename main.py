from assistant.Indexator import Indexator as path_handler
from assistant.Viewer import Viewer as view
from assistant.Deploy import Deploy as depl
import argparse

# import expir

parser = argparse.ArgumentParser(
    prog='Project Manager',
    description='Эта программа помогает отслеживать содержимое каталога с проектами'
)
parser.add_argument('-g', '--get', type=str, default='')
parser.add_argument('-l', '--lst', type=str, default='')
parser.add_argument('-gr', '--gitr', type=str)

args = parser.parse_args()


def git_remote(arg, path=all):
    gitr = depl()
    gitr_view = view()
    dict_of_remote = gitr.git_remote_search(path)
    gitr_view.sorter(dict_of_remote)


def get(arg):
    kwargs = {
        'type_fild': 'type',
        'type_of_search': args.get,
    }

    ess = path_handler()
    ess_view = view()
    dict_of_essence = ess.dir_travel(ess.fild_search, kwargs)
    ess_view.sorter(dict_of_essence)


def lst(arg):
    types_kwargs = {
        'type_fild': args.lst,
    }

    types = path_handler()
    types_view = view()
    dict_of_types = types.dir_travel(types.values_search, types_kwargs)
    types_view.sorter_keys(dict_of_types)


if __name__ == '__main__':
    if args.get != '':
        get(args.get)
    elif args.lst != '':
        lst(args.lst)
    elif args.gitr != '':
        git_remote(args.gitr, '.')
    else:
        print('Должны быть введены аргументы')
