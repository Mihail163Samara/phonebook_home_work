"""Телефонный справочник с внешним хранилищем информации, и чтоб был реализован основной функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных."""


def show_menu():
    print (

    '1.Список контактов',
    '2.Найти контакт по фамилии',
    '3.Найти контакт по номеру телефона',
    '4.Добавить контакт',
    '5.Редактировать контакт',
    '6.Удалить контакт',
    '7.Импорт контакта из другого справочника',
    '8.Завершить работу со справочником', sep = '\n'
    
    )

    choice = int(input("Введите команду: "))
    return choice

def read_txt(phonebook_txt):                                                          
    list_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(phonebook_txt,"r", encoding='utf-8') as fd:
        for line in fd:
            if line != '\n':
                list_book.append(dict(zip(fields, map(lambda x: x.strip(), line.split(','))))) # заменим 18-23 строки на одну строкой
            
    return list_book  





def print_phonebook(phone_bk_lst):
    for d in phone_bk_lst:
        for k,v in d.items():
            print(f"{k}: {v}", end=' ')
        print()


def find_by_last_name(phone_bk_lst):
    last_name = input("Введите фамилию для поиска:")
    for i in phone_bk_lst:
        if i['Фамилия'] == last_name:
            return i
    return "Контакта с такой фамилией не существует"    


def find_by_number(phone_bk_lst):
    number = input("Введите номер контакта для поиска:")
    for i in phone_bk_lst:
        if i['Телефон'] == number:
            return i
    return "Контакта с таким номером не существует" 



def add_contakt_to_phone_book(phone_bk_lst):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    contakt = {}
    for i in fields:
        contakt[i] = input(f"{i}: ")
    while contakt['Фамилия'] == "":
        contakt['Фамилия'] = input("Фамилия: ")
    phone_bk_lst.append(contakt)
    print("Контакт успешно был добавлен")
    


def save_change_book(file_name,phone_bk_lst):

    with open(file_name,'w',encoding='utf-8') as phout:
        for i in range(len(phone_bk_lst)):
            s='' 
            for v in phone_bk_lst[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')



def show_edit_menu():
    print (
    '1.Фамилия',
    '2.Имя',
    '3.Телефон',
    '4.Описание',
    '5.Выход', sep = '\n'
    )

    choice = int(input("Введите команду: "))
    return choice 




def edit_contact(phone_bk_lst):
    last_name = input("Введите фамилию контакта: ")
    if last_name in [i['Фамилия'] for i in phone_bk_lst]:
        contact_index = 0
        for i in range(len(phone_bk_lst)):
            if phone_bk_lst[i]['Фамилия'] == last_name:
                contact_index = i
                print(phone_bk_lst[i])
                break
        
        choice = show_edit_menu()
        while choice != 5:
            if choice == 1:
                phone_bk_lst [contact_index]['Фамилия'] = input("Фамилия: ")
            elif choice == 2:
                phone_bk_lst [contact_index]['Имя'] = input("Имя: ")
            elif choice == 3:
                phone_bk_lst [contact_index]['Телефон'] = input("Телефон: ")
            elif choice == 4:
                phone_bk_lst [contact_index]['Описание'] = input("Описание: ")
            choice = show_edit_menu()
    else:
        print("Контакта с такой фамилией нет")   




def delete_contact(phone_bk_lst):
    last_name = input("Введите фамилию контакта: ")
    if last_name in [i['Фамилия'] for i in phone_bk_lst]:
        contact_index = 0
        for k in range(len(phone_bk_lst)):
            if phone_bk_lst[k]['Фамилия'] == last_name:
                contact_index = k
                print(phone_bk_lst[contact_index])
                break
        delete=''
        while delete not in ['yes','no']:
            delete=input("Подтвердите удаление данного контакта - напечатайте yes или no: ")
        if delete=='yes':
            phone_bk_lst.pop(contact_index)
            print("Контакт успешно удалён\n ")
    else:
        print("Контакта с такой фамилией нет")   



def import_contact(file_name_copy, phone_bk_lst_1):
    phone_bk_lst_2 = read_txt(file_name_copy)
    print_phonebook(phone_bk_lst_2)
    last_name = input("Введите фамилию контакта: ")
    if last_name in [i['Фамилия'] for i in phone_bk_lst_2]:
        contact_index = 0
        for k in range(len(phone_bk_lst_2)):
            if phone_bk_lst_2[k]['Фамилия'] == last_name:
                contact_index = k
                print(phone_bk_lst_2[k])
                break
        phone_bk_lst_1.append(phone_bk_lst_2[contact_index])
        print("Контакт был успешно добавлен ")
    else:
        print("Фамилия не была найдена. Повторите запрос ") 



def phone_book_work(file_name):
    phone_book_list = read_txt(file_name)
    


    choice = show_menu()

    while choice!=8:
        if choice == 1:
            print_phonebook(phone_book_list)
            print()
                
        elif choice == 2:
            print(find_by_last_name(phone_book_list))
            print()
        elif choice == 3:
            print(find_by_number(phone_book_list))
            print()
        elif choice == 4:
            add_contakt_to_phone_book(phone_book_list)
            save_change_book(file_name,phone_book_list)
            print()
        elif choice == 5:
            edit_contact(phone_book_list)
            save_change_book(file_name,phone_book_list)
            print()
        elif choice == 6:
            delete_contact(phone_book_list)
            save_change_book(file_name,phone_book_list)
            print()
        elif choice == 7:
            phone_book_copy = input("Введите справочник для импорта: ")
            import_contact(phone_book_copy,phone_book_list)
            save_change_book(file_name,phone_book_list)
            print()
        
        choice = show_menu()
        
    print("Всего доброго и до новых встреч. Телефонный справочник завершил свою работу. ")



phone_book_work('phonebook.txt')
