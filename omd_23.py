def step2_umbrella():
    print('Утка и сидр были сухими')


def step2_no_umbrella():
    print(
        'Сухим был только сидр.'
        '\nНу, крякнем и булькнем в тину!'
        '\nКрякнуть еще?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        print(
            'Вы крякнули и булькнули в тину.'
            '\nПоделом.'
        )
    print('КОНЕЦ')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()

