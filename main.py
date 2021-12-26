documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}
def exit():
    command_exit = True
    return command_exit


def people_command_execution(document_number):
    for number in documents:
       if document_number == number['number']:
           return number['name']
    return 'Документа нет в базе'

def people():
    document_number = input('Введите номер документа:' )
    result = people_command_execution(document_number)
    print(result)


def shelf_command_execution(document_number):
    for shelf in directories:
        for number in directories[shelf]:
           if document_number == number:
               return shelf
    return 'Документа нет в базе'

def shelf():
    document_number = input('Введите номер документа:')
    result = shelf_command_execution(document_number)
    print(result)


def list():
    for data in documents:
        print(f"Тип документа:'{data['type']}' Номер документа:'{data['number']}' Имя владельца:'{data['name']}'")


def add_command_execution(document_type, document_number, owner_name, number_self):
    for number in documents:
       if document_number == number['number']:
           return 'Номер документа уже есть в базе!'
    for shelf in directories:
        if number_self == shelf:
            new_data = {"type": document_type, "number": document_number, "name": owner_name}
            documents.append(new_data)
            directories[number_self].append(document_number)
            result = str(document_number) + ' добавлен'
            return result
    return 'Полка не существует!'


def add():
    document_type = input('Введите тип документа:')
    document_number = input('Введите номер документа:')
    owner_name = input('Введите имя владельца:')
    number_self = input('Введите номер полки:')
    result = add_command_execution(document_type, document_number, owner_name, number_self)
    print(result)


def delete_command_execution(document_number):
    for number in documents:
       if document_number == number['number']:
           documents.remove(number)
    for shelf in directories:
        for number_doc in directories[shelf]:
            if document_number == number_doc:
                directories[shelf].remove(document_number)
                return str(document_number) + ' удалён'
    return 'Документа нет в базе!'

def delete():
    document_number = input('Введите номер документа:')
    result = delete_command_execution(document_number)
    print(result)


def move_command_execution(document_number, number_self):
    for self in directories:
        for number in directories[self]:
           if document_number == number:
               for key_self in directories:
                   if key_self == number_self:
                       directories[self].remove(document_number)
                       directories[number_self].append(document_number)
                       result = 'Докумет ' + str(document_number) + ' перемещён на полку ' + str(number_self)
                       return result
    return 'Полка не существует!'

def move():
    document_number = input('Введите номер документа:')
    number_self = input('На какую полку переместить?:')
    result = move_command_execution(document_number, number_self)
    print(result)


def add_shelf_command_execution(number_self):
    if number_self in directories:
        return 'Полка существует!'
    directories.setdefault(number_self,[])
    return 'Полка ' + str(number_self) + ' добавлена!'

def add_shelf():
    number_self = input('Введите номер полки:')
    result = add_shelf_command_execution(number_self)
    print(result)

def help():
    help = open('command_help.txt', 'r',  encoding='utf-8')
    for file in help:
        print(file)
    help.close()

def checking_input(executable_command):
    checking = executable_command
    if executable_command == 'p':
        checking = executable_command.replace('p', 'people')
    if executable_command == 's':
        checking = executable_command = executable_command.replace('s', 'shelf')
    if executable_command == 'l':
        checking = executable_command.replace('l', 'list')
    if executable_command == 'a':
        checking = executable_command.replace('a', 'add')
    if executable_command == 'd':
        checking = executable_command.replace('d', 'delete')
    if executable_command == 'm':
        checking = executable_command.replace('m', 'move')
    if executable_command == 'as':
        checking =  executable_command.replace('as', 'add_shelf')
    return checking


if __name__ == '__main__':
    result = False
    command_exit = False
    while command_exit == False:
        executable_command = input('Введите команду:' ).lower()
        checking = checking_input(executable_command)
        try:
            result = globals()[checking]()
        except KeyError:
            print('Ввод не существующей команды')
            result = 'N'
        if result == True:
            command_exit = True