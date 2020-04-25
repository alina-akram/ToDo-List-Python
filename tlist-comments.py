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
           # return self.container.remove(todo_id)
            return self.container.pop(todo_id-1) 
            
#             try:
#                 self.container.remove(todo_id)
                
#             except ValueError:
#                 print("Na")
        else:
            return False    

    def complete_todo(self, todo_id):
        """ complete a todo """
        todo_to_complete = self._find_todo(todo_id) #exists
        
        if todo_to_complete:
            # todo_id.complete = True
            # 1.complete = True
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



        # if behavior is : save when user requests
        # self.container <- todos are in here
        # empty the csv
        # for todo in self.container
        # convert todo to list of things
        # write todo to csv

        # if behavior is : save on every add
        # update function to accept a todo argument
        # convert todo to list of things  -> todocsvrow= ['13415', 'walk dog', 'false']
        # write that list to csv
        # csv_writer.writerow(todocsvrow)




    # def save_todos(self, todo_name): #let's you write a todo directly in to the file/ writes the add-todo() into the file. 

    #     add_todo_to_csv = add_todo(todo_name)

    #     if add_todo_to_csv:
    #         my_file = open("todos.csv", "w") #would've opened file in append mode if I was loading list into my csv
    #         wr = csv.writer(my_file, quoting=csv.QUOT )
         
         #program should load csv file contents into the list that the program displays
         #adds input to dos to csv file 
         #independent of the list it prints. 


# WRITES existing todos in your todo list to the Csv
#if todo to add_todo() is true: #saves todos as adding them, could you input for after adding to save it to file. 
    # file open - writer function:
        #  with open(file_name, 'a+', newline='') as write_obj:
        # # Create a writer object from csv module
        # csv_writer = writer(write_obj) # todo_name
        # # Add contents of list as last row in the csv file
        # csv_writer.writerow(todo)



#coint todos input option. 


# from csv import writer
 
#     # Open file in append mode
   
# # taking in whole list and splitting it up


#          # open - writer function:
#          with open(file_name, 'a+', newline='') as write_obj:
#         # Create a writer object from csv module
#         csv_writer = writer(write_obj) # todo_name/container
#         # Add contents of list as last row in the csv file
#         csv_writer.writerow(container)#list of elements




def main():
    td = TodoList()
    
    # REPL <- 
    # READ, EVAL, PRINT, LOOP
    
    #write a main() asks the user to create, remove, count todos 
    
    # COUNTER EXAMPLE
    # a = 0
    # while True: 
    #     print(a)
    #     input("shit")
    # 
    # a = []
    
    # LIST EXAMPLE
    # while True: 
    #     print(len(a))
    #     input("shit")
    #     a.append("something")

# in main() i want you to read a CSV file of todos, parse it’s contents, and add them to a todo list instance  BEFORE asking user for input etc

# also, i want you to write a “save” function that WRITES existing todos in your todo list to the Csv
    # print(os.getcwd()+ "todos.csv")
    with open('todos.csv') as csv_file:
        csv_reader = csv.reader(csv_file) #expecting values to sep by comma

        next(csv_reader) #to skip over the first line of headings

        # print_list = [] #the list we will add our csv todos into 
        for line in csv_reader:
            #td.container.append(line)
            #print(line[0], line[1])
            # FILL INSTACNE OF TODOLIST WITH INSTNACES OF TODOS
            todo_instance = Todo(line[0], line[1])
            td.container.append(todo_instance)

            #['2', 'test2', ' False']


        #     print_list.append((t.id,t.todo_name, t.complete))
        # print(print_list)

   #accessing the class for the TodoList and assigning a variable to it
    while True:
        # READ
        user_input = input("Enter 1 to create a todo, 2 to remove a todo, 3 to complete a todo, 4 to print all todos:")
        
        #NOTHING ABOVE THIS
        #------------------------
        
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



             #NOTHING BELOW THIS
        #------------------------
        # print(TodoList(container)) # 1. creating a NEW list #2. referencing an undefined var        
        # LOOP
 
if __name__ == '__main__':
    main()  



# SALAR ASKS
# - based on user input, do some action (create/remove/count)
# - take user input, make a todo with it
# - if user asks to create, ask what the task is
# - if user asks to remove, ask how many to remove


# - BONUS - if user asks to remove, ask which one to remove (you'll need to change your internal list to a dictionary)
    
    
# OLD SHIT

# if user_input == 1:        
    #     new_task = TodoList() 
    #     task_name = "Alina Laundry"
    #     complete = "Y"
    #     create_todo = new_task.add_todo(task_name, complete) #accessing the add_todo function and creating a new variable to execute it
    