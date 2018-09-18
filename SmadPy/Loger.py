# Паттерн singleton
# Хотим иметь один объект везде, где подключаем этот модуль создаем объект этого класса


class Loger:
    class __Loger:
        def __init__(self):
            self.fileName = "log.txt"
            self.inFile = True
            self.inConsole = True

    instance = None

    def __init__(self):
        if not Loger.instance:
            Loger.instance = Loger.__Loger()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        setattr(self.instance, name, value)

    def log(self, *args):
        self = self.instance
        if self.inConsole is True:
            for arg in args:
                print(arg, end=' ')
            print("")

        if self.inFile is True:
            with open(self.fileName, 'a') as f:
                for arg in args:
                    print(arg, file=f, end=' ')
                print("", file=f)
    def clearFile(self):
        self=self.instance
        f = open(self.fileName,'w')
        f.close()



# Делегируем некоторые вызовы синглтону

def log(*args):
    Loger().log(*args)


def setFileName(outfileName):
    Loger().fileName = outfileName


def setOutInFile(isNeed):
    Loger().inFile = isNeed


def setOutInConsole(isNeed):
    Loger().inConsole = isNeed

def clearFile():
    Loger().clearFile()

