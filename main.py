class Task:
    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.completed = False
    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.body}\n[{'x' if self.completed else ' '}] {'Completed' if self.completed else 'Not completed'}"

def add_task(args, config):
    if len(args) != 2:
        print("Expected 2 arguments")
        return
    config['tasks'].append(Task(args[0], args[1]))

def view_tasks(args, config):
    if len(args) != 0:
        print("Expected no arguments")
        return
    for task in config['tasks']:
        print(task)

def remove_task(args, config):
    if len(args) != 1:
        print("Expected 1 arguments")
        return
    for task in config['tasks']:
        if task.title == args[0]:
            config['tasks'].remove(task)
            return

def complete_task(args, config):
    if len(args) != 1:
        print("Expected 1 arguments")
    for i, task in enumerate(config['tasks']):
        if task.title == args[0]:
            config['tasks'][i].completed = not config['tasks'][i].completed
            return
    

def commander():
    c = {
        'add_task': {
            'name': 'add_task',
            'callback': add_task,
        },
        'view_tasks': {
            'name': 'view_tasks',
            'callback': view_tasks,
        },
        'remove_task': {
            'name': 'remove_task',
            'callback': remove_task,
        },
        'complete_task': {
            'name': 'complete_task',
            'callback': complete_task,
        },
    }
    return c

conf = {
    'tasks': []
}

while True:
    print("What you want to do:", end=' ')
    inp = input()
    comm = inp.split()[0]
    args = inp.split()[1:]
    if comm in commander():
        commander()[comm]['callback'](args, conf)
    else:
        print("Available commands: ", *list(x + ' ' for x in commander()))

