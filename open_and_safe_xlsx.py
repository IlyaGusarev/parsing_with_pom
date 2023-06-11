import pandas as pd


class OpenAndSafeXlsx:
    def __init__(self, filename):
        self.filename = filename
        self.result_names = []

    def open_data(self):
        self.df = pd.read_excel(f'data/{self.filename}')
        self.codes = self.df['Наименование'].tolist()
        self.names = self.df['Залогодатель'].tolist()
        self.reg_date = self.df['Дата регистрации'].tolist()

    def append_name(self, name):
        self.result_names.append(name)

    def save_result(self):
        result = {
            'Наименование': self.codes,
            'Дата регистрации': self.reg_date,
            'Залогодатель': self.result_names,
        }

        df = pd.DataFrame(result)

        writer = pd.ExcelWriter(f'result/{self.filename}', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        writer._save()
