def menu():
    print("""
======================
  Welcome to OFFICE 
       you can
======================
1. Open ID card
2. Add a new ID card
3. Replace info
4. Search info
5. Delete ID card
0. Exit
======================
    """)


def option() -> str:
    result = input('Enter the number from menu -> ')
    return result


def open_id(office):
    print(office.get(int(input('Enter the number of ID, you want to open -> '))), 'The ID did not find')


def add_id(office):
    key = int(input('Enter the number of ID -> '))
    office.update({key: [{'Name': str(input('Enter a name -> ')),
                          'Phone': str(input('Enter a phone -> ')),
                          'E-mail': str(input('Enter an e-mail -> ')),
                          'Post': str(input('Enter a post -> ')),
                          'Cab': int(input('Enter a cabinet -> ')),
                          'Skype': str(input('Enter a skype -> '))
                          }]
                   })
    print('New ID card added! -> ', office[key])


def replace_info(office):
    key = int(input('Enter the number of ID you want to replace -> '))
    office.update({key: [{'Name': str(input('Enter a name -> ')),
                          'Phone': str(input('Enter a phone -> ')),
                          'E-mail': str(input('Enter an e-mail -> ')),
                          'Post': str(input('Enter a post -> ')),
                          'Cab': int(input('Enter a cabinet -> ')),
                          'Skype': str(input('Enter a skype -> '))
                          }]
                   })
    print('Info in ID card replaced! -> ', office[key])


def search_info(office):
    key1 = int(input('Enter number of ID card (1, 2, 3 ...) -> '))
    key2 = str(input('Enter the info to find (Name, Phone, E-mail, Post, Cab or Skype -> ').capitalize())

    find = office[key1][0][key2]
    print('Found -> ', find)


def delete_id(office):
    num = int(input('Enter the number of ID you want to delete -> '))
    del office[num]
    print('ID deleted!')
    # print(office)
