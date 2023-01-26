class Viewer:
    def sorter(self, dict_of_essence):
        essence_names = []
        for essence in dict_of_essence:
            essence_names.append(essence)

        essence_names.sort()
        for theme in essence_names:       # Вывод тем по алфавиту
            print(f'{theme:<14}{dict_of_essence[theme]}')