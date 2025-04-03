class Converter:
    def __init__(self, killogram):
        self.__killogram = killogram

    def __check_value(c):
        if isinstance(c, int) or isinstance(c, float):
            return True
        return False

    @property
    def killogram(self):
        return self.__killogram

    @killogram.setter
    def killogram(self, killogram):
        if Converter.__check_value(killogram):
            self.__killogram = killogram
        else:
            print('Килограммы задаются только числами.')
        # self.__killogram = killogram


pound1 = Converter(12)
print(pound1.killogram, 'кг', '=>', pound1.killogram * 2.205, 'фунтов')
pound1.killogram = 41
print(pound1.killogram, 'кг', '=>', pound1.killogram * 2.205, 'фунтов')
pound1.killogram = 'hhf'