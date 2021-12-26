import unittest
from main import people_command_execution, shelf_command_execution, add_command_execution, delete_command_execution, move_command_execution, add_shelf_command_execution

param_list_test_1 = [("Геннадий Покемонов", "11-2"),
                     ("Василий Гупкин", "2207 876234"),
                     ("Документа нет в базе", "126")]

param_list_test_2 = [("1", "2207 876234"),
                     ("Документа нет в базе", "126")]

param_list_test_3 = [("Номер документа уже есть в базе!", "insurance", "2207 876234", "Аристарх Павлов", "1"),
                     ("2307 172344 добавлен", "passport", "2307 172344", "Дмитрий Гавшин", "3"),
                     ("Полка не существует!", "passport", "2307 172444", "Дмитрий Гавшин", "5")]

param_list_test_4 = [("10006 удалён", "10006"),
                     ("Документа нет в базе!", "126")]

param_list_test_5 = [("Докумет 11-2 перемещён на полку 2", "11-2", "2"),
                     ("Полка не существует!", "11-2", "5")]

param_list_test_6 = [("Полка существует!", "1"),
                     ("Полка 4 добавлена!", "4")]



class Test_unit(unittest.TestCase):

    def test_people_command_execution(self):
        for param_1, param_2 in param_list_test_1:
            self.assertEqual(param_1, people_command_execution(param_2), 'Вывод не соответствует ожиданию')

    def test_shelf_command_execution(self):
        for param_1, param_2 in param_list_test_2:
            self.assertEqual(param_1, shelf_command_execution(param_2), 'Вывод не соответствует ожиданию')

    def test_add_command_execution(self):
        for param_1, param_2, param_3, param_4, param_5 in param_list_test_3:
            self.assertEqual(param_1, add_command_execution(param_2, param_3, param_4, param_5), 'Вывод не соответствует ожиданию')

    def test_delete_command_execution(self):
        for param_1, param_2 in param_list_test_4:
            self.assertEqual(param_1, delete_command_execution(param_2), 'Вывод не соответствует ожиданию')

    def test_move_command_execution(self):
        for param_1, param_2, param_3 in param_list_test_5:
            self.assertEqual(param_1, move_command_execution(param_2, param_3), 'Вывод не соответствует ожиданию')

    def test_add_shelf_command_execution(self):
        for param_1, param_2 in param_list_test_6:
            self.assertEqual(param_1, add_shelf_command_execution(param_2), 'Вывод не соответствует ожиданию')



if __name__ == '__main__':
    unittest.main()