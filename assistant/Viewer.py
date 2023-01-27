class Viewer:
    def sorter(self, dict_of_essence):
        essence_list = []
        for essence in dict_of_essence:
            essence_list.append(essence)

        essence_list.sort()
        for key in essence_list:  # Вывод ключей по алфавиту
            print(f'{key:<14}{dict_of_essence[key]}')

    def sorter_keys(self, dict_of_essence):
        essence_list = []
        values_list = set(dict_of_essence.values())
        for essence in values_list:
            essence_list.append(essence)

        essence_list.sort()
        for item in essence_list:
            print(item)
