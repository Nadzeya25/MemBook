# import keyboard
from logg import logging
from operations import create_note, show_notes, deleting_note, find_note_by_id, find_note_by_data, edit_notes
import os


def start_menu():
    while True:
        logging.info("Главное меню")
        print("Главное меню блокнота Заметки: ")
        num_menu = input("Выберите действие из списка\n"
                         "1 - Операции\n"
                         "2 - Выход\n"
                         )
        match num_menu:
            case "1":
                logging.info("Вход в меню Операции")
                menu_notes(num_menu)
            case "2":
                logging.info("Окончание работы")
                print("Вы покидаете приложение Заметки")
                exit()
            case _:
                logging.info("Некорректный ввод")
                print("Некорректный ввод номера меню")


def menu_notes(num_menu):
    while True:
        if num_menu == "1":
            if os.stat("Base_membook.csv").st_size == 0:
                logging.info("блокнот пуст")
                print()
                print("Сейчас здесь пусто, надо заполнить блокнот заметками")
                create_note()
            print("Меню операций")
            menu_operations = input("Выберите операцию\n"
                                    "1 - Добавление новой заметки\n"
                                    "2 - Показать все заметки\n"
                                    "3 - Удаление заметки\n"
                                    "4 - Редактирование заметки\n"
                                    "5 - Поиск заметки по дате\n"
                                    "6 - Поиск заметки по номеру\n"
                                    "0 - Возврат в стартовое меню\n"
                                    )
            match menu_operations:
                case "1":
                    logging.info("Выбор операции - Добавление новой заметки")
                    create_note()

                    break
                case "2":
                    logging.info("Выбор операции - Показать все заметки")
                    show_notes()
                    break
                case "3":
                    logging.info("Выбор операции - Удаление заметки")
                    deleting_note()
                    break
                case "4":
                    logging.info("Выбор операции - Редактирование заметки")
                    edit_notes()
                case "5":
                    logging.info("Выбор операции - Поиск заметки по дате")
                    find_note_by_data()
                    break
                case "6":
                    find_note_by_id()
                    logging.info("Выбор операции - Поиск заметки по номеру")
                    break
                case "0":
                    logging.info("Выход в главное меню")
                    break
                case _:
                    logging.info("Некорректный ввод")
                    print("Некорректный ввод номера меню ")
