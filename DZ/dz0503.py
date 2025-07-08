def sr(fn):
    def summ_sr(*args):
        print('Среднее арифметическое чисел : ', *args, fn(*args) / len(args))

    return summ_sr


@sr
def summa(*args):
    return sum(args)


summa(2, 3, 3, 4)




