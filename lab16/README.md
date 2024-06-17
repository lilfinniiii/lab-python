# Лабораторна робота №16: Advanced TODO List

## 2.2 Мета роботи
Метою лабораторної роботи є виконання завдань для створення todo list у мові програмування Python.

## 2.3 Опис завдання

### Task 1: Create Task Class
Create a Python class named Task with the following attributes:
```
title
description
due_date (use datetime.date )
```

### Task 2: Add Method to Task Class
Add a method named is_due_today() to the Task class that checks if the task is due today and returns a boolean.

### Task 3: Create Schedule Class
Create a class named Schedule that manages multiple tasks. It should have the following methods:
add_task(task: Task)
remove_task(task_title: str)
get_task(task_title: str) -> Task

### Task 4: List Overdue Tasks
Add a method named list_overdue_tasks() to the Schedule class that returnsa list of tasks that are overdue.

### Task 5: List Tasks Due Today
Add a method named list_tasks_due_today() to the Schedule class that returns a list of tasks that are due today.

### Task 6: Sort Tasks by Due Date
Add a method named sort_tasks_by_due_date() to the Schedule class that returns a list of tasks sorted by their due dates.

### Task 7: Update Task
Add a method named update_task(task_title: str, **kwargs) to the Schedule class that updates the attributes of a task.

### Task 8: Task Status
Add a status attribute to the Task class which can be 'Pending', 'In Progress', or 'Completed'. Modify Task and Schedule to handle task status updates.

### Task 9: Weekly Schedule
Create a method weekly_schedule(start_date: date) in the Schedule class that returns a list of tasks for the week starting from the provided date.

### Task 10: Monthly Schedule
Create a method monthly_schedule(year: int, month: int) in the Schedule class that returns a list of tasks for the specified month.

### Task 11: Task Priority
Add a priority attribute to the Task class which can be 'Low', 'Medium', or 'High'. Modify Task and Schedule to handle task priority.

### Task 12: List Tasks by Priority
Add a method list_tasks_by_priority(priority: str) to the Schedule class that returns a list of tasks with the specified priority.

### Task 13: Save Schedule to File
Add a method save_to_file(filename: str) to the Schedule class that saves the schedule to a file.

### Task 14: Load Schedule from File
Add a method load_from_file(filename: str) to the Schedule class that loads the schedule from a file.

### Task 15: Task Notes
Add a notes attribute to the Task class that can store additional information about the task. Modify Task and Schedule to handle task notes.

### Task 16: List Tasks with Notes
Add a method list_tasks_with_notes() to the Schedule class that returns a list of tasks that have notes.

### Task 17: Mark Task as Completed
Add a method mark_as_completed(task_title: str) to the Schedule class that marks the specified task as completed.

### Task 18: List Completed Tasks
Add a method list_completed_tasks() to the Schedule class that returns a list of completed tasks.

### Task 19: Find Task by Keyword
Add a method find_task_by_keyword(keyword: str) to the Schedule class that returns a list of tasks that contain the specified keyword in their title or description.

### Task 20: Task Deadline Notification
Add a method check_deadlines() to the Schedule class that returns a list of tasks that are due in the next 24 hours.

### Task 21: List All Tasks
Add a method list_all_tasks() to the Schedule class that returns a list of all tasks.

### Task 22: Task Duration
Add a duration attribute to the Task class which specifies the expected time to complete the task in hours. Modify Task and Schedule to handle task duration.

### Task 23: List Tasks by Duration
Add a method list_tasks_by_duration(min_duration: int, max_duration: int) to the Schedule class that returns a list of tasks whose duration falls within the specified range.

### Task 24: Task History
Add a method task_history() to the Schedule class that returns a history of tasks added, removed, and updated in the schedule.

### Task 25: Clear Completed Tasks
Add a method clear_completed_tasks() to the Schedule class that removes all completed tasks from the schedule.

### Task 26: Task Recurrence
Add a recurrence attribute to the Task class that specifies if the task is recurring (daily, weekly, monthly). Modify Task and Schedule to handle task recurrence.

### Task 27: List Recurring Tasks
Add a method list_recurring_tasks() to the Schedule class that returns a list of recurring tasks.

### Task 28: Task Reminders
Add a method set_reminder(task_title: str, reminder_date: date) to the Schedule class that sets a reminder for a specific task.

### Task 29: Task Completion Percentage
Add a method completion_percentage() to the Schedule class that returns the percentage of completed tasks.

### Task 30: Task Dependency
Add a dependencies attribute to the Task class that specifies other tasks that need to be completed before the task can start. Modify Task and Schedule to handle task dependencies.

## 2.4 Виконання роботи
### Task 1: Create Task Class
Код функції `task1`:
```python
from datetime import date, datetime, timedelta
class Task:
    def __init__(self, title, description, due_date, status="Pending", priority="Medium", notes="", duration=1, recurrence=None, dependencies=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority
        self.notes = notes
        self.duration = duration
        self.recurrence = recurrence
        self.dependencies = dependencies
        self.completed_dependencies = []
```
### Task 2: Add Method to Task Class
Код функції `task2`:
```python
    def is_due_today(self):
        return self.due_date == date.today()
```
### Task 3: Create Schedule Class
Код функції `task3`:
```python
class Schedule:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, task):
        self.tasks.append(task)
        self.history.append(("added", task))
    
    def remove_task(self, task_title):
        task = self.get_task(task_title)
        if task:
            self.tasks.remove(task)
            self.history.append(("removed", task))
    
    def get_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                return task
        return None
```
### Task 4: List Overdue Tasks
Код функції `task4`:
```python
    def list_overdue_tasks(self):
        return [task for task in self.tasks if task.notes]
```

### Task 17: Mark Task as Completed
Код функції `task17`:
```python
    def mark_as_completed(self, task_title):
        task = self.get_task(task_title)
        if task:
            task.status = "Completed"
```
### Task 18: List Completed Tasks
Код функції `task18`:
```python
    def list_completed_tasks(self):
        return [task for task in self.tasks if task.status == "Completed"]
```
### Task 19: Find Task by Keyword
Код функції `task19`:
```python
    def find_task_by_keyword(self, keyword):
        return [task for task in self.tasks if keyword in task.title or keyword in task.description]
```
### Task 20: Task Deadline Notification
Код функції `task20`:
```python
    def check_deadlines(self):
        now = datetime.now().date()
        return [task for task in self.tasks if now + timedelta(days=1) >= task.due_date >= now]
```
### Task 21: List All Tasks
Код функції `task21`:
```python
    def list_all_tasks(self):
        return self.tasks
```
### Task 22: Task Duration
Код функції `task22`:
```python
 check task 1
```
### Task 23: List Tasks by Duration
Код функції `task23`:
```python
    def list_tasks_by_duration(self, min_duration, max_duration):
        return [task for task in self.tasks if min_duration <= task.duration <= max_duration]
```
### Task 24: Task History
Код функції `task24`:
```python
    def task_history(self):
        return self.history
```
### Task 25: Clear Completed Tasks
Код функції `task25`:
```python
    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != "Completed"]
```
### Task 26: Task Recurrence
Код функції `task26`:
```python
check task 1
```
### Task 27: List Recurring Tasks
Код функції `task27`:
```python
    def list_recurring_tasks(self):
        return [task for task in self.tasks if task.recurrence]
```
### Task 28: Task Reminders
Код функції `task28`:
```python
    def set_reminder(self, task_title, reminder_date):
        task = self.get_task(task_title)
        if task:
            task.reminder_date = reminder_date
```
### Task 29: Task Completion Percentage
Код функції `task29`:
```python
    def completion_percentage(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task.status == "Completed")
        return (completed_tasks / total_tasks) * 100 if total_tasks else 0
```
### Task 30: Task Dependency
Код функції `task30`:
```python
    def list_tasks_with_dependencies(self):
        return [task for task in self.tasks if task.dependencies]

    def list_tasks_with_completed_dependencies(self):
        return [task for task in self.tasks if task.dependencies and all(dep.status == "Completed" for dep in task.dependencies)]
```
## 2.5 Результати
```python
from datetime import date
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today())
task.is_due_today() # Expected output: True

schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.get_task("Buy groceries") # Expected output: Task

from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today() - timedelta(days=1))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today() + timedelta(days=2))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_overdue_tasks() # Expected output: [task1]

task = Task(title="Buy groceries", description="Milk, Bread, Eggs
", due_date=date(2024, 5, 25))
schedule = Schedule()
schedule.add_task(task)
schedule.mark_as_completed("Buy groceries")
task.status # Expected output: "Completed"

task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_completed_tasks() # Expected output: [task1]

task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.find_task_by_keyword("assignment") # Expected output: [task2]

from datetime import datetime, timedelta
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=datetime.now().date() + timedelta(days=1))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=datetime.now().date() + timedelta(days=2))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.check_deadlines() # Expected output: [task1]

task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_all_tasks() # Expected output: [task1, task2]

task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), duration=2)
schedule = Schedule()
schedule.add_task(task)
task.duration # Expected output: 2

task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), duration=2)
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), duration=4)
schedule = Schedule()
schedule.add_task(task1)

schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task1)
schedule.remove_task("Buy groceries")
schedule.task_history() # Expected output: [("added", task1),
("removed", task1)]

task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.clear_completed_tasks()
schedule.list_all_tasks() # Expected output: [task2]

task = Task(title="Water plants", description="Water the plants
in the garden", due_date=date(2024, 5, 25), recurrence="weekly")
schedule = Schedule()
schedule.add_task(task)
task.recurrence # Expected output: "weekly"

task1 = Task(title="Water plants", description="Water the plants
in the garden", due_date=date(2024, 5, 25), recurrence="weekly")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_recurring_tasks() # Expected output: [task1]

task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule = Schedule()
schedule.add_task(task)
schedule.set_reminder("Buy groceries", date(2024, 5, 24))

task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.completion_percentage() # Expected output: 50.0

task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Prepare breakfast", description="Use
groceries to prepare breakfast", due_date=date(2024, 5, 26),
dependencies=[task1])
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
task2.dependencies # Expected output: [task1]

```

## 2.6 Висновки
У цій лабораторній роботі було виконано завдання з створенням todolist у мові програмування Python

## 2.7 Інструкції з запуску
Для запуску програми вам потрібен Python версії 3.12. Код можна запускати у будь-якому середовищі розробки або з командного рядка.

