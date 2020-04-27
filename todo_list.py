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

    def __repr__(self):
        return Todo(identifier, todo_name, complete)

class TodoList(object):
    """Code needed to manage todo list"""
    
    def __init__(self):
        self.container = []
    
    
    def add_todo(self, todo_name, complete=False): #adds/creates a new todo
        """ add a todo to self.todos"""
      
        todo = Todo(todo_name, complete)
        self.container.append(todo)
        return todo


    def _find_todo(self, todo_id):
        """locate todo in todo list"""

        for todo_object in self.container:
            if str(todo_object.id) == str(todo_id):
                return todo_object # returns an OBJECT
            
        
    def remove_todo(self, todo_id): 
        """Remove an item"""

        # GOAL get the index of the todo id in the todolist container, and remove it
      
        # if todo_to_remove:
        for index, element in enumerate(self.container): 
        #element is the instance and can only be accessed in pritn
            if element.id == todo_id:
                return self.container.remove(element)
         

    def complete_todo(self, todo_id):
        """ complete a todo """
        todo_to_complete = self._find_todo(todo_id) #exists
        if todo_to_complete:
            todo_to_complete.complete = True


    def count_todos(self):
        """find out the number of todos/tasks that are in our list"""
        total_todos = (len(self.container))
        return total_todos
    
    def print_count_todos(self):

        print_todos = (len(self.container))
        print(print_todos)


    def show_todos(self):
        """Print out and view all contents/tasks in the list"""
        for t in self.container:
            printed = ([t.id, t.todo_name, t.complete])
            return printed


    def print_to_console(self):
        for t in self.container:
            printed = ([t.id, t.todo_name, t.complete])
            print(printed)   
        

    def save_todo(self, todo_instance):
        """let's you write a todo directly in to your CSV file"""
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
        user_input = input("Welcome to your Todo-List! Let's start organizing\n\nEnter 1 to Create A Todo Item\n\nEnter 2 to Remove A Todo Item\n\nEnter 3 to Mark Complete\n\nEnter 4 to View The List Of Items\n\nEnter 5 to Check Total Number of Items:\n")
        # EVAL
        if user_input == "1":
            todo_input = input("Enter the name of the todo item you would like to add: ")
            todo_instance = td.add_todo(todo_input)
            td.save_todo(todo_instance) 
        
        elif user_input == "2":
            remove_task = input("Enter the id of the todo item you would like to remove: ")
            td.remove_todo(remove_task)
            
        elif user_input == "3":
            to_mark = input("Enter the id of the todo item you want to mark as complete: ")
            td.complete_todo(to_mark)

        elif user_input == "4":
            td.print_to_console()

        elif user_input == "5":
            td.print_count_todos()
 
        # LOOP
 
if __name__ == '__main__':
    main()
