def step2_umbrella():
    while True:
        print('\nЧтобы глисты вышли нужно всего лишь...'
          '\nЯ экономлю на счетчиках используя один копеечный...'
          '\nКогда из роженицы полезло ЭТО врачи были в шоке'
          '\n Новое платье Пугачевой поразило ВСЕХ'
          '\n НУЖНА ВСЕГО ЛИШЬ ЛОЖКА СОДЫ И ОДИН ЛИМОН'
          '\n Всего одна таблетка и          '
          '\n 10 лучших рецептов из кабачка'
              '\n  ▲'
              '\n ▲ ▲'

          )

def step2_no_umbrella():
    print('Ну, тогда взять бокал сидра. Один.')

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('ЧИТАТЬ ПРОДОЛЖЕНИЕ В ИСТОЧНИКЕ: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()


