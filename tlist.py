import csv
import os
import uuid
from csv import writer 

class Todo(object):
    
    def __init__(self, todo_name, complete=False, identifier=None):
        self.todo_name = todo_name
        self.complete = complete
        self.id = identifier
        if self.id is None:
            self.id = str(uuid.uuid4())


class TodoList(object):
    """Code needed to manage todo list"""
    
    def __init__(self):
        self.container = []
    
    
    def add_todo(self, todo_name, complete=False): #adds/creates a new todo
        """ add a todo to self.todos"""
        todo = Todo(todo_name, complete)
        self.container.append(todo)
        return todo


    def _find_todo(self, todo_id): # is this an object or an int 
        """locate todo in todo list"""
        for todo_object in self.container:
            if str(todo_object.id) == str(todo_id):
                return todo_object # returns an OBJECT
            
        return None 

    def remove_todo(self, todo_id): 
        """Remove an item"""
        todo_to_remove = self._find_todo(todo_id)
        if todo_to_remove: # does it exist?
            return self.container.pop(todo_id-1) 
        else:
            return False    

    def complete_todo(self, todo_id):
        """ complete a todo """
        todo_to_complete = self._find_todo(todo_id) #exists
        if todo_to_complete:
            todo_to_complete.complete = True
            
    def count_todos(self, container):
        print(len(self.container))

    def print_todos(self):
        for t in self.container:
            print([t.id, t.todo_name, t.complete])

    def save_todo(self, todo_instance): #let's you write a todo directly in to the file/ writes the add-todo() into the file. 
        with open("todos.csv", 'a+', newline ='') as csv_file:
            todo_writer = csv.writer(csv_file)
            #Todo -> todocsvrow = ['13415', 'walk dog', 'false']
            row = [todo_instance.id, todo_instance.todo_name, todo_instance.complete]
            todo_writer.writerow(row)
            

def main():
    td = TodoList()
    filename = 'todos.csv'
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file) #expecting values to sep by comma
        next(csv_reader) #to skip over the first line of headings
        for line in csv_reader:
            todo_instance = Todo(line[1], line[2], line[0])
            td.container.append(todo_instance)

    while True:
        # READ
        user_input = input("Enter 1 to create a todo, 2 to remove a todo, 3 to complete a todo, 4 to print all todos: ")
        # EVAL
        if user_input == "1":
            todo_input = input("Enter todo name: ")
            todo_instance = td.add_todo(todo_input)
            td.save_todo(todo_instance) 
        
        elif user_input == "2":
            remove_task = eval(input("Enter todo id: "))
            td.remove_todo(remove_task)
            
        elif user_input == "3":
            to_mark = eval(input("Enter todo id: "))
            td.complete_todo(to_mark)

        elif user_input == "4":
            td.print_todos()

        # LOOP
 
if __name__ == '__main__':
    main()  
