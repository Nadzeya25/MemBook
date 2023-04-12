import logging
from datetime import date
import uuid
from os import path
import os

def create_note():
    id_note = str(uuid.uuid1())[0:3]
    title_note = input("Введите название заметки: ")
    body_note = input("Введите содержание заметки: ")
    date_note = str(date.today().strftime("%d-%m-%Y"))
    str_note = (id_note + ";" + title_note + ";" + body_note + ";" + date_note + "\n")
    create_file_notes(str_note)
    logging.info(f'Создана новая заметка с ID - {id_note}')
    return print("Заметка сохранена")


def create_file_notes(text):
    with open('Base_membook.csv', 'a', encoding='utf-8') as data:
        data.write(text)


def read_notes_from_file():
    array_notes = []
    if path.exists('Base_membook.csv'):
            with open('Base_membook.csv', 'r', encoding='utf-8') as data:
                notes = data.read().strip().split('\n')
                for note in notes:
                    split_note = note.split(';')

                    array_notes.append(split_note)
            return array_notes


def show_notes():
    input_array = read_notes_from_file()
    for arr in input_array:
        print('ID - ' + arr[0] + '\n' +
              'Название заметки - ' + arr[1] + '\n' +
              'Содержание заметки - ' + arr[2] + '\n' +
              'Дата создания - ' + arr[3] + '\n'
              )


def deleting_note():
    input_array = read_notes_from_file()
    for note in input_array:
        print(f'ID - {note[0]}\nИмя заметки - {note[1]}\n')
    id_del = input('Выберите ID заметки, которую хотите удалить: ')
    flag = False
    for note in input_array:
        if id_del == note[0]:
            flag = True
            input_array.remove(note)
    with open('Base_membook.csv', 'w+', encoding='utf-8') as file:
        file.seek(0)
        file.close()
    with open('Base_membook.csv', 'a', encoding='utf-8') as file:
        for note in input_array:
            new_str = (note[0] + ';' + note[1] + ';' + note[2] + ';' + note[3] + '\n')
            file.write(new_str)
    if flag:
        logging.info(f'Заметка с ID - {id_del} удалена!!!!')
        print(f'Заметка с ID - {id_del} удалена!!!!')
    else:
        logging.info('Ошибка ввода')
        print('Заметки с таким ID нет, повторите операцию')
    logging.info(f'Удалена заметка с ID - {id_del}')


def find_note_by_id():
    if path.exists('Base_membook.csv'):
        input_array = read_notes_from_file()
        for note in input_array:
            print(f'ID - {note[0]}')
        id_find = input('Выберите ID заметки для поиска: ')
        flag = False
        for note in input_array:
            if id_find == note[0]:
                print('ID - ' + note[0] + '\n' +
                      'Название заметки - ' + note[1] + '\n' +
                      'Содержание заметки - ' + note[2] + '\n' +
                      'Дата создания - ' + note[3] + '\n'
                      )
                flag = True
        if flag is False:
            logging.info('Ошибка ввода')
            print('Заметки с таким ID нет!!')

    else:
        print('Что то пошло не так, попробуйте еще раз!')


def find_note_by_data():
    if path.exists('Base_membook.csv'):
        input_array = read_notes_from_file()
        find_data = input('Введите дату в формате "dd-mm-yyyy"\n')
        flag = False
        for note in input_array:
            if find_data == note[-1]:
                print('ID - ' + note[0] + '\n' +
                      'Название заметки - ' + note[1] + '\n' +
                      'Содержание заметки - ' + note[2] + '\n' +
                      'Дата создания - ' + note[3] + '\n'
                      )
                flag = True
        if flag is False:
            logging.info('Ошибка ввода')
            print('Заметка с такой датой не найдена')
    else:
        print('Что то пошло не так, попробуйте еще раз!')


def edit_notes():
    input_array = read_notes_from_file()
    for note in input_array:
        print(f'ID - {note[0]}\nИмя заметки - {note[1]}\n')
    edit_note = input('Выберите ID заметки которую необходимо изменить: ')
    flag = False
    for note in input_array:
        if edit_note == note[0]:
            flag = True
            while True:
                print('Меню редактирования заметки')
                type_num = input('Выберите вариант редактирования\n'
                                 '1 - Редактирование названия заметки\n'
                                 '2 - Редактирование содержания заметки\n'
                                 ).strip()
                match type_num:
                    case '1':
                        note[1] = input('Введите новое название заметки: ')
                        logging.info(f'Название заметки с ID-{edit_note} изменено')
                        with open('Base_membook.csv', 'w+', encoding='utf-8') as file:
                            file.seek(0)
                            file.close()
                        with open('Base_membook.csv', 'a', encoding='utf-8') as file:
                            for note in input_array:
                                new_str = (note[0] + ';' + note[1] + ';' + note[2] + ';' + note[3] + '\n')
                                file.write(new_str)
                        break
                    case '2':
                        note[2] = input('Введите новое содержание заметки: ')
                        logging.info(f'Содержание заметки с ID-{edit_note} изменено')
                        with open('Base_membook.csv', 'w+', encoding='utf-8') as file:
                            file.seek(0)
                            file.close()
                        with open('Base_membook.csv', 'a', encoding='utf-8') as file:
                            for note in input_array:
                                new_str = (note[0] + ';' + note[1] + ';' + note[2] + ';' + note[3] + '\n')
                                file.write(new_str)
                        break
    if flag is False:
        logging.info('Ошибка ввода')
        print('Заметки с таким ID нет, повторите операцию')