from assistant.PathClass import PathClass as path_handler

if __name__ == '__main__':
    """Просматриваем все каталоги и подкаталоги от этого уровня и ниже
    
    1. Определяем структуру:
        1. Создаём дерево тем
        2. В качестве листьев предполагаем отдельные проекты
        3. Выделяем документацию (те подкаталоги, в которых количество .md файлов > 1)
        4. Исключаем из анализа данный проект
    
    """
    path_handler = path_handler()
    # print(path_handler.tree())
    for theme_name in path_handler.tree():
        print(theme_name)
