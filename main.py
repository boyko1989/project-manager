from assistant.PathClass import PathClass as path_handler

if __name__ == '__main__':
    """Просматриваем все каталоги и подкаталоги от этого уровня и ниже
    
    1. Определяем структуру:
        1. Создаём дерево тем
        2. В качестве листьев предполагаем отдельные проекты
        3. Выделяем документацию (те подкаталоги, в которых количество .md файлов > 1)
        4. Исключаем из анализа данный проект
    
    """
    theme_names = []
    path_handler = path_handler()
    for theme in path_handler.ls_of_themes():       # theme.name
        theme_names.append(theme.name)

    theme_names.sort()
    for theme in theme_names:
        print(theme)            # Вывод тем по алфавиту
