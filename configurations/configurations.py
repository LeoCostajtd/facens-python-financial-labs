class Configurations ():
    def__init__(self):
        self.__file_output = './out/transactions.txt' #definir o diretorio atual

    @property
    def file_output(self):
        return self.__file_output
