x = 1
task_list = {}

class Task:
    __num = 0

    def __init__(self, string):
        self.__string = string
        self.__id = str(Task.__num)
        Task.__num += 1
        self.__status = 'todo'
        task_list[self.__id] = self

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, new_string):
        self.__string = new_string

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status

    def __str__(self):
        return self.__id + '     ' + self.string + '     ' + self.status

def cr_task():
    x = input('Введите задачу: ')
    return Task(x)

def pr_tasks():
    if not task_list:
        print("Нет задач.")
    else:
        for task in task_list.values():
            print(task)

def ch_string(t_id):
    if t_id in task_list:
        task_list[t_id].string = input('Введите новый текст задачи: ')
    else:
        print("Задача не найдена.")

def ch_status(t_id):
    if t_id in task_list:
        if input('Если задача в процессе, введите 1, если уже выполнена, введите 2: ') == '1':
            task_list[t_id].status = 'in-progress'
        else:
            task_list[t_id].status = 'done'
    else:
        print("Задача не найдена.")

def main():
    global x
    while x:
        print("\nМеню:")
        print("1. Создать задачу")
        print("2. Показать задачи")
        print("3. Изменить текст задачи")
        print("4. Изменить статус задачи")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            cr_task()
        elif choice == '2':
            pr_tasks()
        elif choice == '3':
            t_id = input("Введите ID задачи для изменения текста: ")
            ch_string(t_id)
        elif choice == '4':
            t_id = input("Введите ID задачи для изменения статуса: ")
            ch_status(t_id)
        elif choice == '5':
            x = 0
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
