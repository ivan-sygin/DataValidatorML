import pandas as pd


class FileWithData:
    filename: str
    _data: pd.DataFrame
    column_count: int

    @property
    def data(self):
        return self._data

    @data.getter
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.column_count = len(self.data.columns.tolist())

    def __init__(self, filename):
        self.filename = filename
        self.data = pd.read_csv(filename)

    def delete_empty_columns(self):
        self.data = self.data.dropna(axis='columns', how='all')

    def delete_duplicate_columns(self):
        self.data = self.data.T.drop_duplicates().T

    def save_to_file(self, filename):
        self.data.to_csv(filename)

    def sort_by_columns(self,numbers):
        if type(numbers) == int:
            self.data = self.data.sort_values(self.data.columns.tolist()[numbers], ascending=True)
        elif type(numbers) == list:
            list_columns = self.data.columns.tolist()
            list_name_cols = [list_columns[num-1] for num in numbers]
            self.data = self.data.sort_values(list_name_cols, ascending=True)
