from assistant.Indexator import Indexator as path_handler
from assistant.Viewer import Viewer as view

# import expir

if __name__ == '__main__':
    """Просматриваем все каталоги и подкаталоги от этого уровня и ниже
    
    1. Определяем структуру:
        1. Создаём дерево тем
        2. В качестве листьев предполагаем отдельные проекты
        3. Выделяем документацию (те подкаталоги, в которых количество .md файлов > 1)
        4. Исключаем из анализа данный проект
    
    """

    th_kwargs = {
        'type_fild': 'type',
        'type_of_search': 'theme',
    }

    th = path_handler()
    th_view = view()
    dict_of_themes = th.dir_travel(th.fild_search, th_kwargs)
    th_view.sorter(dict_of_themes)

    print('-----------------------------')

    pr_kwargs = {
        'type_fild': 'type',
        'type_of_search': 'project',
    }

    pr = path_handler()
    pr_view = view()
    dict_of_projects = pr.dir_travel(pr.fild_search, pr_kwargs)
    pr_view.sorter(dict_of_projects)

    print('-----------------------------')

    types_kwargs = {
        'type_fild': 'type',
    }

    types = path_handler()
    types_view = view()
    dict_of_types = types.dir_travel(types.values_search, types_kwargs)
    types_view.sorter_keys(dict_of_types)
