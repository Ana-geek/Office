from lib import *

office = {
    1: [{
        'Name': 'Michael Gary Scott',
        'Phone': '300 098 672 99',
        'E-mail': 'gary@gmail.com',
        'Post': 'Director of the company',
        'Cab': 76,
        'Skype': 'gary_scott_98'}],
    2: [{
        'Name': 'Dwight Kurt Schrute',
        'Phone': '300 987 987 77',
        'E-mail': 'dwight_kurt@gmail.com',
        'Post': 'Assistant Regional Manager',
        'Cab': 56,
        'Skype': 'dwight_kurt_56'}],
    3: [{
        'Name': 'James Duncan Halpert',
        'Phone': '300 936 782 44',
        'E-mail': 'james_halpert@gmail.com',
        'Post': ' Assistant Regional Manager',
        'Cab': 44,
        'Skype': 'duncan_8765'}]
}


def main():
    answer = None
    while answer != '0':
        # Вывод меню
        menu()
        # Выбор пользователя
        answer = option()
        # Реализация выбора
        if answer == '1':
            open_id(office)
        elif answer == '2':
            add_id(office)
        elif answer == '3':
            replace_info(office)
        elif answer == '4':
            search_info(office)
        elif answer == '5':
            delete_id(office)
        elif answer == '0':
            print('Bye!')
        else:
            print('Такой команды нет в списке. Попробуйте снова.')


if __name__ == '__main__':
    main()
