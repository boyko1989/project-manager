class Array_functions():
    def aaa_del(path):
        clear_path = path.split('/')

        del clear_path[-1]
        del clear_path[-1]

        clear_path = '/'.join(clear_path)

        return clear_path
