#todo:
#  Разработать систему учета решения задач учениками курса «Разработчик на Питоне».
#
# Проблема.
# Преподаватель каждый урок задает некоторое количество задач в качестве домашнего задания, для упрощения можно считать, что одну.
# Каждый ученик решает каждую задачу. Переводит ее статус в решенную.
# Преподаватель проверяет каждую задачу каждого ученика и либо подтверждает ее статус как решенную или меняет ее статус как не решенную.
# Вопрос. Как спроектировать систему классов на Питоне для решения задачи учета?
# Разработайте систему
# классов (Teacher, Pupil, Lesson, Task. Нужен ли класс Группа?);
# атрибутов для каждого состояния каждого объекта;
# методов для каждого объекта.
# Отчетность? Запросы? Начните с формулировки решаемой задачи – спецификации или технического задания. Затем спроектируйте классы, атрибуты, методы. Протестируйте систему.


import random


class Task:
    def __init__(self, pupil_id: int, info: str, status: str = "UNCHECKED"):
        self.pupil_id = pupil_id
        self.info = info
        self.status = status


class Pupil:
    def __init__(self, pupil_id: int):
        self.pupil_id = pupil_id
        self.completed_homeworks = {}
        self.uncompleted_homeworks = {}

    def get_completed_homework_task_by_lesson(self, lesson_id: int):
        return self.completed_homeworks.get(lesson_id)

    def take_homework_task(self, lesson_id: int, task: Task):
        self.uncompleted_homeworks[lesson_id] = task

    def do_lessons_homework_tasks(self):
        for lesson_id, task in self.uncompleted_homeworks.items():
            task.status = "SOLVED_BY_PUPIL"
            self.completed_homeworks[lesson_id] = task

        self.uncompleted_homeworks.clear()

    def do_lesson_homework_task(self, lesson_id: int):
        lesson_task = self.uncompleted_homeworks.pop(lesson_id)
        lesson_task.status = "SOLVED_BY_PUPIL"

        self.completed_homeworks[lesson_id] = lesson_task

    def get_back_homework_task_for_redoing(self, lesson_id: int, task: Task):
        self.uncompleted_homeworks[lesson_id] = task

        try:
            self.completed_homeworks.pop(lesson_id)
        except KeyError:
            pass


class Group:
    def __init__(self, name: str, pupils: list[Pupil]):
        self.name = name
        self.pupils = {pupil.pupil_id: pupil for pupil in pupils}

    def count_pupils(self) -> int:
        return len(self.pupils)

    def set_pupils_homework_tasks(self, lesson_id: int, task_info: str):
        for pupil in self.pupils.values():
            pupil.take_homework_task(lesson_id, Task(pupil_id=pupil.pupil_id, info=task_info))

    def count_solved_lesson_homeworks_task_from_pupils(self, lesson_id: int) -> dict[int, Task]:
        completed_solved_tasks = {}

        for pupil in self.pupils.values():
            task = pupil.get_completed_homework_task_by_lesson(lesson_id)

            if task is not None and task.status == "SOLVED_BY_PUPIL":
                completed_solved_tasks[pupil.pupil_id] = task

        return completed_solved_tasks

    def count_checked_lesson_homeworks_tasks_by_teacher(self, lesson_id: int):
        count = 0

        for pupil in self.pupils.values():
            task = pupil.get_completed_homework_task_by_lesson(lesson_id)

            if task is not None and task.status == "CHECKED_BY_TEACHER":
                count += 1

        return count

    def get_back_incorrect_tasks_to_pupils(self, lesson_id: int, incorrect_tasks: dict[int, Task]):
        for pupil_id, task in incorrect_tasks.items():
            pupil = self.pupils[pupil_id]

            pupil.get_back_homework_task_for_redoing(lesson_id, task)


class Lesson:
    def __init__(self, lesson_id: int, name: str, group: "Group"):
        self.lesson_id = lesson_id
        self.name = name
        self.group = group

    def get_count_group_pupils(self) -> int:
        return self.group.count_pupils()

    def get_count_group_checked_tasks_by_teacher(self) -> int:
        return self.group.count_checked_lesson_homeworks_tasks_by_teacher(self.lesson_id)

    def set_homework_tasks_for_group(self, task_info: str):
        self.group.set_pupils_homework_tasks(self.lesson_id, task_info)

    def get_solved_group_lesson_tasks(self) -> dict[int, Task]:
        return self.group.count_solved_lesson_homeworks_task_from_pupils(self.lesson_id)

    def get_back_incorrect_tasks_to_group(self, incorrect_tasks: dict[int, Task]):
        self.group.get_back_incorrect_tasks_to_pupils(self.lesson_id, incorrect_tasks)


class Teacher:
    def __init__(self, first_name: str):
        self.first_name = first_name
        self.checked_lessons = {}
        self.unchecked_lessons = {}

    def teach_lesson(self, lesson: Lesson, task_info: str):
        self.unchecked_lessons[lesson.lesson_id] = lesson
        self.give_homework_task_for_lesson(lesson, task_info)

    def give_homework_task_for_lesson(self, lesson: Lesson, task_info: str):
        lesson.set_homework_tasks_for_group(task_info)

    def check_lesson_homework_tasks_by_lesson_id(self, lesson_id: int):
        incorrect_tasks = {}

        lesson = self.unchecked_lessons[lesson_id]

        unchecked_completed_homeworks = {
            pupil_id: task for pupil_id, task in lesson.get_solved_group_lesson_tasks().items()
            if task.status == "SOLVED_BY_PUPIL"
        }

        for pupil_id, task in unchecked_completed_homeworks.items():
            self.check_homework_task(task)

            if task.status == "UNCHECKED":
                incorrect_tasks[pupil_id] = task

        if incorrect_tasks:
            lesson.get_back_incorrect_tasks_to_group(incorrect_tasks)

        if lesson.get_count_group_pupils() == lesson.get_count_group_checked_tasks_by_teacher():
            self.checked_lessons[lesson.lesson_id] = lesson
            self.unchecked_lessons.pop(lesson.lesson_id)

    def check_lessons_homework_tasks(self):
        for lesson in self.unchecked_lessons.values():
            incorrect_tasks = {}

            unchecked_completed_homeworks = {
                pupil_id: task for pupil_id, task in lesson.get_solved_group_lesson_tasks().items()
                if task.status == "SOLVED_BY_PUPIL"
            }

            for pupil_id, task in unchecked_completed_homeworks.items():
                self.check_homework_task(task)

                if task.status == "UNCHECKED":
                    incorrect_tasks[pupil_id] = task

            if incorrect_tasks:
                lesson.get_back_incorrect_tasks_to_group(incorrect_tasks)

            if lesson.get_count_group_pupils() == lesson.get_count_group_checked_tasks_by_teacher():
                self.checked_lessons[lesson.lesson_id] = lesson
                self.unchecked_lessons.pop(lesson.lesson_id)

    def check_homework_task(self, task: Task):
        task.status = random.choice(["CHECKED_BY_TEACHER", "UNCHECKED"])


if __name__ == "__main__":
    pupils = [Pupil(pupil_id) for pupil_id in range(1, 10)]
    group = Group("GG-101", pupils)

    math_lesson = Lesson(3, "Математика", group=group)

    physics_teacher = Teacher("Анна")

    physics_teacher.teach_lesson(math_lesson, "решить уравнения энштейна")

    for pupil in pupils:
        pupil.do_lesson_homework_task(math_lesson.lesson_id)

    for pupil in pupils:
        assert pupil.completed_homeworks

        for pupil_task in pupil.completed_homeworks.values():
            assert pupil_task.status == "SOLVED_BY_PUPIL"

    physics_teacher.check_lesson_homework_tasks_by_lesson_id(math_lesson.lesson_id)

    for pupil in pupils:
        if pupil.completed_homeworks:
            for pupil_task in pupil.completed_homeworks.values():
                assert pupil_task.status == "CHECKED_BY_TEACHER"

        if pupil.uncompleted_homeworks:
            for pupil_task in pupil.uncompleted_homeworks.values():
                assert pupil_task.status == "UNCHECKED"

    print(group.count_checked_lesson_homeworks_tasks_by_teacher(math_lesson.lesson_id))

    while group.count_checked_lesson_homeworks_tasks_by_teacher(math_lesson.lesson_id) != group.count_pupils():
        for pupil in [pupil for pupil in pupils if not pupil.completed_homeworks]:
            pupil.do_lesson_homework_task(math_lesson.lesson_id)
        physics_teacher.check_lesson_homework_tasks_by_lesson_id(math_lesson.lesson_id)

    print(group.count_checked_lesson_homeworks_tasks_by_teacher(math_lesson.lesson_id))