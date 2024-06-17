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
    
    def is_due_today(self):
        return self.due_date == date.today()

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
    
    def list_overdue_tasks(self):
        return [task for task in self.tasks if task.notes]
    
    def mark_as_completed(self, task_title):
        task = self.get_task(task_title)
        if task:
            task.status = "Completed"
    
    def list_completed_tasks(self):
        return [task for task in self.tasks if task.status == "Completed"]
    
    def find_task_by_keyword(self, keyword):
        return [task for task in self.tasks if keyword in task.title or keyword in task.description]
    
    def check_deadlines(self):
        now = datetime.now().date()
        return [task for task in self.tasks if now + timedelta(days=1) >= task.due_date >= now]
    
    def list_all_tasks(self):
        return self.tasks
    
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.due_date},{task.status},{task.priority},{task.notes},{task.duration},{task.recurrence},{task.dependencies}\n")
    
    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                task_info = line.strip().split(',')
                dependencies = eval(task_info[8]) if task_info[8] else None
                self.add_task(Task(title=task_info[0], description=task_info[1], due_date=date.fromisoformat(task_info[2]), status=task_info[3], priority=task_info[4], notes=task_info[5], duration=int(task_info[6]), recurrence=task_info[7], dependencies=dependencies))
    
    def list_tasks_by_duration(self, min_duration, max_duration):
        return [task for task in self.tasks if min_duration <= task.duration <= max_duration]
    
    def task_history(self):
        return self.history
    
    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != "Completed"]
    
    def list_recurring_tasks(self):
        return [task for task in self.tasks if task.recurrence]
    
    def set_reminder(self, task_title, reminder_date):
        task = self.get_task(task_title)
        if task:
            task.reminder_date = reminder_date
    
    def completion_percentage(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task.status == "Completed")
        return (completed_tasks / total_tasks) * 100 if total_tasks else 0
    
    def list_tasks_with_dependencies(self):
        return [task for task in self.tasks if task.dependencies]
    
    def list_tasks_with_completed_dependencies(self):
        return [task for task in self.tasks if task.dependencies and all(dep.status == "Completed" for dep in task.dependencies)]
