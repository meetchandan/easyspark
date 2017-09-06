

class DataSource(object):

    @property
    def name(self):
        return self._name

    @property
    def desc(self):
        return self._desc

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def schema(self):
        return self.schema

    def __init__(self, name, path, schema, desc='', hbase_scan=None):
        pass

