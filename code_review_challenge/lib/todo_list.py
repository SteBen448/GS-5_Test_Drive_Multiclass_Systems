# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        if todo.task in list(map(lambda t: t.task, self.todo_list)):
            raise Exception("This task already exists")
        self.todo_list.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are incomplete
        falseList = list(filter(lambda item: item.complete == False, self.todo_list))
        return falseList

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        trueList = list(filter(lambda item: item.complete == True, self.todo_list))
        return trueList

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self.todo_list: 
            if task.complete == False:
                task.complete = True


