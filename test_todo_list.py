
import unittest 

#class we want to test
#implement the methods
# - m unittest test_todo_list.py
from todo_list import Todo, TodoList

class TestTodoList(unittest.TestCase):
	""" 
	The basic class that inherits unittest.TestCase
	"""
	def setUp(self):
		self.todo_list = TodoList()

	def test_container_has_list_of_todo_instances(self):
		self.assertIsInstance(self.todo_list.container, list)

	def test_add_todo(self):
		#test if it is adding
		
		self.assertEqual(self.todo_list.count_todos(), 0) #start at 0 because empty
		self.todo_list.add_todo("Do laundry")
		self.assertEqual(self.todo_list.count_todos(), 1)
		
	def test_remove_todo(self):

		self.assertEqual(self.todo_list.count_todos(), 0)
		todo = self.todo_list.add_todo("Pick up dry cleaning")
		id_to_remove = todo.id
		self.assertEqual(self.todo_list.count_todos(), 1)
		self.todo_list.remove_todo(id_to_remove)
		self.assertEqual(self.todo_list.count_todos(), 0)


	def test_complete_todo(self):
		self.assertEqual(self.todo_list.count_todos(), 0)
		todo = self.todo_list.add_todo("Pick up dry cleaning")
		id_to_remove = todo.id
		self.todo_list.complete_todo(id_to_remove)
		self.assertEqual(self.todo_list.show_todos(), [id_to_remove, "Pick up dry cleaning", True])



if __name__ == "__main__":
	unittest.main()



# if __name__ == '__main__':
#     person = Person()
#     print('User Abbas has been added with id ', person.set_name('Abbas'))
#     print('User associated with id 0 is ', person.get_name(0))