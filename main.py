from base import preview,add_record,del_record,find_record,edit_record,create_base

def input_choice():
    while True:
        user_choice= input('''
    1 - preview
    2 - add_record
    3 - del_record
    4 - find_record
    5 - edit_record
    q - exit
    ''')
        if user_choice == "1":
            preview()
        elif user_choice == "2":
            add_record()
        elif user_choice == "3":
            del_record()
        elif user_choice == "4":
            find_record()
        elif user_choice == "5":
            edit_record()    
        elif user_choice.lower() == "q":
            print('Выход')
            break
        else:
            print('Сделайте правильный выбор!')    
create_base()
input_choice()  