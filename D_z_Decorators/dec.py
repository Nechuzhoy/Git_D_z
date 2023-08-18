import os
import logging
from functools import wraps


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        logging.basicConfig(filename="main.log", level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")
        # logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
        # format="%(asctime)s %(levelname)s %(message)s")
        # level: это — уровень, на котором нужно начинать логирование.
        # Если он установлен в info — это значит, что все сообщения с уровнем debug игнорируются.
        # filename: этот параметр указывает на объект обработчика файла.
        # Тут можно указать имя файла, в который нужно осуществлять логирование.
        # filemode: это — необязательный параметр, указывающий режим, в котором предполагается работать с файлом журнала
        # w (write, запись) приводит к тому, что логи перезаписываются при каждом запуске
        # По умолчанию параметр filemode установлен в значение a (append, присоединение),
        # то есть — в файл будут попадать записи из всех сеансов работы программы.
        # format снабдить записи отметками времени, указывающими на момент вывода той или иной записи.
        # logging.debug("A DEBUG Message")
        # logging.info("An INFO")
        # logging.warning("A WARNING")
        # logging.error("An ERROR")
        # logging.critical("A message of CRITICAL severity")
        result = old_function(*args, **kwargs)
        logging.info(f'{old_function}, with arguments {args} and {kwargs}, Result = {result}')
        return result

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'



    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()