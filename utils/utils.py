#abrir arquivo e escrever no arquivo
from configurations.configurations import Configurations #pode usar tudo da pasta configurations.py
from datatime import date

class Utils():
    def __init__(self):
        self.__configurations = Configurations ()
        
    def read_file(self):
        with open(self.__configurations.file_output, 'r') as file:
            return map(lambda l: l.replace('\n', ''),file.readlines())
    
    def write_file(self, _type, value, description):
        with open(self.configurations.file_output, 'a+') as file: #a+ para add ao ultimo arquivo
            file.write(
                f'\n{date.today()} - {_type} - R$ {value} - {description}'
            )