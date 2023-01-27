def is_even(number):
    try:
        if number % 2 == 0:
            return True
        else:
            return False
    except TypeError:
        print('Требуется ввести число для корректной работы программы.')
    except ValueError:
        print('Недопустимое значений')
