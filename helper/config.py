import yaml


class Config(object):

    def __init__(self, file_path):
        self.read(file_path)


    def read(self, file_path):
        from utils import apply_func_to_dict
        from utils import substitute_env_variables_in
        try:
            with open(file_path, 'r') as file_reader:
                cfg = apply_func_to_dict(yaml.safe_load(file_reader), substitute_env_variables_in)
        except IOError:
            raise IOError('Error reading configuration object')
        except:
            raise ValueError('The contents of the file do not adhere to json structure')

        self._config = cfg


    def merge_configs(self, c):
        print("TODO: implement this")


    def contains(self, item):
        return item in self._config

