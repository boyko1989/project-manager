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
    dict_of_themes = path_handler().ls_of_themes()
    theme_sort = view()
    theme_sort.sorter(dict_of_themes)

    print('------------------')

    dict_of_projects = path_handler().ls_of_projects()
    projects_sort = view()
    theme_sort.sorter(dict_of_projects)
    # expir.expir()