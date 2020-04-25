import csv
import os
import uuid

class Todo(object):
    
    def __init__(self, todo_name, complete=False):
        self.todo_name = todo_name
        self.complete = complete
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

    def save_todos(filename, container): #let's you write a todo directly in to the file/ writes the add-todo() into the file. 
        from csv import writer 
        add_list_to_csv = self.container
        with open(todos.csv, 'a+', newline ='') as write_obj: #create writer obj
            csv_writer = writer(write_obj)
            csv_writer.writerow(add_list_to_csv)


def main():
    td = TodoList()
  that WRITES existing todos in your todo list to the Csv
    
    with open('todos.csv') as csv_file:
        csv_reader = csv.reader(csv_file) #expecting values to sep by comma
        next(csv_reader) #to skip over the first line of headings
        for line in csv_reader:
            todo_instance = Todo(line[0], line[1])
            td.container.append(todo_instance)

    while True:
        # READ
        user_input = input("Enter 1 to create a todo, 2 to remove a todo, 3 to complete a todo, 4 to print all todos:")
        
        # EVAL
        if user_input == "1":
            todo_input = input("Enter todo name: ")
            td.add_todo(todo_input)
            # td.save_todo(filename, ) 
        
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
