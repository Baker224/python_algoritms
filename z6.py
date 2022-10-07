"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class Queue:
    def __init__(self):
        self.new_task = []
        self.re_complete_task = []
        self.complete_task = []

    def push(self, item):
        self.new_task.append(item)

    def work_complete(self):
        removed = self.new_task.pop(0)
        self.complete_task.append(removed)
        return removed

    def rework(self):
        removed = self.new_task.pop(0)
        self.re_complete_task.append(removed)
        return removed

    def rework_complete(self):
        removed = self.re_complete_task.pop(0)
        self.complete_task.append(removed)
        return removed

    def tasks(self):
        return print(self.new_task, 'new tasks'), print(self.re_complete_task, 'rework'), print(self.complete_task,
                                                                                                'complete')


dashboard = Queue()
dashboard.push(1)
dashboard.push(2)
dashboard.tasks()
dashboard.work_complete()
dashboard.tasks()
dashboard.rework()
dashboard.tasks()
dashboard.rework_complete()
dashboard.tasks()
