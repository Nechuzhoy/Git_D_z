from application.salary import calculate_salary
from application.db.people import get_employees
import PyQt5


if __name__ == '__main__':
    print(f'Сегодня, что-то: {calculate_salary(3, 3)}')
    print(f'А, что-то: {get_employees(3,3)}')
