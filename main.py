from assistant.PathClass import PathClass as path_handler
# import expir

if __name__ == '__main__':
    """Просматриваем все каталоги и подкаталоги от этого уровня и ниже
    
    1. Определяем структуру:
        1. Создаём дерево тем
        2. В качестве листьев предполагаем отдельные проекты
        3. Выделяем документацию (те подкаталоги, в которых количество .md файлов > 1)
        4. Исключаем из анализа данный проект
    
    """
    theme_names = []
    dict_of_themes = path_handler().ls_of_themes()
    for theme in dict_of_themes:
        theme_names.append(theme)

    theme_names.sort()
    for theme in theme_names:       # Вывод тем по алфавиту
        print(f'{theme:<14}{dict_of_themes[theme]}')

    # expir.expir()