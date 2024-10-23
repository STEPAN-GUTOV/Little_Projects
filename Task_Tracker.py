import json
import datetime
import os

x = 1
task_list = {}

class Task:
    __num = 0
    def toJSON(self):
        return json.dumps(self.__dict__, sort_keys=True, indent=4)

    def __init__(self, string, cr_time):
        self.__string = string
        self.__id = str(Task.__num)
        Task.__num += 1
        self.__status = 'todo'
        task_list[self.__id] = self
        self.__cr_time = cr_time

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

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
    @property
    def last_change(self):
        return self.__last_change

    @last_change.setter
    def last_change(self, new_last_change):
        self.__last_change = new_last_change
    @property
    def cr_time(self):
        return self.__cr_time
    

    def __str__(self):
        return self.__id + '     ' + self.string + '     ' + self.status
def cr_task():
    x = input('Введите задачу: ')
    b = Task(x, str(datetime.datetime.today()))
    b.last_change = str(datetime.datetime.today())

def pr_tasks():
    if not task_list:
        print("Нет задач.")
    else:
        for task in task_list.values():
            print(task)
def ch_string(t_id):
    if t_id in task_list:
        task_list[t_id].string = input('Введите новый текст задачи: ')
        task_list[t_id].last_change = str(datetime.datetime.today())
    else:
        print("Задача не найдена.")
def ch_status(t_id):
    if t_id in task_list:
        if input('Если задача в процессе, введите 1, если уже выполнена, введите 2: ') == '1':
            task_list[t_id].status = 'in-progress'
        else:
            task_list[t_id].status = 'done'
        task_list[t_id].last_change = str(datetime.datetime.today())
    else:
        print("Задача не найдена.")
def del_task(t_id):
    if t_id in task_list:
        print(task_list.pop(t_id).id, ' Удалена')
        
    else:
        print("Задача не найдена.")
def pr_time():
    if not task_list:
        print("Нет задач.")
    else:
        for i in task_list:
            print(i, 'создан: ',task_list[i].cr_time, 'последнее изменение: ',task_list[i].last_change)


load = {}
if not os.path.exists('output.json'):
        with open('output.json', 'w') as file:
            json.dump({}, file) 
        print("Создан новый файл output.json.")

with open('output.json', 'r') as file:
    load = json.load(file)


task_list.clear()

for new_id, i in enumerate(load):
    string = json.loads(load[i])["_Task__string"]
    status = json.loads(load[i])["_Task__status"]
    cr_time = json.loads(load[i])["_Task__cr_time"]
    last_change = json.loads(load[i])["_Task__last_change"]
    task = Task(string, cr_time)
    task.status = status
    task.last_change = last_change
    task_list[str(new_id)] = task



def main():
    global x
    while x:
        print("\nМеню:")
        print("1. Создать задачу")
        print("2. Показать задачи")
        print("3. Изменить текст задачи")
        print("4. Изменить статус задачи")
        print("5. Удалить задачу")
        print("6. Показать дату создания и изменения")
        print("7. Выход")


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
            t_id = input("Введите ID задачи для удаления: ")
            del_task(t_id)
        elif choice == '6':
            pr_time()

        elif choice == '7':
            x = 0
            update = {}
            for i in task_list:
                update[i] = task_list[i].toJSON()
            with open('output.json', 'w') as file:
                json.dump(update, file, indent=4)
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()


